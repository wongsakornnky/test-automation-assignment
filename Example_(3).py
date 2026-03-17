import requests

headers = {
    "x-api-key": "reqres_27c324eec5224bceb06954a52ccc3d67"
}

# Test Case 1
response = requests.get("https://reqres.in/api/users/12", headers=headers)

print("Status Code:", response.status_code)

assert response.status_code == 200

data = response.json()["data"]

assert data["id"] == 12
assert data["email"] == "rachel.howell@reqres.in"
assert data["first_name"] == "Rachel"
assert data["last_name"] == "Howell"
assert data["avatar"] == "https://reqres.in/img/faces/12-image.jpg"

print("Test Case 1 Passed")


# Test Case 2
response = requests.get("https://reqres.in/api/users/1234", headers=headers)

print("Status Code:", response.status_code)

assert response.status_code == 404
assert response.json() == {}

print("Test Case 2 Passed")
