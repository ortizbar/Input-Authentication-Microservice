# Input-Authentication-Microservice

## Description
The Input Validation Microservice validates application input before processing.

## Communication Pipe
REST API using HTTP POST requests and JSON responses.

## How to Request Data

### Endpoint:

```
http://localhost:5002/validate
```

### Example Request:

```
json={
        "request_type": "input_validation",
        "input_data": "normal user input"
    }
```

### Example Python Request:

```
import requests
response = requests.post(
    "http://localhost:5002/validate",
    json={
        "request_type": "input_validation",
        "input_data": "normal user input"
    }
)
print(response.json())
```

## How to Receive Data

### Example Response:

```
json{
        "status": "valid",
        "message": "Input accepted"
    }
Test program sent request to Input Validation Microservice.
Test program received response from Input Validation Microservice:
{'message': 'Input accepted', 'status': 'valid'}
```

## UML Sequence Diagram 

<img width="1063" height="587" alt="Screenshot 2026-05-20 200907" src="https://github.com/user-attachments/assets/000743ce-a207-4cd3-954a-5b3c133bd35e" />
