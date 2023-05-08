from fastapi import FastAPI
from src.events import start_handler
from src.api import hello
from src.api.v1 import welcome

app_title = 'Minimalistic FastAPI API Starter Template'
app_description = '''This is a minimalistic FastAPI API starter template 
that provides a basic project structure for various types of backend 
services. It aims to save time by eliminating the need to set up a simple 
API project and allows developers to focus on specific use cases or extend 
the template for more complex requirements. The template is designed with 
Docker in mind, enabling you to easily run the API using Docker-compose.'''

app = FastAPI(title=app_title,
              description=app_description)

app.add_event_handler('startup', start_handler(app))

app.include_router(hello.router)
app.include_router(welcome.router)
