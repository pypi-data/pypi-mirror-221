from fastapi.testclient import TestClient
from cow_api.main import app, Cow, Weight, Feeding, MilkProduction

client = TestClient(app)


class TestAPI:
    def test_cows_endpoint_returns_200(self):
        response = client.get("/cows")
        assert response.status_code == 200

    def test_get_cows_endpoint_returns_nonempty_list(self):
        response = client.get("/cows")
        assert response.json() != []

    def test_post_cows_endpoint_returns_201(self):
        cow = Cow.generate_fake()
        response = client.post("/cows/", json=cow.model_dump())
        assert response.status_code == 201

    def test_post_cows_endpoint_returns_cow(self):
        cow = Cow.generate_fake()
        response = client.post("/cows/", json=cow.model_dump())
        assert response.json() == cow.model_dump()

    def test_put_cows_endpoint_returns_200(self):
        first_cow_id = client.get("/cows").json()[0]["id"]
        new_cow = Cow.generate_fake()
        response = client.put(f"/cows/{first_cow_id}", json=new_cow.model_dump())
        assert response.status_code == 200

    def test_put_cows_update_name_returns_new_name(self):
        first_cow_id = client.get("/cows").json()[0]["id"]
        new_cow = Cow.generate_fake()
        response = client.put(f"/cows/{first_cow_id}", json=new_cow.model_dump())
        new_cow_name = client.get(f"/cows/{new_cow.id}").json()["name"]
        assert response.json()["name"] == new_cow_name

    def test_delete_cows_endpoint_returns_200(self):
        first_cow_id = client.get("/cows").json()[0]["id"]
        response = client.delete(f"/cows/{first_cow_id}")
        assert response.status_code == 200

    def test_filter_cows_endpoint(self):
        # Try to filter by female cows
        response = client.get("/cows/filter/sex?value=Female")
        assert response.status_code == 200

        cows = response.json()
        # Check if all cows returned are female
        assert all(cow["sex"] == "Female" for cow in cows)

        # Try to filter by male cows
        response = client.get("/cows/filter/sex?value=Male")
        assert response.status_code == 200

        cows = response.json()
        # Check if all cows returned are male
        assert all(cow["sex"] == "Male" for cow in cows)
