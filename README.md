# URL Shortener Microservice

## Overview
This is a simple URL Shortener microservice built with **FastAPI** and **Redis**. The service allows users to shorten URLs and retrieve the original URLs using a unique short code.

## Features
- Shorten long URLs
- Retrieve original URLs using a short code
- Uses Redis for fast lookups
- Containerized using Docker for easy deployment

## Prerequisites
Ensure you have the following installed on your system:
- [Python 3.9+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure
```
url-shortener/
│── docker-compose.yml      # Defines Redis & FastAPI containers
│── Dockerfile              # Builds the FastAPI app
│── .gitignore              # Git ignore rules
│── app/
│   ├── main.py             # FastAPI application
│   ├── redis_client.py     # Redis connection
└── requirements.txt        # Python dependencies
```

## Setup and Running the Project

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

### 2. Set Up a Virtual Environment (Optional for Local Development)
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the Project with Docker Compose
```sh
docker-compose up --build
```
This will:
- Start a **Redis** container
- Build and start the **FastAPI** microservice

### 5. Verify Everything is Running
Check running containers:
```sh
docker ps
```
Expected output:
```
CONTAINER ID   IMAGE    COMMAND                  STATUS         PORTS
xxxxxxxxxxx   redis    "docker-entrypoint.s…"   Up 10 seconds  6379/tcp
xxxxxxxxxxx   fastapi  "uvicorn app.main:app"   Up 10 seconds  0.0.0.0:8000->8000/tcp
```

### 6. Test the API
Open your browser or use **cURL**:
```sh
curl -X GET "http://localhost:8000/"
```
Response:
```json
{"message": "Hello, FastAPI!"}
```

### 7. Stopping the Services
To stop the running containers:
```sh
docker-compose down
```


## License
This project is licensed under the MIT License.

