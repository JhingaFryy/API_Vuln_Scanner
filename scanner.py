# API Vulnerability Scanner
# Description: This script scans APIs for common security issues like Broken Authentication, Rate Limiting Bypass, and Sensitive Data Exposure.

import requests
import time
import json

# Define API endpoints to test
API_URLS = [
    "https://example.com/api/v1/login",
    "https://example.com/api/v1/user",
    "https://example.com/api/v1/payment"
]

# Headers for testing authentication bypass
HEADERS = {
    "User-Agent": "SecurityScanner/1.0",
    "Authorization": "Bearer invalid_token"
}

# Payloads for testing injections and security misconfigurations
PAYLOADS = [
    "' OR '1'='1",  # SQL Injection
    "../../../etc/passwd",  # Path Traversal
    "<script>alert('XSS')</script>",  # XSS
]

def test_authentication_bypass(url):
    """Test for authentication and authorization bypass."""
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        print(f"[!] Possible Auth Bypass on {url}")
    else:
        print(f"[-] Auth seems secured on {url}")

def test_rate_limiting(url):
    """Test for rate limiting by sending multiple requests."""
    for _ in range(10):
        response = requests.get(url)
        time.sleep(0.2)  # Adjust for rate limit detection
    
    if response.status_code == 200:
        print(f"[!] Possible Rate Limiting Bypass on {url}")
    else:
        print(f"[-] Rate limiting in place on {url}")

def test_payload_injection(url):
    """Test for common injection vulnerabilities."""
    for payload in PAYLOADS:
        response = requests.post(url, data={"input": payload}, headers=HEADERS)
        if "error" in response.text.lower() or response.status_code == 500:
            print(f"[!] Potential Injection Issue on {url} with payload {payload}")
        else:
            print(f"[-] No immediate vulnerability detected on {url}")

def main():
    print("Starting API Security Scan...")
    for url in API_URLS:
        test_authentication_bypass(url)
        test_rate_limiting(url)
        test_payload_injection(url)
    print("Scan Complete!")

if __name__ == "__main__":
    main()
