# Backend Developer Assessment – PurpleMerit
## Overview

This project is a backend service developed as part of the Backend Developer Assessment for PurpleMerit.

The objective of this project is to demonstrate backend fundamentals such as API design, authentication concepts, project and workspace management, background job processing, and collaboration event handling.

## Tech Stack

- Python 3.11
- Flask (Backend Framework)
- In-memory data structures (for simplicity)
- Threading (for background job simulation)

## Features Implemented

### Authentication
- Simple login API with role response
- Demonstrates authentication and authorization concept

### Project Management
- Create projects
- List all projects

### Workspace Management
- Create workspaces under projects
- List workspaces

### Background Job Processing
- Submit background jobs
- Asynchronous execution using threads
- Job status and result tracking

### Collaboration Event Handling
- Create collaboration events (e.g., user join)
- List collaboration events
- Simulated real-time behavior via APIs

### Project Structure
backend-assessment
│
├── app                 # Flask application (main backend logic)
├── README.md           # Project documentation
├── .gitignore          # Ignored files and folders
└── venv/               # Virtual environment (local, not pushed to GitHub)

## API Endpoints

### Authentication
- POST `/api/login`

### Projects
- POST `/api/projects`
- GET `/api/projects`

### Workspaces
- POST `/api/workspaces`
- GET `/api/workspaces`

### Background Jobs
- POST `/api/jobs`
- GET `/api/jobs`

### Collaboration Events
- POST `/api/events`
- GET `/api/events`

## Setup and Run Instructions

### Prerequisites
- Python 3.11 installed
- Git installed

### Steps to Run the Project

```bash
git clone <repository-url>
cd backend-assessment
python -m venv venv
venv\Scripts\activate
pip install flask
python app.py```

Server will start at:
http://127.0.0.1:5000

## Design Notes and Trade-offs

- The application is implemented using in-memory data structures to keep the solution simple and focused on core backend concepts.
- Authentication is implemented as a basic login flow to demonstrate the authorization concept; JWT-based authentication can be added as a future enhancement.
- Background job processing is simulated using Python threading to showcase asynchronous execution and job lifecycle handling.
- Real-time collaboration is represented through event APIs instead of WebSockets to keep the implementation lightweight.
- The design prioritizes clarity, correctness, and extensibility over advanced infrastructure setup due to time constraints.

## Future Improvements

- Implement JWT-based authentication and role-based access control
- Integrate a relational or NoSQL database for persistent storage
- Add Redis or a message queue for scalable background job processing
- Implement WebSocket-based real-time collaboration
- Containerize the application using Docker
- Add automated tests and CI/CD pipeline




