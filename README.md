# NeuroCheck – Alzheimer’s Assessment Tool
A Python-based CLI application designed to perform a **preliminary cognitive assessment** inspired by the Boston Naming Test (BNT).
The system evaluates user speech responses, analyses cognitive patterns, and connects patients with relevant doctors.

---

## Features

### Patient Module

* Secure signup and data storage using MySQL
* Audio-based cognitive test (speech activity analysis)
* Score generation using signal processing
* Risk classification (Low / Moderate / High)
* Doctor recommendation based on location

---

### Doctor Module

* Doctor registration system
* View assigned patients
* Access patient test results and risk levels

---

### Audio Processing Engine

* Records real-time speech using PyAudio
* Converts audio to NumPy arrays
* Applies signal thresholding to detect speech activity
* Generates a normalised cognitive score

---

### Analysis System

* Interprets test scores into meaningful risk levels
* Provides user-friendly explanations
* Simulates early-stage cognitive screening

---

### Database Integration

* MySQL-based backend
* Structured relational schema:

  * `patient`
  * `doctor`
  * `result`
  * `recommendation`
* Automatic data seeding for initial setup

---

## Tech Stack

* **Language:** Python
* **Database:** MySQL
* **Libraries:**
  * NumPy
  * PyAudio
* **Architecture:** Modular CLI-based system

---

## Project Structure

```
NeuroCheck/
│
├── db/
│   └── database.py
│
├── modules/
│   ├── patient.py
│   ├── doctor.py
│   ├── test_engine.py
│   ├── analysis.py
│   └── seed_data.py
│
├── main.py
├── requirements.txt
├── schema.sql
├── .gitignore
└── README.md
```

---

## Setup Instructions

### 1️. Clone the Repository

```bash
git clone https://github.com/your-username/NeuroCheck.git
cd NeuroCheck
```

---

### 2️. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️. Setup MySQL Database

Run the following in MySQL:

```sql
CREATE DATABASE Project;
USE Project;
-- Run schema.sql file
SOURCE schema.sql;
```

---

### 5️. Run the Application

```bash
python main.py
```

---

## How It Works

1. User signs up as Patient or Doctor
2. Patient takes a speech-based test
3. Audio is processed to calculate the activity score
4. Score is analysed into a risk category
5. Patient can view results and get doctor recommendations
6. Doctors can view assigned patients and their data

---

## Author

**Dherya Jain**
