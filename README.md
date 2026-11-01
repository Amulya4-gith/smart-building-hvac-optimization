# Smart Building HVAC Optimization Platform

A beginner-friendly Flask web application for the Git & Docker technical assignment. It demonstrates a dashboard for indoor temperature, humidity, air-quality indicator, occupancy, energy consumption, rule-based alerts, and basic HVAC mode/setpoint controls.

> **Important:** Sensor values are simulated. The control form changes demo application state only and does not connect to real building equipment.

## Features
- Responsive dashboard for environmental and energy indicators
- Simulated sensor readings refreshed when the dashboard loads
- Rule-based alerts for high temperature, humidity, air-quality indicator, and empty occupancy
- HVAC mode selector (`Auto`, `On`, `Off`) and target temperature validation
- Health endpoint at `/health`
- Dockerfile and Docker Compose configuration

## Project structure
```text
smart-building-hvac-optimization/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Run locally (optional)
Requires Python 3.12 or a compatible version.
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open `http://localhost:5000`.

## Run using Docker (recommended)
Install and start Docker Desktop first. From the project folder:
```bash
docker compose up --build -d
docker compose ps
```
Open `http://localhost:5000`. Test the health endpoint at `http://localhost:5000/health`.
Stop the app with:
```bash
docker compose down
```

## Git and GitHub workflow
Replace `YOUR-USERNAME` with your GitHub username.
```bash
git init
git branch -M main
git add .
git commit -m "chore: initialize HVAC optimization project"
git branch development
git switch development
git switch -c feature/dashboard
git add app.py templates/index.html static/style.css
git commit -m "feat: add HVAC monitoring dashboard"
git switch development
git merge feature/dashboard
git add Dockerfile docker-compose.yml requirements.txt .dockerignore
git commit -m "build: containerize application with Docker"
git switch main
git merge development
git remote add origin https://github.com/YOUR-USERNAME/smart-building-hvac-optimization.git
git push -u origin main
git push -u origin development
```

### Useful Git commands
```bash
git status
git log --oneline --graph --all
git branch
git switch development
git pull origin main
git push origin development
```

For a meaningful conflict-resolution demonstration, create a temporary branch and edit the same README line in two branches, then merge and resolve the conflict manually. Do not create a conflict just to claim one occurred; document the steps and screenshot the actual result if you perform this demonstration.

## Assignment mapping
1. **Problem analysis:** dashboard tracks indoor conditions, occupancy and energy and offers basic control settings.
2. **Project structure:** Flask app, HTML templates, CSS assets, dependency list and container configuration.
3. **Git initialization:** `.git` is created by `git init`; `.gitignore` excludes generated files and secrets.
4. **Branching:** `main` contains stable work, `development` integrates work, and `feature/dashboard` isolates dashboard development.
5. **Workflow:** use staged changes, meaningful commits, merges and remote synchronization.
6. **Commit history:** run `git log --oneline --graph --all` and include a screenshot.
7. **Docker design:** one web service is containerized; Compose publishes port 5000.
8. **Dockerfile:** uses a Python base image, installs dependencies, copies source and starts Gunicorn.
9. **Docker Compose:** defines the web service, port mapping, timezone environment variable and restart policy. No database or persistent volume is required for this demo.
10. **Testing:** check the dashboard and `/health`, change the HVAC mode/setpoint, and verify invalid setpoints are rejected.
11. **Benefits:** reproducible setup, version history, easier collaboration and portable deployment.
12. **Challenges and improvements:** demo readings are random and state is in memory. Future work could integrate real sensors, persistent storage, authentication, role-based access, automated tests and secure control interfaces.

## Screenshots to capture for your report
1. GitHub repository page showing project files.
2. Terminal showing `git log --oneline --graph --all`.
3. Git branches (`git branch -a`) and merge output.
4. `docker compose up --build -d` completing successfully.
5. `docker compose ps` showing the running service.
6. Browser showing the dashboard at `http://localhost:5000`.
7. Browser showing `http://localhost:5000/health`.
8. HVAC control form after applying a setting.

## Safety and scope
This is an educational prototype only. Do not connect it to real HVAC hardware without proper building-management integration, authorization, fail-safe controls and security review.
