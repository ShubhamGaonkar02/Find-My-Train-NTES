# 🚆 Find My Train - NTES

A web-based Indian Railway enquiry portal that provides train information, live train running status, PNR status, train schedules, and station-related information.

## 🌐 Live Website

🚆 **[Visit Find My Train - NTES](https://find-my-train-ntes.vercel.app/)**

## 📌 Project Overview

Find My Train - NTES is a railway enquiry web application developed using a Python FastAPI backend and a responsive HTML, CSS, and JavaScript frontend.

The application connects with Indian Railway enquiry services to provide real-time railway information through a simple and user-friendly interface.

## ✨ Features

- 🚆 Live Train Status
- 🎫 PNR Status
- 🚉 Trains Between Stations
- 📍 Live Station Information
- 🛤️ Train Route / Schedule
- 🔎 Train Search
- ⏱️ Train delay and running information
- 📱 Responsive design for desktop and mobile
- ⚡ FastAPI backend
- 🌐 Live deployment using Vercel

## 🛠️ Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript
- Tailwind CSS
- SVG Icons
- Google Fonts (Inter)

### Backend

- Python
- FastAPI
- Uvicorn
- REST API endpoints

### Python Libraries

- Requests
- PyCryptodome
- Pillow
- NTES Client

### Version Control

- Git
- GitHub

### Deployment

- Vercel

## 🔌 API Endpoints

The backend provides the following API endpoints:

| Endpoint | Description |
|---|---|
| `/api/search` | Search for trains |
| `/api/train_info` | Get train information |
| `/api/live_status` | Get live running status |
| `/api/schedule` | Get train schedule |
| `/api/station_live` | Get live station information |
| `/api/trains_between` | Find trains between two stations |
| `/api/pnr_status` | Check PNR status |

## 📂 Project Structure

```text
Find-My-Train-NTES/
│
├── api/
│   └── index.py
│
├── ntes/
│   ├── client.py
│   ├── crypto.py
│   ├── pnr.py
│   ├── exceptions.py
│   └── utils.py
│
├── static/
│   └── index.html
│
├── main.py
├── requirements.txt
├── vercel.json
├── README.md
└── .gitignore
