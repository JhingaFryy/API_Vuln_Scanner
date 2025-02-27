# API Vulnerability Scanner

## 📌 Description
This script scans APIs for common security issues like **Broken Authentication, Rate Limiting Bypass, and Injection Vulnerabilities**.

## 🚀 Features
- **Authentication Bypass Testing**
- **Rate Limiting Detection**
- **Injection Payload Testing (SQLi, XSS, Path Traversal)**

## 🛠️ Installation
Ensure you have Python installed, then install the required dependency:
```bash
pip install requests
```

## 🔧 Usage
1. **Edit Target APIs**
   - Open `api_vuln_scanner.py` and update the `API_URLS` list with your target endpoints:
   ```python
   API_URLS = [
       "https://api.example.com/login",
       "https://api.example.com/user",
       "https://api.example.com/payment"
   ]
   ```

2. **Run the Scanner**
   ```bash
   python api_vuln_scanner.py
   ```

3. **Analyze Results**
   - ✅ `[!] Possible Auth Bypass on {URL}` → The API might be vulnerable to authentication bypass.
   - ✅ `[!] Possible Rate Limiting Bypass on {URL}` → The API is not enforcing rate limits.
   - ✅ `[!] Potential Injection Issue on {URL} with payload {payload}` → The API might be vulnerable to SQLi, XSS, or Path Traversal.

## 📜 Disclaimer
This tool is for educational and ethical testing purposes only. **Do not use it on unauthorized systems.**

## 👨‍💻 Author
**Jatin** - Bug Bounty Hunter | Cybersecurity Enthusiast 🚀


##Donate a Coffee:
Paypal: pardeshijatin1998@gmail.com
