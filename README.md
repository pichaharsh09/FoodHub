# FoodHub — Full-Stack Food Ordering Application

FoodHub is a full-stack food ordering application built with React and FastAPI. It provides a React-based user interface and a modular backend API for managing restaurants, food items, users, and orders.

## Tech Stack

**Frontend**
- React
- Vite
- JavaScript
- CSS

**Backend**
- Python
- FastAPI
- SQLAlchemy ORM
- Pydantic
- PostgreSQL

**Tools**
- Git and GitHub
- Swagger UI / OpenAPI
- VS Code

## Features

### Backend
- REST API endpoints for restaurants, food items, users, and orders
- CRUD operations for supported resources
- SQLAlchemy models and database relationships
- Pydantic schemas for request and response validation
- Modular architecture separating routes, services, repositories, and models
- Automatic interactive API documentation through FastAPI

### Frontend
- React component-based architecture
- Reusable food and restaurant cards
- Category navigation
- Hero section and navigation bar
- API integration module

## Project Structure

```text
FoodHub/
├── backend/
│   └── app/
│       ├── database/
│       ├── models/
│       ├── repositories/
│       ├── routers/
│       ├── schemas/
│       ├── services/
│       ├── crud.py
│       ├── exceptions.py
│       ├── main.py
│       └── test_crud.py
├── frontend/
├── frontend-react/
│   └── src/
│       ├── assets/
│       ├── components/
│       ├── api.js
│       ├── App.jsx
│       ├── App.css
│       ├── index.css
│       └── main.jsx
└── README.md
```

## Backend Architecture

The backend follows a modular, layered structure:

- **Routers:** Define API endpoints and handle HTTP requests.
- **Services:** Contain application and business logic.
- **Repositories:** Handle database access for supported resources.
- **Models:** Define SQLAlchemy database models and relationships.
- **Schemas:** Define and validate API request and response data.
- **Database:** Contains database configuration and the shared SQLAlchemy base.

This separation makes the application easier to maintain, test, and extend.

## Getting Started

### Prerequisites

Install the following:

- Python
- Node.js and npm
- PostgreSQL
- Git

### 1. Clone the repository

```bash
git clone https://github.com/pichaharsh09/FoodHub.git
cd FoodHub
```

### 2. Set up the backend

```bash
cd backend
python -m venv venv
```

Activate the virtual environment.

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

Install the backend dependencies using the project's dependency file, if provided:

```bash
pip install -r requirements.txt
```

Configure the PostgreSQL connection using the database settings expected by the application. Keep credentials in environment variables or a local environment file, and never commit secrets to GitHub.

Start the development server:

```bash
uvicorn app.main:app --reload
```

### 3. Explore the API

Once the backend is running, open:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

These pages provide interactive API documentation for the registered endpoints.

### 4. Set up the frontend

Open a second terminal from the project root:

```bash
cd frontend-react
npm install
npm run dev
```

Open the local URL printed by Vite in the terminal.

Ensure the backend is running and that the frontend API configuration points to the correct backend URL.

> Note: Database configuration, dependency files, and environment variable names may differ by local setup. Follow the actual project configuration when running the application.

## API Resources

The backend includes routers for the following resources:

| Resource | Router |
|---|---|
| Restaurants | `restaurants.py` |
| Food items | `foods.py` |
| Users | `users.py` |
| Orders | `orders.py` |

For available routes, HTTP methods, request bodies, and response formats, see the interactive documentation at `/docs`.

## Learning Outcomes

This project demonstrates practical experience with:

- Building REST APIs using FastAPI
- Relational database modeling with SQLAlchemy
- Request and response validation with Pydantic
- Organizing a backend into maintainable modules
- Connecting a React frontend to a backend API
- Version control and collaborative development workflows using Git

## Future Improvements

- Expand automated API and integration test coverage
- Add authentication and authorization where needed
- Improve frontend loading, error, and empty states
- Add deployment configuration and continuous integration
- Improve application logging and production configuration

## Author

**Harsh Picha**

GitHub: [@pichaharsh09](https://github.com/pichaharsh09)

---

*FoodHub is a learning and portfolio project focused on full-stack application development.*
