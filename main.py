import requests
from datetime import datetime

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")
yesterday = datetime(year=2022, month=1, day=21)
yesterday_formatted = yesterday.strftime("%Y%m%d")

USER_NAME = "fanyu"
TOKEN = "pixelaisfun"
GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la"
CREATE_USER_ENDPOINT = "/v1/users"
CREATE_GRAPH_ENDPOINT = f"/v1/users/{USER_NAME}/graphs"
POST_VALUE_ENDPOINT = f"/v1/users/{USER_NAME}/graphs/{GRAPH_ID}"
UPDATE_PIXEL_ENDPOINT = f"/v1/users/{USER_NAME}/graphs/{GRAPH_ID}/{yesterday_formatted}"
DELETE_PIXEL_ENDPOINT = f"/v1/users/{USER_NAME}/graphs/{GRAPH_ID}/{yesterday_formatted}"

create_user_json = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# user_response = requests.post(url=f"{PIXELA_ENDPOINT}{CREATE_USER_ENDPOINT}", json=create_user_json)

create_graph_json = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=f"{PIXELA_ENDPOINT}{CREATE_GRAPH_ENDPOINT}",
#                                json=create_graph_json, headers)

post_value_json = {
    "date": today_formatted,
    "quantity": "6",
}

# response = requests.post(url=f"{PIXELA_ENDPOINT}{POST_VALUE_ENDPOINT}", json=post_value_json,
#                          headers=headers)

update_pixel_json = {
    "quantity": "1"
}

# update_pixel_response = requests.put(url=f"{PIXELA_ENDPOINT}{UPDATE_PIXEL_ENDPOINT}",
#                                      json=update_pixel_json, headers=headers)
# print(update_pixel_response.text)

delete_pixel_response = requests.delete(url=f"{PIXELA_ENDPOINT}{DELETE_PIXEL_ENDPOINT}", headers=headers)
print(delete_pixel_response.text)
