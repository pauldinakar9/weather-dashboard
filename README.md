# 🌤 DevOps Weather Dashboard Project — Complete Learning Journey

## 📌 Project Goal

Build a complete cloud-hosted Flask weather dashboard and automate deployment using Terraform.

Final target:

```text
terraform apply
    ↓
EC2 created
    ↓
Security Group configured
    ↓
Python installed
    ↓
GitHub repo cloned
    ↓
Dependencies installed
    ↓
Flask app launched automatically
```

---

# 🧠 Technologies Used

* Python
* Flask
* OpenWeather API
* HTML/CSS/Bootstrap
* Git & GitHub
* AWS EC2
* Terraform
* Linux
* SSH
* cloud-init

---

# 🚀 Phase 1 — Local Flask App Development

## Step 1 — Create Project Folder

```bash
mkdir weatherapp
cd weatherapp
```

---

## Step 2 — Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3 — Install Packages

```bash
pip install flask requests python-dotenv
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

---

## Step 4 — Create Project Structure

```text
weatherapp/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
│
├── templates/
│   └── index.html
│
└── venv/
```

---

# 🌦 Weather Dashboard Features Built

## Initial Features

* Current weather
* Multiple cities
* Temperature
* Humidity
* Wind speed

---

## Advanced Features Added

### ✅ 3 Dynamic City Cards

Users could change all three cities.

### ✅ Local Time & Timezones

Used timezone offsets from OpenWeather API.

### ✅ Animated Gradient Background

Modern dashboard UI.

### ✅ Glassmorphism Cards

Professional modern frontend style.

### ✅ Dark/Light Mode Toggle

Frontend enhancement.

### ✅ Auto Refresh Dashboard

```html
<meta http-equiv="refresh" content="60">
```

### ✅ Real-Time Clock

Implemented using JavaScript.

### ✅ Dynamic Weather Colors

Cards changed color based on weather condition.

### ✅ 5-Day Forecast

Used OpenWeather Forecast API.

### ✅ Geolocation Button

Added browser location detection.

---

# ❌ Mistakes & Debugging During Flask Development

## Mistake 1 — Forgot Shell Permissions

Error:

```text
Permission denied
```

### Fix

```bash
chmod +x script.sh
```

---

## Mistake 2 — Wrong SSH Key Permissions

Error:

```text
WARNING: UNPROTECTED PRIVATE KEY FILE!
```

Cause:

```bash
chmod 777 key.pem
```

### Fix

```bash
chmod 400 key.pem
```

Important lesson:
SSH private keys must NOT be publicly readable.

---

## Mistake 3 — Flask KeyError

Error:

```python
KeyError: 'main'
```

Cause:

* Invalid API response
* Wrong city/API issue

### Fix

Added response validation.

---

## Mistake 4 — Python Indentation Errors

Error:

```python
IndentationError: expected an indented block
```

Cause:

* Improper indentation inside loops.

### Fix

Rewrote Python structure carefully.

Lesson:
Python is indentation-sensitive.

---

## Mistake 5 — Overloading App with IPL API

Problem:
Dashboard became cluttered.

### Decision

Removed IPL integration.

Lesson:
Focused apps are better than overloaded dashboards.

---

# 📦 Phase 2 — Git & GitHub Workflow

## Initialize Git

```bash
git init
```

---

## Add Files

```bash
git add .
```

---

## Commit

```bash
git commit -m "Initial weather dashboard project"
```

---

## Push to GitHub

```bash
git remote add origin <repo_url>
git push -u origin main
```

---

# 📄 README Creation

Created a professional README including:

* Installation steps
* Project structure
* Features
* Technologies used
* Future improvements

Lesson:
README is essential for professional GitHub projects.

---

# ☁️ Phase 3 — Manual EC2 Deployment

## Step 1 — Create EC2

Used AWS EC2 manually.

---

## Step 2 — SSH Into EC2

```bash
ssh -i key.pem ubuntu@PUBLIC_IP
```

---

## Step 3 — Install Python

```bash
sudo apt update
sudo apt install python3-pip python3-venv -y
```

---

## Step 4 — Clone Repo

```bash
git clone <repo_url>
```

---

## Step 5 — Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 6 — Install Requirements

```bash
pip install -r requirements.txt
```

---

## Step 7 — Configure Environment Variables

Created `.env`

```env
API_KEY=xxxxx
```

---

## Step 8 — Run Flask App

```bash
python app.py
```

Opened:

```text
http://PUBLIC_IP:5000
```

App became live.

---

# ❌ Manual Deployment Debugging

## Mistake — Security Group Missing Port 5000

Problem:
App inaccessible.

### Fix

Added inbound rule:

| Port | Type       |
| ---- | ---------- |
| 5000 | Custom TCP |

---

## Mistake — Flask Bound to localhost

Problem:
App not accessible externally.

### Fix

```python
app.run(host="0.0.0.0", port=5000)
```

Lesson:
Cloud apps must bind to all interfaces.

---

# 🔥 Major DevOps Learning

## Servers Are Disposable

Terminating EC2 deletes:

* server
* app
* public IP

Lesson:
Infrastructure should be reproducible.

This led into Terraform learning.

---

# 🏗 Phase 4 — Terraform Automation

## Goal

Automate:

* EC2 creation
* Security Groups
* App deployment
* Python installation
* GitHub clone
* Flask launch

---

# Terraform Files Created

```text
weather-terraform/
│
├── main.tf
├── outputs.tf
```

---

# Terraform Resources Used

## Provider

```hcl
provider "aws" {
  region = "us-east-1"
}
```

---

## Security Group

Opened:

* SSH (22)
* Flask (5000)

---

## EC2 Instance

Created using:

```hcl
resource "aws_instance" "weather_server"
```

---

# ⚡ user_data Automation

Terraform automatically:

```bash
apt update
install python
install pip
install git
clone repo
create venv
install requirements
run Flask app
```

This was the core DevOps automation milestone.

---

# ❌ Terraform & Infrastructure Debugging

## Problem 1 — SSH Permission Denied

Error:

```text
Permission denied (publickey)
```

### Root Cause

Wrong/mismatched SSH keys.

### Fix

Created new clean AWS keypair:

```text
weather_key
```

Updated Terraform:

```hcl
key_name = "weather_key"
```

---

## Problem 2 — Wrong AMI

Used:

```text
ami-0c02fb55956c7d316
```

This was Amazon Linux.

But Terraform script used:

```bash
apt install
```

which belongs to Ubuntu.

### Result

Provisioning failed.

---

## Problem 3 — Wrong SSH Username

Tried:

```bash
ubuntu@
```

But Amazon Linux requires:

```bash
ec2-user@
```

Lesson:
Different AMIs use different default users.

---

## Problem 4 — cloud-init Failure

Debugged using:

```bash
sudo cat /var/log/cloud-init-output.log
```

Critical DevOps lesson:
Always inspect provisioning logs.

---

## Problem 5 — Private GitHub Repo

Error:

```text
fatal: could not read Username for 'https://github.com'
```

Cause:
Terraform EC2 could not clone private repo.

### Fix

Made GitHub repo public.

Lesson:
Non-interactive automation cannot answer GitHub auth prompts.

---

## Problem 6 — Terraform State Issues

Learned about:

* stale state
* infra recreation
* immutable infrastructure

Used:

```bash
terraform destroy
terraform apply
```

multiple times.

---

# ✅ Final Successful Architecture

```text
Local Machine
    ↓
Terraform Apply
    ↓
AWS EC2 Created
    ↓
Security Groups Created
    ↓
user_data Executes
    ↓
Repo Cloned from GitHub
    ↓
Python Environment Created
    ↓
Flask App Installed
    ↓
Weather Dashboard Live
```

---

# 🎯 Final Outcome

Successfully achieved:

✅ Flask development
✅ API integration
✅ Linux administration
✅ GitHub workflow
✅ EC2 deployment
✅ Terraform automation
✅ SSH troubleshooting
✅ cloud-init debugging
✅ Infrastructure as Code

---

# 🧠 Biggest DevOps Lessons Learned

## 1. Infrastructure Should Be Reproducible

Terraform allows:

```bash
terraform apply
terraform destroy
```

Servers become disposable.

---

## 2. Provisioning Is Fragile

Small issues break automation:

* wrong AMI
* wrong username
* wrong package manager
* wrong keys
* private repos

---

## 3. Logs Are Critical

Most important debugging tools:

```bash
/var/log/cloud-init-output.log
output.log
ps aux
ss -tulpn
```

---

## 4. Cloud Automation Requires Careful Alignment

Everything must align:

* AMI
* package manager
* SSH username
* keypair
* GitHub repo
* ports
* Flask binding

---

# 🚀 Suggested Next Learning Steps

## 1. Gunicorn

Replace Flask development server.

---

## 2. Nginx

Reverse proxy setup.

---

## 3. Docker

Containerize app.

---

## 4. CI/CD

GitHub Actions automation.

---

## 5. Terraform Modules

Professional infrastructure structure.

---

## 6. AWS Secrets Manager

Secure API key handling.

---

# 🏁 Final Achievement

This project evolved from:

```text
simple Flask weather app
```

into:

```text
fully automated Infrastructure-as-Code deployment project
```

This is genuine beginner-to-intermediate DevOps learning experience.
