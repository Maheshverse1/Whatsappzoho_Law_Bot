# zoho_auth.py

import requests
import webbrowser

# ==== Replace with your actual values ====
CLIENT_ID = "clientID"
CLIENT_SECRET = "secret"
REDIRECT_URI = "URL"  # This must match Zoho API Console
SCOPE = "scope"
REGION = "in"  # use 'in' for India, 'com' for US, etc.

# Step 1: Generate authorization URL
auth_url = (
    f"https://accounts.zoho.{REGION}/oauth/v2/auth?"
    f"scope={SCOPE}&"
    f"client_id={CLIENT_ID}&"
    f"response_type=code&"
    f"access_type=offline&"
    f"redirect_uri={REDIRECT_URI}"
)

print(f"\n🔗 Visit this URL in your browser to authorize:\n{auth_url}\n")
webbrowser.open(auth_url)

# Step 2: Paste the code from the URL you were redirected to
auth_code = input("📥 Paste the 'code' from the redirected URL: ").strip()

# Step 3: Exchange code for tokens
token_url = f"https://accounts.zoho.{REGION}/oauth/v2/token"
data = {
    "code": auth_code,
    "redirect_uri": REDIRECT_URI,
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "grant_type": "authorization_code",
}

response = requests.post(token_url, data=data)

print("\n🔐 Token Response:", response.status_code)
print(response.json())
