import pytest
import requests
from configuration import token_y_poligon

url = f"https://cloud-api.yandex.net/v1/disk/resources"
headers = {"Authorization": token_y_poligon}

def test_success_create_folder_201():
    folder_name = "success test 1"
    creating_folder_url = f"{url}?path={folder_name}"
    response = requests.put(creating_folder_url, headers=headers)

    assert response.status_code == 201

def test_success_create_folder_400():
    folder_name = "success test 2"
    creating_folder_url = f"{url}?{folder_name}"
    response = requests.put(creating_folder_url, headers=headers)

    assert response.status_code == 400

def test_success_create_folder_409():
    folder_name = "success test 1"
    creating_folder_url = f"{url}?path={folder_name}"
    response = requests.put(creating_folder_url, headers=headers)

    assert response.status_code == 409

def test_success_create_folder_404():
    url = f"https://cloud-api.yandex.net/v1/disk/resource"
    folder_name = "success test 4"
    creating_folder_url = f"{url}?path={folder_name}"
    response = requests.put(creating_folder_url, headers=headers)

    assert response.status_code == 404