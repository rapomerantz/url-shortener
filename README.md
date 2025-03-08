# FastAPI URL Shortener

This is a simple URL shortener service built with FastAPI and Redis.

## 🚀 Features
- Shortens URLs and stores them in Redis.
- Retrieves original URLs from short codes.
- Uses FastAPI for a lightweight and fast backend.
- Containerized with Docker for easy deployment.

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/url-shortener.git
cd url-shortener
```

### 2️⃣ Install Dependencies
#### Run Locally (without Docker)
```sh
pip install -r requirements.txt
```

#### Run with Docker
```sh
docker-compose up --build
```

---

## 🛠️ Running the Application
### Run Without Docker
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Run With Docker
```sh
docker-compose up
```

---

## 🔗 API Endpoints

### ➤ Shorten a URL
#### **POST** `/shorten`
**Request Body:**
```json
{
  "url": "https://example.com"
}
```
**Response:**
```json
{
  "original_url": "https://example.com",
  "short_url": "http://localhost:8000/abc123"
}
```

### ➤ Retrieve Original URL
#### **GET** `/{short_code}`
**Example:**
```sh
curl -X GET http://localhost:8000/abc123
```
**Response:**
```json
{
  "original_url": "https://example.com"
}
```

---

## 🐳 Docker Usage
### **Build & Run Containers**
```sh
docker-compose up --build
```

### **Stop Containers**
```sh
docker-compose down
```

---

## ⚙️ Environment Variables
| Variable       | Default Value | Description |
|---------------|--------------|-------------|
| `REDIS_HOST`  | `redis`      | Redis hostname |
| `REDIS_PORT`  | `6379`       | Redis port |

---

## 📜 License
This project is licensed under the MIT License.