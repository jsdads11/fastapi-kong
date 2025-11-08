# cd /Users/tonyodonnell/Library/Mobile Documents/com~apple~CloudDocs/Dev/Kong-FastAPI5/app

# https://fastapi.tiangolo.com/deployment/docker/#docker-cache
#
# ------------------------------------------------------------------------------------------------------ #

# Python FastAPI Standalone App setup

# ----------------
# WORKS! #
# ----------------
# python3 -m venv .venv-api .
# source bin/activate && pip install -r requirements.txt
# fastapi dev main.py         // or uvicorn main:app --reload
# ------------------------------------------------------------------------------------------------------ #

# ----------------
# WORKS NOW TOO! #
# ----------------
# Python App Docker setup
# -----------------------
# pip install -r requirements.txt
#             >> fastapi[standard]>=0.113.0,<0.114.0ls -
#             >> pydantic>=2.7.0,<3.0.0
# Create an app directory and cd into it.
# Create an empty file __init__.py
# Create a main.py file with the code below:
#
#├── app
#│   ├── __init__.py
#│   └── main.py
#├── Dockerfile
#└── requirements.txt

# // Build your FastAPI image and run the docker container standalone
# docker build -t myimage .
# // Run the docker container
# docker run -d --name mycontainer -p 8005:8005 myimage

# docker ps -a: To see all the running containers in your machine.
# docker stop myimage       // <container_id>: To stop a running container // 
# docker rm mycontainer     //<container_id>: To remove/delete a docker container(only if it stopped).
# docker image ls: To see the list of all the available images with their tag, image id, creation time and size.
# docker rmi <image_id>: To delete a specific image.

# ------------------------------------------------------------------------------------------------------ #
# Run Kong, Postgres, and FastAPI together
# KONG_DATABASE=postgres docker compose --profile database up -d
# Then add service and route in Kong

# add service "fastapi-anal-sent-svc"
# curl -i -X POST http://localhost:8001/services/ --data name=fastapi-random-svc --data host="127.0.0.0" --data url='http://fastapi:8005/'

# add route "fastapi-anal-sent-route"  (by path)
# curl -i -X POST http://localhost:8001/services/fastapi-random-svc/routes --data name=fastapi-random-route --data 'paths[]=/'

# Create and run Dockerfile with the following content: // python 3.11 is out there now ! 
# >>    FROM python:3.9
# >>    WORKDIR /code
# >>    COPY ./requirements.txt /code/requirements.txt
# >>    RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# >>    COPY ./app /code/app
# >>    CMD ["uvicorn", "main:app","--reload","--host", "0.0.0.0", "--port", "8005"]


# You should be able to check it in your Docker container's URL, for example: 
# http://127.0.0.1/items/5?q=somequery
# http://0.0.0.0
# http://127.0.0.1/docs
# curl http://127.0.0.1/items/5?q=somequery

# run Kong, Postgres, and FastAPI together
# KONG_DATABASE=postgres docker compose --profile database up -d
# Then add service and route in kong
# 
# add service "fastapi-service"
# curl -i -X POST http://localhost:8001/services/ --data name=fastapi-service --data url='http://fastapi:8005/'

# add route "fastapi-route"  (by path)
# curl -i -X POST http://localhost:8001/services/fastapi-service/routes --data name=fastapi-route --data 'paths[]=/api/hello'
# 
# ------------------------------------------------------------------------------------------------------ #

# "/" returns Hello World - "/items/{item_id}" returns item_id and optional query param q
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
