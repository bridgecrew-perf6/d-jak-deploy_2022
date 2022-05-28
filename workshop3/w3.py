from fastapi import Request, FastAPI, Query
from fastapi.responses import (
    HTMLResponse,
    JSONResponse,
    PlainTextResponse,
    RedirectResponse
)
from typing import List
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
app = FastAPI()

@app.get("/reqest_query_string_discovery/")
def read_items(u: str = Query("default"), q: List[str] = Query(None)):
    query_items = {"q": q, "u": u}
    return query_items

@app.get("/jinja",response_class=HTMLResponse)
def read_item(request: Request, my_string: str = Query("Wheeeee!"), my_list: List[str] = Query(None)):
    my_list = my_list or [1,2,3,4]
    return templates.TemplateResponse("index.html.j2", {
        "request": request, 
        "my_string": my_string, 
        "my_list": my_list })


@app.get("/simple_path_tmpl/{sample_variable}")
def simple_path_tmpl(sample_variable: str):
    print(f"{sample_variable=}")
    print(type(sample_variable))
    return {"sample_variable": sample_variable}

@app.get("/muza/{artist}/{album}/{track_no}")
def music_path(artist: str, album: str, track_no: int):
    print(f"{artist=}")
    print(f"{album=}")
    print(f"{track_no=}")

    return {
        "artist": artist,
        "album": album,
        "track_no": track_no
    }

objects = {
    1: {"field_a": "1a", "field_b": "1b"},
    2: {"field_a": "2a", "field_b": "2b"},
    3: {"field_a": "3a", "field_b": "3b"},
    # .... #
}

@app.get("/db/{id}/{field}")
def db(id: int, field: str):
    return {"field": objects.get(id,{}).get(f"field_{field}")}


# @app.get("/test_request/")
# def read_params(request: Request):
#     print(f"{request.query_params=}")
#     return request.query_params

# @app.get("/static", response_class=HTMLResponse)
# def index_static():
#     return """
#     <html>
#         <head>
#             <title>Some HTML in here</title>
#         </head>
#         <body>
#             <h1>Look Ma! HTML!</h1>
#         </body>
#     </html>
#     """




