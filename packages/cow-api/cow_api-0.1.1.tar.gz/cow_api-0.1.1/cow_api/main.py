from cow_api.models import Cow
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from loguru import logger
from typing import List, Optional

import json

logger.add("cow_api.log", rotation="500MB")

all_cows: List[Cow] = [Cow.generate_fake() for _ in range(100)]

app = FastAPI(title="Cow API", version="0.1.0")


@app.get("/cows", status_code=200, response_model=List[Cow])
async def get_cows() -> List[Cow]:
    """
    Get all cows.

    Returns:
        list: List of cows."""
    logger.success("Successfully retrieved all cows.")
    return all_cows


@app.get("/cows/{cow_id}", status_code=200, response_model=Cow)
async def get_single_cow(cow_id: str) -> Cow | None:
    """
    Get single cow based on id.

    Returns:
        Single Cow."""

    for cow in all_cows:
        if cow.id == cow_id:
            logger.success("Successfully retrieved single cow.")
            return cow


@app.post("/cows/", status_code=201)
async def add_cow(cow: Cow) -> Cow:
    """
    Add a cow.

    Returns:
        Dict: same payload as the one sent with 201 status code on success.
    """
    all_cows.append(cow)
    logger.success("Successfully added cow.")
    return cow


@app.put("/cows/{cow_id}", status_code=200, response_model=Cow)
async def update_cow(cow_id: str, cow: Cow) -> Cow:
    """
    Update a cow.

    Returns:
        Dict: same payload as the one sent with 200 status code on success.
    """
    for i, existing_cow in enumerate(all_cows):
        if existing_cow.id == cow_id:
            all_cows[i] = cow
            logger.success("Successfully updated cow.")
            return cow
    logger.error("Cow not found.")
    raise HTTPException(status_code=404, detail="Cow not found")


@app.delete("/cows/{cow_id}", status_code=200)
async def delete_cow(cow_id: str) -> Cow:
    """
    Delete a cow.

    Returns:
        Dict: same payload as the one sent with 200 status code on success.
    """
    for i, existing_cow in enumerate(all_cows):
        if existing_cow.id == cow_id:
            del all_cows[i]
            logger.success("Successfully deleted cow.")
            return existing_cow
    logger.error("Cow not found.")
    raise HTTPException(status_code=404, detail="Cow not found")


def filter_cow(cow: Cow, field: str, value: str) -> bool:
    # This assumes that the field is a nested field using '.', e.g. "weight.mass_kg"
    fields = field.split(".")
    temp_value = cow

    # Traverse the nested fields and check if the value matches.
    for f in fields:
        if hasattr(temp_value, f):
            temp_value = getattr(temp_value, f)
        else:
            return False
    try:
        # Attempt to convert the value to json. This will handle boolean and numeric values correctly.
        value = json.loads(value)
    except json.JSONDecodeError:
        # If the value cannot be converted, leave it as is. It is likely a string.
        pass
    return temp_value == value


@app.get("/cows/filter/{field}", response_model=List[Cow])
async def filter_cows(field: str, value: Optional[str] = None) -> List[Cow]:
    """
    Filter cows based on the field and value provided.

    Returns:
        list: List of filtered cows.
    """
    if not value:
        logger.warning("Found no value to filter by. Returning all cows.")
        return all_cows

    filtered_cows = [cow for cow in all_cows if filter_cow(cow, field, value)]

    if len(filtered_cows) == 0:
        logger.warning(
            f"Found no cows matching the filter, based on {field}. Returning all cows."
        )
        return all_cows

    logger.success("Successfully filtered cows.")
    return filtered_cows


@app.get("/healthcheck", status_code=200)
def healthcheck() -> JSONResponse:
    logger.success("Successfully healthchecked.")
    return JSONResponse(content=jsonable_encoder({"status": "Ok"}))
