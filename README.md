[![License](https://img.shields.io/badge/license-MIT-red.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12.4-blue.svg)](https://www.python.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-latest-green.svg)](https://www.mongodb.com/)
[![Docker](https://img.shields.io/badge/Docker-latest-lightblue.svg)](https://www.docker.com/)

## Record Processing Backend

This project is a FastAPI-based backend application for processing and managing records with MongoDB as the database. It includes functionalities for creating, updating, deleting, and fetching records.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)



## Prerequisites

Python 3.9 or higher - [Official documentation](https://www.python.org/downloads/)

Docker and Docker Compose - [Official documentation](https://docs.docker.com/get-docker/)

## Installation
### Clone the Repository
```bash
git clone https://github.com/ksjavali/record-processing-backend.git
```

## Navigate to the project directory

```bash
cd record_processing_backend
```


### Setup Virtual Environment

```bash
python -m venv env
```
```bash
source env/bin/activate  # On Windows, use env\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```
### Set up MongoDB
Ensure MongoDB is installed and running. Configure the MongoDB URI in .env file.
	
### Environment Variables
Create a .env file in the root directory of your project and add the following:

```bash
MONGODB_URI=<URL to your MongoDB cluster>
```
Example: 
```bash
MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.mbpzzqn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
```

### Running the Application
```bash
cd src
uvicorn main:app --reload
```
The application would run on http://localhost:8000

Visit http://localhost:8000/docs in your browser to access the API documentation (Swagger UI).

### To run the test files
Make sure the src directory is your current working directory before executing the tests.

```bash
pytest test_main.py
```
### Build the Docker containers

Navigate to the root folder.

```bash
docker-compose build
```

### Start the Docker containers in detached mode

```bash
docker-compose up -d
```
### To compress the repository
```bash
git archive --format=tar.gz --output=backend_app.tar.gz HEAD
```

### To uncompress the tar ball file
```bash
tar -xzvf backend_app.tar.gz  -C path/to/folder
```

## API Documentation
### API Endpoints

Here record_id refers to the record_identifier

**POST /**
- Creates a new record.

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "record_identifier": "id",
  "description": "your_description",
  "timestamp": "2024-07-13T16:47:26.418Z",
  "category": 0
}'
```

**GET /all/records**
- Returns all records from the MongoDB collection.
```bash
curl -X 'GET' \
  'http://localhost:8000/all/records' \
  -H 'accept: application/json'
  ```

**GET /category/{category_id}**
- Returns records filtered by `category_id`.
```bash
curl -X 'GET' \
  'http://localhost:8000/category/{category_id}' \
  -H 'accept: application/json'
```

**GET /record_identifier/{record_id}**
- Returns records filtered by `record_id`.
```bash
curl -X 'GET' \
  'http://localhost:8000/record_identifier/{record_id}' \
  -H 'accept: application/json'
```

**GET /description/{description}**
- Returns records filtered by `description`.
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/description/{description}' \
  -H 'accept: application/json'
```

**GET /timestamp/{timestamp}**
- Returns records filtered by `timestamp`.
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/timestamp/{timestamp}' \
  -H 'accept: application/json'
  ```


**PUT /{record_identifier}**
- Updates a record identified by `record_id`.
```bash
curl -X 'PUT' \
  'http://127.0.0.1:8000/12' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "record_identifier": "string",
  "description": "your_description",
  "timestamp": "2024-07-13T16:51:34.713Z",
  "category": 0
}'
```

**DELETE /delete/{record_id}**
- Deletes a record identified by `record_id`.

```bash
curl -X 'DELETE' \
  'http://127.0.0.1:8000/delete/{record_id}' \
  -H 'accept: application/json'
```

**DELETE /delete**
- Deletes multiple records based on IDs provided in the request body.
```bash
curl -X 'DELETE' \
  'http://127.0.0.1:8000/delete' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "ids": [
    "id1", "id2"
  ]
}'
```

## Contributing
Your contributions to the project are appreciated. You can submit issues and pull requests here.



