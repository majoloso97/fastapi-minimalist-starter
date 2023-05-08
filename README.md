# Minimalistic FastAPI API Starter Template

This is a minimalistic FastAPI API starter template that provides a basic project structure for various types of backend services. It aims to save time by eliminating the need to set up a simple API project and allows developers to focus on specific use cases or extend the template for more complex requirements. The template is designed with Docker in mind, enabling you to easily run the API using Docker-compose.

[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/) [![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/) [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)

## Features

- Minimalistic design for quick setup
- FastAPI framework for high-performance and asynchronous web development
- Docker support for easy deployment and scalability
- Extensible project structure for different backend service needs
- Example endpoints and configuration for basic functionality

## Prerequisites

Before getting started with this minimalistic API starter template, ensure that you have the following prerequisites installed:

- Git (to manage code version control, you can get it from the [website](https://git-scm.com/downloads)) 
- A code editor of your preference ([VSCode](https://code.visualstudio.com/) is a great starter code editor)
- Docker with docker-compose (for running the API using Docker-compose, Python and requirements are installed through docker-compose, you can download it from the [official Docker site](https://www.docker.com/))

## Getting Started

To create a new project based on this minimalistic API template, follow these steps:

1. Fork the original repository: 

   - [Visit the original repository on GitHub](https://github.com/majoloso97/fastapi-minimalist-starter).
   - Click on the "Fork" button at the top-right corner of the repository page.
   - Choose your GitHub account to create a fork of the repository.
   - You can use a different name for your project.
   - Click the "Create Fork" button.

    Forking the original repository is recommended so you can create a separate copy of the project under your GitHub account, which allows you to make modifications without affecting the original template project. This way, you can set up your own repository and have full control over it.

2. Clone your forked repository:

   ```bash
   git clone https://github.com/your-username/your-api-project.git
   ```

3. If you're using VSCode, you can open a new VSCode window with the project code with:

   ```bash
   code fastapi-minimalist-starter
   ```

4. Change into the project directory:

   ```bash
   cd fastapi-minimalist-starter
   ```

5. Start the API using Docker-compose:

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker image and start the API container.

6. Access the automatic API documentation using the following URL:

   ```
   http://localhost/docs
   ```

7. Access the API example endpoints:

   ```
   GET
   http://localhost:8000/api/hello
   ```
   ```
   POST
   http://localhost:8000/api/v1/welcome
   Body (optional): {"first_name": "John", "last_name": "DOE}
   ```


8. Modify the project according to your specific needs.

## Project Structure

The project structure of this minimalistic API template is organized as follows:

```
fastapi-minimalist-starter/
├── src/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   └── welcome.py
│   │   ├── __init__.py
│   │   └── hello.py
│   ├── __init__.py
│   ├── events.py
│   ├── main.py
│   ├── schema.py
│   └── settings.py
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

- **src**: Contains the main application source code.
  - **api**: Contains API-related modules.
    - **v1**: Contains routes for the V1 API endpoints.
      - **\_\_init\_\_.py**: Initializes the V1 module.
      - **welcome.py**: Defines the `/api/v1/welcome` endpoint and handler.
    - **\_\_init\_\_.py**: Initializes the API module.
    - **hello.py**: Defines the `api/hello` endpoint and handler.
  - **\_\_init\_\_.py**: Initializes the application.
  - **events.py**: Event handlers for the API server (startup, shut down, etc).
  - **main.py**: Entrypoint of the API application.
  - **schema.py**: Basic schemas for response/request body.
  - **settings.py**: Configuration settings for the API.

- **.gitignore**: Specifies files and directories to ignore in git version control.
- **docker-compose.yml**: Docker-compose configuration for running the API container. Environment variables to pass to the container are added here under the `environment` key.
- **Dockerfile**: Dockerfile for building the API image. Optionally, for local development, you can add the `--reload` flag to the CMD command. Be sure to remove it when deploying to production.
- **README.md**: Main documentation for the template project.
- **requirements.txt**: Lists the Python dependencies required for the project.

Feel free to extend or modify the project structure based on your specific use cases.

## Customization

To customize this minimalistic API starter template, consider the following steps:

- Modify the `README.md` file to document your own efine your own API endpoints and handlers.
- Modify the `docker-compose.yml` file to match the image and container name to your new project name. 
- Add a `.env` file to the project root and adjust the variables in the `docker-compose.yml` file as bash variables (for example: `YOUR_ENV_VAR=$YOUR_ENV_VAR`). This allows you to add environment variables that you need to pass to the container, such as passwords, keys, etc, while not exposing the actual values. It's suggested to use the same variable names in both the `.env` and `docker-compose.yml` to keep consistency.
- Modify the `src/api/routes.py` file to define your own API endpoints and handlers.
- Update the `src/settings.py` file to adjust the configuration settings of the API. Adjust the Settings class to add variables as needed.
- Update the Dockerfile if needed.
- Extend the project structure by adding additional modules, services, or integrations as needed.