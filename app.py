# Threat Intelligence Dashboard
# Created by: Madibana Maria

import socket
import requests
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = "YOUR_API_KEY_HERE"

def check_ip(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Accept": "application/json", "Key": API_KEY}
    params = {"ipAddress": ip, "maxAgeInDays": 90}
    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()["data"]
        return {
            "ip": ip,
            "score": data["abuseConfidenceScore"],
            "country": data["countryCode"],
            "reports": data["totalReports"],
            "risk": assess_risk(data["abuseConfidenceScore"])
        }
    except:
        return {"ip": ip, "score": 0, "country": "N/A", "reports": 0, "risk": "UNKNOWN"}

def assess_risk(score):
    if score == 0:
        return "CLEAN"
    elif score < 25:
        return "LOW RISK"
    elif score < 75:
        return "MEDIUM RISK"
    else:
        return "HIGH RISK"

@app.route("/")
def dashboard():
    test_ips = [
        "8.8.8.8",
        "1.1.1.1",
        "192.168.1.2",
        "185.220.101.45",
        "45.33.32.156",
    ]

    results = [check_ip(ip) for ip in test_ips]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    clean = sum(1 for r in results if r["risk"] == "CLEAN")
    low = sum(1 for r in results if r["risk"] == "LOW RISK")
    high = sum(1 for r in results if r["risk"] in ["MEDIUM RISK", "HIGH RISK"])

    return render_template("index.html",
        results=results,
        timestamp=timestamp,
        total=len(results),
        clean=clean,
        low=low,
        high=high
    )

if __name__ == "__main__":
    app.run(debug=True)