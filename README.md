# 🔐 OTP Verification System using Python

A secure and user-friendly OTP (One-Time Password) verification system built with Python and Tkinter.

The project generates a secure 6-digit OTP, stores only its hashed value, provides time-based expiration, limits verification attempts, and supports OTP regeneration.

> **Current version:** Demo Mode  
> The OTP is displayed inside the application for testing purposes. No email credentials are required.

---

## ✨ Features

- 🔢 Secure 6-digit OTP generation
- 🔐 SHA-256 hashing of OTP
- ⏱️ 10-minute OTP expiration
- 🚫 Maximum 3 verification attempts
- 🔄 OTP resend cooldown
- 📧 Email input validation
- 🖥️ Simple Tkinter graphical interface
- 🛡️ OTP is not stored as plain text internally
- 🧪 Demo mode for testing without email credentials

---

## 🛠️ Technologies Used

- Python
- Tkinter
- `secrets`
- `hashlib`
- `time`

---

## 📂 Project Structure

```text
OTP-Verification-System-using-Python/
│
├── app.py
├── OTP Verification System.ipynb
├── requirements.txt
├── .gitignore
└── README.md

⚙️ How It Works
1. Enter an email address.
2. Click Generate OTP.
3. A secure 6-digit OTP is generated.
4. The OTP is hashed using SHA-256.
5. The demo OTP is displayed in the application.
6. Enter the OTP in the verification field.
7. The system validates:
   - OTP correctness
   - OTP expiration
   - Maximum verification attempts
8. A successful verification message is displayed.
🔒 Security Features
Secure OTP Generation
The project uses Python's secrets module to generate unpredictable OTP values.
OTP Hashing
Instead of keeping the OTP as plain text for verification, its SHA-256 hash is stored internally.
OTP Expiration
Each OTP remains valid for 10 minutes.
Attempt Limiting
Users have a maximum of 3 verification attempts.
Resend Protection
A 30-second cooldown is applied before another OTP can be generated.
🧪 Demo Mode
The current version runs without an email service.
After clicking Generate OTP, the generated OTP appears inside the application:
Demo OTP: 123456

This makes the project easy to test without exposing email passwords or API credentials.
▶️ How to Run
1. Clone the repository
git clone https://github.com/TheVerma11/OTP-Verification-System-using-Python.git
cd OTP-Verification-System-using-Python

2. Run the application
py app.py

or:
python app.py

3. Test the OTP flow
- Enter an email address.
- Click Generate OTP.
- Copy the displayed Demo OTP.
- Enter it in the OTP field.
- Click Verify OTP.
📦 Requirements
The project uses Python's standard library and Tkinter.
No external packages are required for the current demo version.
Tkinter is included with standard Python installations on Windows.

🚀 Future Improvements
Possible future enhancements include:
- Real email OTP delivery
- Google SMTP / transactional email integration
- OTP delivery through SMS
- Passwordless authentication
- Database-based user management
- OTP attempt logging
- Improved UI/UX
- CAPTCHA integration
- Rate limiting
- Production-ready authentication backend
👨‍💻 Author
Rohit Verma
Computer Science Ph.D. Research Scholar
GitHub: TheVerma11
📄 License
This project is created for educational and portfolio purposes.
```