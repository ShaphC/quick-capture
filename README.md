# Quick-Capture

A simple Python/Flask landing page to capture emails.  
Includes a confirmation page and easy integration with ConvertKit (now called Kit).

## Features

- Landing page with email form
- Confirmation page after subscription
- Secure environment variable management
- Ready for deployment on Ubuntu server
- Connects to ConvertKit API

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export CONVERTKIT_API_KEY=your_api_key
python3 app.py
