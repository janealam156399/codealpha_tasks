# 🔐 Secure Coding Review

This project demonstrates a basic code review for identifying and fixing security vulnerabilities in a login system.

---

## 🚨 Vulnerabilities Found

### 1. Hardcoded Credentials
The password was directly written in the code, making it insecure.

### 2. Plain Text Password
Password was stored and compared in plain text.

### 3. No Password Protection
Password input was visible on the screen.

---

## ✅ Fixes Implemented

### 1. Password Hashing
Used SHA-256 hashing to store and compare passwords securely.

### 2. Hidden Password Input
Used getpass module to hide password input.

### 3. Improved Security Practices
Avoided storing sensitive data directly in code.

---

## 🛠️ Technologies Used

- Python
- hashlib
- getpass
