import requests

# Replace this URL with your classmate's Render API endpoint
url = "https://paca-oncis-jero.onrender.com/jero?name=jero"

try:
    response = requests.get(url, timeout=30)

    # Check the HTTP status code
    if response.status_code == 200:
        data = response.json()

        print("\n===== CLASSMATE'S API RESPONSE =====")

        # Display meaningful JSON data
        for key, value in data.items():
            print(f"{key.replace('_', ' ').title()}: {value}")

    else:
        print("Request failed.")
        print("Status Code:", response.status_code)

except requests.exceptions.RequestException as error:
    print("Could not connect to the API.")
    print("Error:", error)
