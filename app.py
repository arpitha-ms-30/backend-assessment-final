from flask import Flask, jsonify, request
import threading
import time

app = Flask(__name__)

projects = []
workspaces = []
jobs = []
events = []

@app.route("/")
def home():
    return "Backend server is running successfully!"

@app.route("/api/health")
def health_check():
    return jsonify({"status": "ok"})

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    if data.get("username") == "admin" and data.get("password") == "admin123":
        return jsonify({"message": "Login successful", "role": "Owner"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# Project APIs
@app.route("/api/projects", methods=["POST"])
def create_project():
    project = {"id": len(projects) + 1, "name": request.get_json().get("name")}
    projects.append(project)
    return jsonify(project), 201

@app.route("/api/projects", methods=["GET"])
def get_projects():
    return jsonify(projects), 200

# Workspace APIs
@app.route("/api/workspaces", methods=["POST"])
def create_workspace():
    data = request.get_json()
    workspace = {
        "id": len(workspaces) + 1,
        "project_id": data.get("project_id"),
        "name": data.get("name")
    }
    workspaces.append(workspace)
    return jsonify(workspace), 201

@app.route("/api/workspaces", methods=["GET"])
def get_workspaces():
    return jsonify(workspaces), 200

# Job APIs
def run_job(job_id):
    time.sleep(5)
    for job in jobs:
        if job["id"] == job_id:
            job["status"] = "completed"
            job["result"] = "Job executed successfully"

@app.route("/api/jobs", methods=["POST"])
def create_job():
    job = {"id": len(jobs) + 1, "status": "running", "result": None}
    jobs.append(job)
    threading.Thread(target=run_job, args=(job["id"],)).start()
    return jsonify(job), 202

@app.route("/api/jobs", methods=["GET"])
def get_jobs():
    return jsonify(jobs), 200

# -------- Real-Time Event Simulation --------

@app.route("/api/events", methods=["POST"])
def create_event():
    event = {
        "id": len(events) + 1,
        "type": request.get_json().get("type"),
        "message": request.get_json().get("message")
    }
    events.append(event)
    return jsonify(event), 201

@app.route("/api/events", methods=["GET"])
def get_events():
    return jsonify(events), 200

if __name__ == "__main__":
    app.run(debug=True)
