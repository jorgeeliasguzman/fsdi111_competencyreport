import requests

TEST_USER = {
    "first_name": "Juan",
    "last_name": "Doe",
    "hobbies": "Skiing and playing ping pong",
    "active": 1
}

URL = "http://127.0.0.1:5000/users"

def test_user_creation():
    out = requests.post(URL, json=TEST_USER)
    if out.status_code == 201:
        print(out.json())
    else:
        print("Something went wrong.")


def test_user_deactivate():
    out = requests.delete("%s/2" % URL)
    if out.status_code == 200:
        print(out.json())
    else:
        print("something went wrong while trying to deactivate.")

if __name__ == "__main__":
    test_user_creation()
    test_user_deactivate()