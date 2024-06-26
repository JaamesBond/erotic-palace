import json
import requests
from config import CONFIG


def add_girl(name, age, hair_colour, phone, boobs=None, ass=None, race=None, bmi=None, personality=None, services=None):
    arguments = locals()
    new_girl = {}
    print(arguments)
    for arg in arguments:
        new_girl.update({arg: arguments[arg]})

    print(new_girl)

    response = requests.post(f"{CONFIG['api']['url']}/girls", json=new_girl)
    return int(response.text)


def list_of_girls():
    response = requests.get(f"{CONFIG['api']['url']}/girls")
    girls = json.loads(response.text)

    return girls


def get_girl_by_id(id):
    response = requests.get(f"{CONFIG['api']['url']}/girls/{id}")
    girl = json.loads(response.text)

    return girl


def get_girl_by_name(name):
    response = requests.get(f"{CONFIG['api']['url']}/girls/{name}")
    girl = json.loads(response.text)

    return girl


def update_girl(girl):
    print(girl)
    response = requests.put(f"{CONFIG['api']['url']}/girls/{girl['id']}", json=girl)
    girl = json.loads(response.text)

    return girl['id']


def delete_girl(id):
    requests.delete(f"{CONFIG['api']['url']}/girls/{id}")
