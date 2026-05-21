import requests

response = requests.post(
  "http://localhost:5002/validate",
  json={
      "request_type": "input_validation",
      "input_data": "normal user input"
    }
)

print("Test program sent request to Input Validation Microservice.")
print("Test program received response from Input Validation Microservice:")
print(response.json())
