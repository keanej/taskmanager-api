# 🚀 TaskManager API (FastAPI)
# https://taskmanager-api-3-o4pc.onrender.com/docs#/

A simple but fully functional **REST API** built using **FastAPI**, **SQLAlchemy**, and **Pydantic**.  
This project demonstrates backend development skills essential for Python developer roles, including:

- API design & routing
- Data modeling (SQLAlchemy ORM)
- Database sessions & transactions
- Dependency injection
- Request/response validation with Pydantic
- Auto-generated API documentation (Swagger UI / OpenAPI)

The API supports:

- Managing **Users**
- Managing **Tasks**
- Linking Tasks to Users

---

## 🛠️ Tech Stack

| Component         | Technology              |
| ----------------- | ----------------------- |
| Backend Framework | FastAPI                 |
| Database          | SQLite (for simplicity) |
| ORM               | SQLAlchemy              |
| Data Validation   | Pydantic                |
| Web Server        | Uvicorn                 |
| Python Version    | 3.10                    |

---

## 📁 Project Structure

taskmanager-api/
│── app/
│ ├── main.py
│ ├── database/
│ │ ├── session.py
│ │ └── init.py
│ ├── models/
│ │ ├── user.py
│ │ ├── task.py
│ │ └── init.py
│ ├── schemas/
│ │ ├── user.py
│ │ ├── task.py
│ │ └── init.py
│ └── routers/
│ ├── users.py
│ ├── tasks.py
│ └── init.py
│
├── venv/
├── requirements.txt (optional)
└── README.md

---

---

## ▶️ Install & Run

### 1. Clone the project
