from fastapi.testclient import TestClient
import pytest
from main import app
from main import get_person
from models import Persona

client = TestClient(app)


async def test_get():
    # Set up any necessary fixtures or mocks
    item_id = 1
    expected_result = {"id": 1, "name": "prueba", "age": "20"}

    # Call the async function being tested
    result = await get_person(item_id)

    assert result == expected_result

# @pytest.mark.asyncio
# async def test_get_job():
#     # Set up any necessary fixtures or mocks
#     item_id = 1
#     expected_result = {
#         "id": 1,
#         "name": "prueba",
#         "age": "20"
#     }

#     # Call the async function being tested
#     result = await read_main(item_id)

#     assert result 

    # Assert that the function returned the expected result
    # assert result == expected_result

# async def test_read_item():
#     response = client.get("/items/2", headers={"X-Token": "coneofsilence"})
#     assert response.status_code == 200
#     assert response.json() == {
#         "id": 2,
#         "name": "Roberlina",
#         "age": "20"
#     }


# def test_read_item_bad_token():
#     response = client.get("/items/2", headers={"X-Token": "hailhydra"})
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid X-Token header"}


# def test_read_inexistent_item():
#     response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Item not found"}


# async def test_create_item():
#     print('hola')
    # response = client.post(
    #     "/items/",
    #     headers={"X-Token": "coneofsilence"},
    #     json={
    #         "name": "Roberlina",
    #         "age": "20"
    #     },
    # )

    # assert response.status_code == 200, response.text
    # data = response.json()
    # assert data["name"] == "Roberlina"


# def test_create_item_bad_token():
#     response = client.post(
#         "/items/",
#         headers={"X-Token": "hailhydra"},
#         json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
#     )
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid X-Token header"}


# def test_create_existing_item():
#     response = client.post(
#         "/items/",
#         headers={"X-Token": "coneofsilence"},
#         json={
#             "id": "foo",
#             "title": "The Foo ID Stealers",
#             "description": "There goes my stealer",
#         },
#     )
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Item already exists"}