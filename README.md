# ⚡ FastAPI Backend Project

## 📌 Description
This project is a backend REST API developed using FastAPI, focused on learning and applying backend development concepts with Python.

The API provides endpoints for handling requests, processing data, and returning structured responses, following modern backend practices.

---

## 🚀 Technologies

- Python  
- FastAPI  
- Uvicorn  
- Pydantic  
- REST API  

---

## ⚙️ Features

- Creation of REST endpoints  
- Request and response handling  
- Data validation using Pydantic  
- Automatic interactive API documentation (Swagger UI)  
- Structured backend architecture  

---

## 📂 Project Structure

    fast_api_python_back_end/
    ├── main.py
    ├── requirements.txt
    └── app/
        ├── routes/
        ├── models/
        └── services/

---

## ▶️ How to Run

### 1. Clone the repository
git clone https://github.com/NatanMaia-ops/fast_api_python_back_end.git  
cd fast_api_python_back_end  

### 2. Create virtual environment
python -m venv venv  

Linux/Mac:
source venv/bin/activate  

Windows:
venv\Scripts\activate  

### 3. Install dependencies
pip install -r requirements.txt  

### 4. Run the server
uvicorn main:app --reload  

---

## 🌐 API Access

After running, access:

- API: http://127.0.0.1:8000  
- Swagger Docs: http://127.0.0.1:8000/docs  
- ReDoc Docs: http://127.0.0.1:8000/redoc  

---

## 📡 Example Endpoints

- GET / → Root endpoint  
- GET /items/{id} → Get item by ID  
- POST /items → Create new item  

---

## 📊 Learning Goals

This project was created to:

- Practice backend development with Python  
- Understand REST API concepts  
- Learn FastAPI structure and best practices  
- Work with request validation and routing  

---

## 📫 Contact

- LinkedIn: https://www.linkedin.com/in/natan-alencar-573702352/
