# Threat Intelligence Dashboard

A live threat intelligence dashboard built with Python and Flask.
Created by Madibana Maria — BCIS Student, University of the Free State.

## What it does
- Checks IP addresses against the AbuseIPDB global threat database
- Assigns risk levels: Clean, Low Risk, Medium Risk, High Risk
- Displays results on a live web dashboard in real time
- Shows abuse score, country of origin, and total reports per IP

## Technologies used
- Python 3
- Flask (web framework)
- AbuseIPDB API (real threat intelligence database)
- HTML & CSS (dashboard interface)

## How to run it
1. Clone this repository
2. Install dependencies:
   pip install flask requests
3. Get a free API key from https://www.abuseipdb.com
4. Replace YOUR_API_KEY_HERE in app.py with your key
5. Run the app:
   python app.py
6. Open your browser and go to http://127.0.0.1:5000

## What I learned
- How threat intelligence works in real cybersecurity
- How to integrate real security APIs into a tool
- How to build a live web dashboard with Flask
- How SOC analysts assess and classify IP threats

## Author
Madibana Maria — BCIS Student, University of the Free State
Cybersecurity interest: Blue Team & Defensive Security# threat-intelligence-dashboard
A Python and Flask based live threat intelligence dashboard that checks IPs against a real global threat database
