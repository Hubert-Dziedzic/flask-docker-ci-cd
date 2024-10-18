# Flask Docker App with Unit Tests

This project is a simple Flask web application containerized using Docker. It includes basic unit tests to ensure that the application works as expected. The project demonstrates best practices for deploying a Flask app in Docker and running automated tests.

## Features
- Simple Flask application that returns "Hello, World!" on the main route.
- Dockerized environment for easy deployment and isolation.
- Unit tests to ensure the app works as expected.

## Built With
- Python (Flask)
- Docker
- Flask-Testing
  
## Requirements
- Docker
- Docker Compose

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Hubert-Dz/flask-docker-app.git
   cd flask-docker-app
   
   docker build -t flask-docker-app .
   docker run -p 5000:5000 flask-docker-app
  The app will be accessible at http://localhost:5000 and will display "Hello, World!".

## Running Tests

1. To run unit tests inside the Docker container:

   ```bash
   docker build -t flask-docker-app --target test .

## Project Structure
flask-docker-app/ 
├── app.py # Main Flask application 
├── Dockerfile # Docker configuration 
├── requirements.txt # Python dependencies 
├── test_app.py # Unit tests 
└── README.md # Project documentation

## Author

- [Hubert Dziedzic](https://github.com/Hubert-Dziedzic)
