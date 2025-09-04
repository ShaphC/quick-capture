from flask import Flask, render_template, request, redirect, url_for
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CONVERTKIT_API_URL = "https://api.convertkit.com/v3/forms/YOUR_FORM_ID/subscribe"
CONVERTKIT_API_KEY = os.getenv("CONVERTKIT_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form.get("email")
        if email:
            try:
                requests.post(
                    CONVERTKIT_API_URL,
                    data={"email": email, "api_key": CONVERTKIT_API_KEY},
                    timeout=5
                )
            except Exception as e:
                print(f"ConvertKit error: {e}")
            return redirect(url_for("confirmation"))
    return render_template("index.html")

@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")

if __name__ == "__main__":
    app.run(debug=True)
