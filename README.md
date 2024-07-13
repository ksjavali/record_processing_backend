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
- [License](#license)


## Prerequisites

Python 3.9 or higher - [Official documentation](https://www.python.org/downloads/)

Docker and Docker Compose - [Official documentation](https://docs.docker.com/get-docker/)

## Installation

### Clone the Repository
```
git clone https://github.com/ksjavali/record-processing-backend.git
```

## Navigate to the project directory

```
cd record-processing-backend
```

### Setup Virtual Environment

```
python -m venv env
```
```
source env/bin/activate  # On Windows, use env\Scripts\activate
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Environment Variables

Create a .env file in the root directory of your project and add the following:

```
MONGODB_URI=<URL to your MongoDB cluster>
```
```
Example: 
MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.mbpzzqn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
```

## Build the Docker containers

```
docker-compose build
```

## Start the Docker containers in detached mode

```
docker-compose up -d
```
## License
[MIT](https://tldrlegal.com/license/mit-license)

