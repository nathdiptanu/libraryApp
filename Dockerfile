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