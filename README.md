# Task-Manager-API

A simple **Task Management API** built with **FastAPI** and **PostgreSQL**.  
This project was created to practice **real backend skills**: database integration, CRUD operations, and API design.

---

## 🛠 Tech Stack

- **Python 3.11+**
- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Relational database
- **SQLAlchemy** - ORM for database operations
- **Uvicorn** - ASGI server

---

## 📂 Project Structure

app/
├── main.py # Entry point
├── models.py # SQLAlchemy models
└── database/
├── init.py
└── db.py # Database connection
├── routes.py # API endpoints


---

## ⚡ Features

- **Task CRUD**
  - Create, read, update, delete tasks
- **Task Progress**
  - Track progress percentage
- **Timestamps**
  - Auto `created_at` and `updated_at`
- **Database-backed**
  - PostgreSQL as a real backend

---

## 🚀 Setup & Run

1. **Install dependencies**
```bash
pip install -r requirements.txt

CREATE DATABASE taskdb;

DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/taskdb"
