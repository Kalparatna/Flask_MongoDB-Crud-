
# Flask MongoDB CRUD Application

## Overview
This is a simple Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for managing user resources. The application includes a basic user interface built with HTML and utilizes RESTful API principles.

## Features
- User registration and management
- View, edit, and delete user information
- Data validation using Pydantic

## Technologies Used
- Flask
- Flask-PyMongo
- MongoDB
- Docker
- HTML/CSS (Bulma for styling)

## Prerequisites
- Docker and Docker Compose installed on your machine
- Basic knowledge of Flask and RESTful APIs

## Project Structure
```
flask_mongo_crud/
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
├── config.py
├── models/
│   └── user.py
├── routes/
│   └── user_routes.py
├── templates/
│   ├── base.html
│   ├── user_list.html
│   ├── user_form.html
└── utils/
    └── db.py
```

## Setup Instructions

### 1. Clone the Repository
Open your terminal and run the following command to clone the repository:
```bash
git clone <git@github.com:Kalparatna/Flask_MongoDB-Crud-.git>
cd flask_mongo_crud
```

### 2. Build and Run with Docker
Use Docker Compose to build and run the application along with MongoDB:
```bash
docker-compose up --build
```

This command will:
- Build the Docker image defined in the `Dockerfile`.
- Start a MongoDB container and the Flask application.

### 3. Access the Application
Once the containers are up and running, open your web browser and navigate to:
```
http://localhost:5000/users
```

## API Endpoints
You can also access the API endpoints directly using Postman or any API testing tool.

- **GET /users**: Retrieve all users.
- **GET /users/new**: Display a form to add a new user.
- **POST /users**: Create a new user.
- **GET /users/<id>**: Retrieve a user by ID.
- **POST /users/<id>**: Update an existing user.
- **DELETE /users/<id>**: Delete a user.




