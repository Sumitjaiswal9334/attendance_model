# 🤖 AttendAI

<h3 align="center">The Future of Smart Attendance.</h3>

<p align="center">
AI-Powered Smart Attendance System using Face Recognition & Voice Authentication
</p>

<p align="center">
<img src="assets/homepage.png" width="900"/>
</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python"/>

<img src="https://img.shields.io/badge/Streamlit-Latest-red?style=for-the-badge&logo=streamlit"/>

<img src="https://img.shields.io/badge/Supabase-PostgreSQL-3ECF8E?style=for-the-badge&logo=supabase"/>

<img src="https://img.shields.io/badge/OpenCV-ComputerVision-green?style=for-the-badge&logo=opencv"/>

<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>

</p>

---

# 📖 About AttendAI

**AttendAI** is an AI-powered Smart Attendance Management System designed for educational institutions.

Unlike traditional attendance systems, AttendAI leverages **Computer Vision** and **Voice Biometrics** to automate attendance while improving accuracy and eliminating proxy attendance.

The application provides a seamless experience for both **Students** and **Teachers** through facial recognition, optional voice authentication, subject enrollment, attendance analytics, and automated reporting.

---

# ✨ Key Highlights

✅ Face Recognition Authentication

✅ Voice Authentication

✅ Subject Enrollment

✅ Attendance Tracking

✅ AI-powered Attendance Recording

✅ Attendance Reports

✅ Enrollment Codes

✅ Supabase Cloud Database

✅ Secure Authentication

---

# 🚀 Features

## 👨‍🎓 Student Portal

- 🔐 Face Recognition Login
- 🎤 Optional Voice Authentication
- 📚 Subject Enrollment
- 📊 Attendance Dashboard
- 👤 Student Profile
- 📅 Attendance History
- 📈 Attendance Percentage

---

## 👨‍🏫 Teacher Portal

- 📋 Create Subjects
- 👥 Manage Students
- 📸 Face Attendance
- 🎤 Voice Attendance
- 📊 Attendance Reports
- 📤 Export Attendance
- 🔗 Enrollment Codes
- 📈 Course Analytics

---

# 🖥️ Screenshots

## 🏠 Homepage

> Add screenshot here

```md
assets/homepage.png
```

---

## 👨‍🎓 Student Dashboard

> Add screenshot here

```md
assets/student_dashboard.png
```

---

## 👨‍🏫 Teacher Dashboard

> Add screenshot here

```md
assets/teacher_dashboard.png
```

---

## 📸 Face Recognition

> Add screenshot here

```md
assets/face_recognition.png
```

---

## 🎤 Voice Authentication

> Add screenshot here

```md
assets/voice_authentication.png
```

---

# 🛠 Tech Stack

## Frontend

- Streamlit

---

## Backend

- Python

---

## Database

- Supabase
- PostgreSQL

---

## Machine Learning

- OpenCV
- face_recognition
- dlib
- scikit-learn
- Resemblyzer
- librosa
- webrtcvad

---

## Security

- bcrypt
- Environment Variables
- Streamlit Secrets

---

# 📂 Project Structure

```text
AttendAI/

│

├── app.py

├── requirements.txt

├── README.md

│

├── .streamlit/

│ └── secrets.toml

│

├── src/

│ ├── screens/

│ ├── components/

│ ├── pipelines/

│ ├── database/

│ └── ui/

│

└── assets/
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/AttendAI.git
```

```bash
cd AttendAI
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Create .env

```env
SUPABASE_URL=YOUR_SUPABASE_URL

SUPABASE_KEY=YOUR_SUPABASE_KEY
```

---

## Streamlit Secrets

Create

```
.streamlit/secrets.toml
```

```toml
supabase_url="YOUR_SUPABASE_URL"

supabase_key="YOUR_SUPABASE_KEY"
```

---

## Run

```bash
streamlit run app.py
```

Application will be available at

```
http://localhost:8501
```

---

# 🔐 Authentication

AttendAI supports secure multi-modal authentication for both students and teachers.

## 👨‍🎓 Student Authentication

- Face Recognition Login
- Optional Voice Authentication
- Secure Profile Verification

### Workflow

```
Capture Face
      │
      ▼
Face Detection
      │
      ▼
Face Encoding
      │
      ▼
Compare with Database
      │
      ▼
Authentication Success
```

---

## 👨‍🏫 Teacher Authentication

- Email Login
- Password Authentication (bcrypt)
- Optional Voice Authentication

---

# 🧠 AI Pipeline

## 📸 Face Recognition Pipeline

```
Webcam Image
      │
      ▼
Face Detection (dlib)
      │
      ▼
Face Alignment
      │
      ▼
128-D Face Encoding
      │
      ▼
SVM Classification
      │
      ▼
Recognized Student
      │
      ▼
Attendance Marked
```

### Technologies Used

- OpenCV
- dlib
- face_recognition
- scikit-learn

---

## 🎤 Voice Recognition Pipeline

```
Audio Recording
      │
      ▼
Voice Activity Detection
      │
      ▼
Feature Extraction
      │
      ▼
Speaker Embedding
      │
      ▼
Similarity Matching
      │
      ▼
Voice Verified
```

### Technologies Used

- Resemblyzer
- Librosa
- WebRTC VAD

---

# 🗄 Database

AttendAI uses **Supabase PostgreSQL** as the backend database.

## Main Tables

| Table | Purpose |
|--------|----------|
| users | Student & Teacher Accounts |
| subjects | Course Information |
| enrollments | Student Enrollment |
| attendance | Attendance Logs |
| enrollment_codes | Subject Join Codes |

---

# 🔄 Application Workflow

## 👨‍🏫 Teacher Workflow

```
Teacher Login
      │
      ▼
Create Subject
      │
      ▼
Generate Enrollment Code
      │
      ▼
Students Join Subject
      │
      ▼
Upload Face Dataset
      │
      ▼
Take Attendance
      │
      ▼
Generate Reports
```

---

## 👨‍🎓 Student Workflow

```
Face Login
      │
      ▼
Join Subject
      │
      ▼
View Dashboard
      │
      ▼
Attendance Recorded
      │
      ▼
Track Attendance
```

---

# 📊 Attendance System

AttendAI supports multiple attendance methods.

### Face Recognition

✔ High Accuracy

✔ Fast Detection

✔ Automatic Attendance

---

### Voice Authentication

✔ Speaker Verification

✔ Optional Multi-factor Authentication

✔ Secure Attendance

---

# 📈 Reports

Teachers can generate

- Daily Reports
- Weekly Reports
- Monthly Reports
- Subject-wise Reports
- Student-wise Reports

Reports can be exported for further analysis.

---

# 🔒 Security

AttendAI follows multiple security practices.

- bcrypt Password Hashing
- Secure Face Embeddings
- Voice Embedding Storage
- Environment Variables
- Streamlit Secrets
- Supabase Authentication
- PostgreSQL Cloud Database

---

# 🧪 AI Models Used

## Face Recognition

| Model | Purpose |
|--------|----------|
| dlib | Face Detection |
| face_recognition | Face Encoding |
| SVM | Face Classification |

---

## Voice Recognition

| Library | Purpose |
|----------|----------|
| Resemblyzer | Speaker Embeddings |
| Librosa | Audio Processing |
| WebRTC VAD | Voice Detection |

---

# 📦 Major Dependencies

- streamlit
- numpy
- pandas
- OpenCV
- dlib
- face_recognition
- scikit-learn
- librosa
- resemblyzer
- supabase
- bcrypt
- pillow
- segno

---

# 🌟 Why AttendAI?

Unlike traditional attendance systems, AttendAI combines **Artificial Intelligence**, **Computer Vision**, and **Voice Biometrics** to provide a secure, accurate, and intelligent attendance solution.

Key benefits:

- Faster Attendance Process
- Reduced Manual Work
- Improved Accuracy
- Secure Authentication
- Cloud-based Data Management
- Easy Subject Enrollment
- AI-driven Attendance System

---

# 🐛 Troubleshooting

## ❌ Webcam Not Detected

- Ensure webcam permissions are enabled.
- Close other applications using the camera.
- Update your webcam drivers.

---

## ❌ Face Not Recognized

- Add **3–5 clear face images** under good lighting.
- Avoid blurry or low-resolution images.
- Ensure your face is clearly visible.

---

## ❌ Voice Authentication Failed

- Record your voice in a quiet environment.
- Speak naturally and avoid background noise.
- Re-enroll your voice profile if necessary.

---

## ❌ Supabase Connection Error

Verify your configuration:

```env
SUPABASE_URL=YOUR_SUPABASE_URL
SUPABASE_KEY=YOUR_SUPABASE_KEY
```

Also verify:

```
.streamlit/secrets.toml
```

contains valid credentials.

---

## ❌ Torch Installation Error

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

---

## ❌ dlib Installation Error (Windows)

```bash
pip install dlib-bin
```

---

## ❌ Permission Denied (Windows)

```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

# 🚀 Future Enhancements

AttendAI is designed with scalability in mind. Future releases may include:

### 🤖 AI Features

- Proxy Attendance Detection
- Face Liveness Detection
- Student Risk Prediction
- Classroom Engagement Analysis
- Attendance Trend Prediction
- AI Attendance Assistant
- Automatic Attendance Reports
- Smart Notifications

---

### 📱 Platform Features

- Mobile Application
- QR Code Attendance
- NFC Attendance
- Offline Attendance Support
- Cloud Synchronization

---

### 📊 Analytics

- Teacher Dashboard
- Student Performance Dashboard
- Attendance Heatmaps
- Department Analytics
- Attendance Insights
- AI Recommendations

---

# 🎯 Future Vision

AttendAI aims to become an intelligent classroom platform by combining:

- Artificial Intelligence
- Computer Vision
- Voice Biometrics
- Cloud Computing
- Data Analytics

to transform traditional attendance systems into smart, automated solutions.

---

# 🤝 Contributing

Contributions are always welcome!

If you'd like to improve AttendAI:

1. Fork this repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project for educational and research purposes.

---

# 🌟 Support

If you found this project helpful,

please consider giving it a ⭐ on GitHub.

It motivates further development and improvements.

---

<p align="center">

## 🤖 AttendAI

### **The Future of Smart Attendance.**

Built with ❤️ by **Sumit Jaiswal**

</p>