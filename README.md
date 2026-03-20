# 🚀 DeployFlow – CI/CD Pipeline on AWS

A production-grade CI/CD pipeline built using **GitHub Actions, Docker, and AWS EC2** with a modern deployment dashboard UI.

---

## 🔥 Live Demo

👉 http://3.85.104.7:8000

---

## ⚙️ Tech Stack

- ⚡ FastAPI (Backend)
- 🐳 Docker (Containerization)
- ☁️ AWS EC2 (Deployment)
- 🔁 GitHub Actions (CI/CD)
- 🎨 HTML/CSS (Modern UI Dashboard)

---

## 🧠 Architecture
Developer Push Code
↓
GitHub Actions (CI/CD)
↓
Build Docker Image
↓
Push to Docker Hub
↓
Deploy to AWS EC2
↓
Live Application 🚀

---

## 📸 Screenshots

### 🔥 UI Dashboard
![UI](<img width="1392" height="922" alt="Screenshot 2026-03-20 140037" src="https://github.com/user-attachments/assets/3aa9cac0-b92a-4b0e-b4b4-cf966f24fd4d" />
)

---

### ⚙️ CI/CD Pipeline (GitHub Actions)
![Pipeline](<img width="937" height="346" alt="Screenshot 2026-03-20 134929" src="https://github.com/user-attachments/assets/113ffa90-32b4-4f0f-999a-edb86695f759" />
)

---

### 🐳 Docker Running on EC2
![Docker](<img width="1797" height="71" alt="Screenshot 2026-03-20 135506" src="https://github.com/user-attachments/assets/5541b3a6-8bc2-4fd9-9d76-930715d1933c" />
)

---

### ☁️ AWS EC2 Instance
![EC2](<img width="1894" height="231" alt="Screenshot 2026-03-20 135618" src="https://github.com/user-attachments/assets/fb0cad17-e99a-4c8a-b107-d2abaa0e60ac" />
)

---

## 🚀 Features

- ✅ Automated CI/CD pipeline
- ✅ Dockerized application deployment
- ✅ AWS EC2 hosting
- ✅ Zero manual deployment
- ✅ Modern UI dashboard
- ✅ Auto build → test → deploy

---

## ▶️ Run Locally

```bash
git clone https://github.com/vaibhav343343/deployflow-aws-ci-cd-pipeline.git
cd deployflow-aws-ci-cd-pipeline

docker build -t deployflow .
docker run -p 8000:8000 deployflow
