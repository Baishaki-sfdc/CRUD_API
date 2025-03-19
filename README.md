# User CRUD API with Flask, SQLite & SQLAlchemy

This project implements a RESTful API for managing users using Flask. 
The API supports basic CRUD operations (Create, Read, Update, Delete) with data stored in an SQLite database managed via SQLAlchemy.

## Features

- **Create a User**: Add a new user with `name`, `email`, and `age`.
- **Retrieve All Users**: Get a list of all registered users.
- **Retrieve a Single User**: Fetch a user by its unique ID.
- **Update a User**: Update user details based on its ID.
- **Delete a User**: Remove a user from the database by its ID.
- **Data Validation**: Validates required fields and data types including email format and age value.


## Setup and Installation

1. **Clone the repository:**
   
   git clone <repository-url>
   

Create and activate a virtual environment:   
python -m venv venv
### On Windows:
venv\Scripts\activate


## Install the required dependencies:
pip install -r requirements.txt


## Run the Flask Application:
python app.py

The server will start on http://127.0.0.1:5000/.

## API Endpoints
GET /
Returns API information and available endpoints.

GET /api/users
Retrieves a list of all users.

GET /api/users/<id>
Retrieves a single user by ID.

POST /api/users
Create a new user.
Request Body (JSON):


## Testing the API
Web Browser: For GET requests, simply navigate to the URL.

cURL:
### Example for creating a user in PowerShell (using curl.exe):
curl.exe -X POST http://127.0.0.1:5000/api/users -H "Content-Type: application/json" -d "{\"name\":\"John Doe\", \"email\":\"john@example.com\", \"age\":30}"
 



