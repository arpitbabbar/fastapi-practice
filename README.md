# 🏏 FastAPI CRUD - Players API

This is a beginner-friendly FastAPI project that implements full CRUD operations using an **in-memory dictionary** as a temporary "database". The API manages cricket players with details such as name, country, and IPL team.

> ⚡️ Built as part of FastAPI learning and practice.

---

## 🔧 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Pydantic** (for data validation)
- In-memory `dict` for data storage

---

## 📦 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/fastapi-practice.git
   cd fastapi-practice
   ```

2. **Create a virtual environment and activate it (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn
   ```

4. **Run the app:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Explore the API using Swagger UI:**
   Open your browser and go to [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📌 Features & Routes

### ✅ Basic Routes

| Method | Endpoint                | Description                  |
|--------|-------------------------|------------------------------|
| GET    | `/`                     | Hello World route            |
| GET    | `/get-all-players`      | List all players             |
| GET    | `/get-player/{id}`      | Get player by ID (Path Var)  |
| GET    | `/get-player?name=...`  | Get player by name (Query)   |
| POST   | `/add-player`           | Add a new player             |
| PUT    | `/update-player/{id}`   | Update existing player       |
| DELETE | `/delete-player/{id}`   | Delete a player              |

---

## 📂 Example Data

```json
{
  "name": "Virat",
  "country": "India",
  "ipl_team": "RCB"
}
```

---

## 🧠 Learnings & Concepts Practiced

- FastAPI routing with `@app.get`, `@app.post`, etc.
- Path parameters using `Path(...)`
- Query parameters with validation
- Pydantic models (`BaseModel`, optional fields)
- In-memory CRUD logic
- Basic error handling
- Swagger/OpenAPI integration out of the box

---

## ✨ To-Do / Extensions

- [ ] Add persistent DB (e.g., SQLite + SQLAlchemy)
- [ ] Add Dependency Injection
- [ ] Add JWT Authentication
- [ ] Add custom exception handlers
- [ ] Add unit tests with Pytest

---

## 🙌 Acknowledgements

Thanks to the [FastAPI](https://fastapi.tiangolo.com) docs and community for making it so beginner-friendly.

---

## 📌 Author

Created by [Arpit Babbar](https://github.com/arpitbabbar) ✌️
