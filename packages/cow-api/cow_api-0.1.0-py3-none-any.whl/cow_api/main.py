from fastapi import FastAPI, HTTPException
from faker import Faker
from typing import List, Optional
from pydantic import BaseModel
import uuid
import json

fake = Faker()
Faker.seed(1)


class Weight(BaseModel):
    mass_kg: float
    last_measured: str


class Feeding(BaseModel):
    amount_kg: float
    cron_schedule: str
    last_measured: str


class MilkProduction(BaseModel):
    last_milk: str
    cron_schedule: str
    amount_l: float


class Cow(BaseModel):
    id: str
    name: str
    sex: str
    birthdate: str
    condition: str
    weight: Weight
    feeding: Feeding
    milk_production: MilkProduction
    has_calves: bool

    @classmethod
    def generate_fake(cls):
        return cls(
            id=str(uuid.uuid4()),
            name=fake.first_name(),
            sex=fake.random_element(elements=["Male", "Female"]),
            birthdate=str(fake.date_time()),
            condition=fake.random_element(elements=["Healthy", "Sick"]),
            weight=Weight(
                mass_kg=fake.random_int(min=1000, max=1500),
                last_measured=str(fake.date_time()),
            ),
            feeding=Feeding(
                amount_kg=fake.random_int(min=1, max=10),
                cron_schedule="0 */6 * * *",
                last_measured=str(fake.date_time()),
            ),
            milk_production=MilkProduction(
                last_milk=str(fake.date_time()),
                cron_schedule="0 8,12,16,20 * * *",
                amount_l=fake.random_int(min=1, max=10),
            ),
            has_calves=fake.random_element(elements=[True, False]),
        )


all_cows: List[Cow] = [Cow.generate_fake() for _ in range(100)]


app = FastAPI()


@app.get("/cows", status_code=200, response_model=List[Cow])
async def get_cows() -> List[Cow]:
    """
    Get all cows.

    Returns:
        list: List of cows."""
    return all_cows


@app.get("/cows/{cow_id}", status_code=200, response_model=Cow)
async def get_single_cow(cow_id: str) -> Cow | None:
    """
    Get single cow based on id.

    Returns:
        Single Cow."""

    for cow in all_cows:
        if cow.id == cow_id:
            return cow


@app.post("/cows/", status_code=201)
async def add_cow(cow: Cow):
    """
    Add a cow.

    Returns:
        Dict: same payload as the one sent with 201 status code on success.
    """
    all_cows.append(cow)
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
            return cow
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
            return existing_cow
    raise HTTPException(status_code=404, detail="Cow not found")


def filter_cow(cow: Cow, field: str, value: str):
    fields = field.split(".")
    temp_value = cow
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
async def filter_cows(field: str, value: Optional[str] = None):
    """
    Filter cows based on the field and value provided.

    Returns:
        list: List of filtered cows.
    """
    if not value:
        return all_cows

    filtered_cows = [cow for cow in all_cows if filter_cow(cow, field, value)]

    return filtered_cows
