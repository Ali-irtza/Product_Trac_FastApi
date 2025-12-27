FastAPI Product Management System (Telusko Integration)
This project is a Full-Stack application featuring a FastAPI backend integrated with a React frontend and a PostgreSQL database. I developed the backend logic and database integration while following the Telusko FastAPI curriculum.

🚀 Features
Full CRUD Functionality: Create, Read, Update, and Delete products seamlessly.

Relational Database: Persistent storage using PostgreSQL with SQLAlchemy ORM.

Secure Architecture: Implementation of Environment Variables (.env) to protect database credentials.

CORS Enabled: Configured middleware to allow secure communication with the React frontend.

Automatic API Docs: Interactive documentation via FastAPI's built-in Swagger UI.

🛠️ Tech Stack
Backend: Python, FastAPI, Uvicorn

Database: PostgreSQL, SQLAlchemy

Frontend: React (provided by Telusko)

Security: Python-dotenv, URL percent encoding for special characters

⚙️ Setup & Installation
1. Clone the repository
Bash

git clone <your-repository-link>
cd <your-project-folder>
2. Set up the Python Environment
Bash

# Create and activate virtual environment
python -m venv Project_FastApi
.\Project_FastApi\Scripts\activate

# Install dependencies
pip install -r requirements.txt
3. Database Configuration
Create a .env file in the root directory and add your PostgreSQL credentials:

Plaintext

DB_PASSWORD=your_actual_password
4. Run the Application
Bash

uvicorn main:app --reload
The server will start at http://127.0.0.1:8000. You can access the interactive API docs at http://127.0.0.1:8000/docs.
