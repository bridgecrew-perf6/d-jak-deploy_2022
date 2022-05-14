from fastapi.testclient import TestClient
import pytest
import datetime
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"start": "1970-01-01"}

# @pytest.mark.parametrize("name", ['Zenek', 'Marek', 'Alojzy Niezdąży'])
# def test_hello_name(name):
#     # name = 'elo'
#     response = client.get(f"/hello/{name}")
#     assert response.status_code == 200
#     assert response.json() == {'msg': f"Hello {name}"}


def test_receive_something():
    response = client.put("/events", json={'date': '2022-02-02', 'event':'mamma'})
    assert response.json() == {'id': 0,
                                'name': 'mamma',
                                'date': '2022-02-02',
                                'date_added': datetime.date.today().isoformat()}

def test_receive_something2():
    response = client.put("/events", json={'date': '2022-02-02', 'event':'pappa'})
    assert response.json() == {'id': 1,
                                'name': 'pappa',
                                'date': '2022-02-02',
                                'date_added': datetime.date.today().isoformat()}

def test_read():
    response = client.get("/events/2022-02-02")
    assert response.status_code == 200
    assert response.json() == [{'id': 0,
                                'name': 'mamma',
                                'date': '2022-02-02',
                                'date_added': datetime.date.today().isoformat()},
                                {'id': 1,
                                'name': 'pappa',
                                'date': '2022-02-02',
                                'date_added': datetime.date.today().isoformat()}]
                                
def test_no_events():
    response = client.get("/events/2023-02-02")
    assert response.status_code == 400
    

def test_receive_something3():
    response = client.put("/events", json={"date": "2022-03-22", "event": "Drugi dzień wiosny"})

def test_read_newdata():
    response = client.get("/events/2022-0309-22")
    assert response.status_code == 404
