import datetime
from typing import Dict

from fastapi import FastAPI, HTTPException

from pydantic import BaseModel


app = FastAPI()
days = {"monday": 1, "tuesday": 2, "wednesday":3, "thursday":4, "friday":5, "saturday":6, "sunday": 7}
events = dict()

def validate_date(date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return False
        return True

@app.get("/")
def root():
    return {"start": "1970-01-01"}

class GiveMethodResp(BaseModel):
    method: str

# class GiveMeSomethingResp(BaseModel):
#     received: Dict
#     constant_data: str = "python jest super"

@app.get("/method", status_code=200, response_model=GiveMethodResp)
def return_get():
    return {"method": "GET"}

@app.delete("/method", status_code=200, response_model=GiveMethodResp)
def return_delete():
    return GiveMethodResp(method="DELETE", status_code=200, response_model=GiveMethodResp)

@app.options("/method", status_code=200, response_model=GiveMethodResp)
def return_options():
    return GiveMethodResp(method="OPTIONS")

@app.put("/method", status_code=200, response_model=GiveMethodResp)
def return_put():
    return GiveMethodResp(method="PUT")

@app.post("/method", status_code=201, response_model=GiveMethodResp)
def return_post():
    return GiveMethodResp(method="POST")

@app.get("/day", status_code=200)
def check_name_number(name: str, number: int):
    if name in days.keys():
        if days[name] == number:
            return {"day":f"{name}"}
    raise HTTPException(status_code=400, detail="Day and number are not matching")
    

class NewEventRq(BaseModel):
    date: str
    event: str


class NewEventResp(BaseModel):
    id: int
    name: str
    date: str
    date_added: str

@app.put("/events", response_model=NewEventResp)
def create_event(new_event: NewEventRq):
    new_event.date 
    global events
    if len(events.keys()) == 0:
        ind = 0
    else:
        ind = max(events.keys()) + 1
        
    new_date_added = datetime.date.today().isoformat()
    
    events.update({ind:{"name": new_event.event, "date": new_event.date, "date_added": new_date_added}})
    
    return NewEventResp(id = ind, name = new_event.event, date=new_event.date, date_added=new_date_added)
    


@app.get("/events/{date}", status_code=200)
def return_events(date: str):
    if validate_date(date) == True:
        returned_events = []
        counter = 0
        for key, val in events.items():
            if val['date'] == date:
                returned_events.append({'id': key, 'name':val['name'], 'date':date, 'date_added':val['date_added']})
                counter += 1
        if counter != 0:
            return tuple(returned_events)
        else:
            raise HTTPException(status_code=404, detail="No events")

    else:
        raise HTTPException(status_code=400, detail="Invalid data")

    # return tuple(returned_events)


class HelloResp(BaseModel):
    msg: str


# @app.get("/hello/{name}", response_model=HelloResp)
# def read_item(name: str):
#     return HelloResp(msg=f"Hello {name}")

# class GiveMeSomethingRq(BaseModel):
#     first_key: str


# class GiveMeSomethingResp(BaseModel):
#     received: Dict
#     constant_data: str = "python jest super"


# @app.post("/dej/mi/coś", response_model=GiveMeSomethingResp)
# def receive_something(rq: GiveMeSomethingRq):
#     return GiveMeSomethingResp(received=rq.dict())

