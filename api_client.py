import requests

url = "https://flask-miranda-act4-1.onrender.com/campus"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\n===== CAMPUS INFORMATION =====")
    print("Campus:", data["campus"])
    print("Location:", data["location"])
    print("Status:", data["status"])
    print("Type:", data["type"])

else:
    print("Request failed.")
    print("Status Code:", response.status_code)
