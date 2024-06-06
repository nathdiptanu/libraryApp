# Library Application

This is a simple library application built with Flask that supports basic CRUD operations on books. The API documentation is available via Swagger.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)
- Docker (for Dockerizing the application)

## Installation

1. Clone the repository or download the source code.

2. Navigate to the project directory.

3. Install the required Python packages using `pip`:

    ```bash
    pip install Flask==2.1.3 Flask-RESTful==0.3.9 flasgger==0.9.5
    ```

## Running the Application

1. After installing the dependencies, you can run the Flask application:

    ```bash
    python run.py
    ```

2. The application will start on `http://localhost:5000`.

## Using Swagger

1. Once the application is running, you can access the Swagger UI for API documentation at:

    ```text
    http://localhost:5000/api/docs/
    ```
Jenkins password 

    C:\ProgramData\Jenkins\.jenkins\secrets\initialAdminPassword


2. The Swagger documentation will provide details on the available endpoints, request parameters, and response schema.

## Finding the Schema

The schema for the API can be found in the Swagger UI. By accessing the Swagger documentation, you can view the detailed schema definitions for each API endpoint.

## Dockerizing the Application

To run the application in a Docker container, follow these steps:

1. Create a `Dockerfile` in the project directory with the following content:

    ```dockerfile
    # Use the official Python image from the Docker Hub
    FROM python:3.9-slim

    # Set the working directory in the container
    WORKDIR /app

    # Copy the current directory contents into the container at /app
    COPY . /app

    # Install the required packages
    RUN pip install Flask==2.1.3 Flask-RESTful==0.3.9 flasgger==0.9.5

    # Make port 5000 available to the world outside this container
    EXPOSE 5000

    # Define environment variable
    ENV FLASK_APP=run.py

    # Run the application
    CMD ["flask", "run", "--host=0.0.0.0"]
    ```

2. Build the Docker image:

    ```bash
    docker build -t library-app .
    ```

3. Run the Docker container:

    ```bash
    docker run -p 5000:5000 library-app
    ```

4. The application will be accessible at `http://localhost:5000`.


## Summary

- To run the application locally: `python run.py`
- To access the Swagger documentation: `http://localhost:5000/api/docs/`
- To dockerize the application:
  - Create a `Dockerfile`
  - Build the Docker image: `docker build -t library-app .`
  - Run the Docker container: `docker run -p 5000:5000 library-app`
