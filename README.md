Support Triage API

A FastAPI-based support ticket triage system that analyzes incoming support requests, predicts category and priority, finds similar historical tickets, recommends relevant knowledge base articles, and generates reasoning using Groq LLM.

The project combines traditional similarity search (TF-IDF + Cosine Similarity) with an LLM to provide explainable ticket analysis.

Features
Ticket classification using historical ticket data
Priority prediction
Critical issue detection using keyword rules
Similar ticket retrieval
Knowledge base article recommendation
AI-generated reasoning and suggested resolution
MySQL database integration
REST APIs with FastAPI
Docker and Docker Compose support
Automated tests using PyTest
Tech Stack
Python 3.11
FastAPI
SQLAlchemy
MySQL
Pandas
Scikit-Learn
LangChain
Groq LLM
Docker
PyTest

Project Structure
support-triage-api/
│
├── app/
│   ├── core/
│   ├── models/
│   ├── repositories/
│   ├── routes/
│   ├── schemas/
│   └── services/
│
├── data/
│   ├── historical_tickets.csv
│   └── kb_articles.csv
│
├── tests/
│
├── create_tables.py
├── seed_data.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
Environment Variables

Create a .env file in the project root.

GROQ_API_KEY=api_key
GROQ_MODEL=llama-3.3-70b-versatile

DB_HOST=db
DB_PORT=3306
DB_USER=root
DB_PASSWORD=password
DB_NAME=support_triage
Running Locally

1. Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate

2. Install Dependencies
pip install -r requirements.txt

3. Create Database Tables
python create_tables.py

Expected output:

Tables Created Successfully

4. Seed Initial Data
python seed_data.py

Expected output:

Loaded X KB Articles
Loaded X Historical Tickets
Database Seeding Complete
5. Start FastAPI
uvicorn app.main:app --reload

Application:

http://localhost:8000

Swagger UI:

http://localhost:8000/docs

ReDoc:

http://localhost:8000/redoc
Running with Docker
Build and Start Containers
docker compose up --build

This starts:

MySQL Database
FastAPI Application
Test Container
Verify Application

Open:

http://localhost:8000/docs
Stop Containers
docker compose down
Remove Containers and Volumes
docker compose down -v
Running Tests

Using local environment:

pytest -v

Using Docker:

docker compose run --rm test

Expected:

6 passed
API Endpoints
Health Check
GET /health

Returns application and database status.

Analyze Ticket
POST /tickets/analyze

Example Request:

{
  "title": "Cannot access admin page",
  "description": "Permission denied while opening settings",
  "channel": "Email",
  "requester_type": "Customer"
}
Analysis History
GET /tickets/history

Returns previously analyzed tickets.

Knowledge Base Search
GET /kb/search?query=vpn

Searches KB articles by title.

Analytics Summary
GET /analytics/summary

Returns:

Total requests
Category distribution
Priority distribution
Recent requests
Model Status
GET /model/status

Checks whether the configured Groq model is available.

How Ticket Analysis Works
User submits a ticket.
Ticket text is cleaned and normalized.
TF-IDF vectors are generated.
Cosine similarity is calculated against historical tickets.
Best matching ticket determines category and priority.
Priority is adjusted if critical keywords are detected.
Relevant KB articles are recommended.
Groq LLM generates reasoning and a suggested resolution.
Result is stored in the database.
Docker Changes Made

The project uses a multi-stage Docker build.

Base Stage

Installs Python dependencies and copies source code.

Test Stage

Runs:

pytest -v
Runtime Stage

Runs:

uvicorn app.main:app --host 0.0.0.0 --port 8000

Docker Compose was configured with three services:

db

MySQL 8.0 database with persistent volume.

api

FastAPI application built from the runtime stage.

test

PyTest container built from the test stage.

This setup allows application testing and deployment using the same Dockerfile.

Future Improvements
Replace CSV similarity source with database queries
Add JWT authentication
Add role-based access control
Store vector embeddings in a vector database
Add CI/CD pipeline
Deploy using Kubernetes
Improve ticket classification using fine-tuned models