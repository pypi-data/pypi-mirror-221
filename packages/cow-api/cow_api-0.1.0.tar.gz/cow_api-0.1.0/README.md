# Cow Assignment

### Description

This is a simple cow API that allows you to create, read, update, and delete cows using a RESTful API built with FastAPI.

### Features

1. Fetch all cows or a single cow based on its ID.
2. Create a new cow.
3. Update the details of an existing cow.
4. Delete a cow based on its ID.
5. Filter cows based on their attributes.

### Installation

Install the package using pip:

`pip install cow_api`

### Usage

After installation, you can run the application using uvicorn:

`uvicorn cow_api.main:app --reload`
Then navigate to http://localhost:8000/docs in your web browser to access the API.

### Testing

Tests are located in the tests directory. To run tests, navigate to the root directory of the application and execute the following command:

`pytest`
