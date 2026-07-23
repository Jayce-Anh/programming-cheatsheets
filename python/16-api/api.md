# 16. API

An **API** (**Application Programming Interface**) lets one program talk to another program. In Python, APIs are often used to get data from websites, send data to servers, or connect your app to external services.

## How API works

APIs are commonly used to **allowed server or application communicate to share content and receive data**. Example: 
- mobile app -> weather API server -> weather database
- frontend app -> backend API -> database
- login service -> user service
- payment app -> payment API

Simple flow:

1. Your app sends a request to an API
2. The API processes the request and may talk to a server, database, or another service
3. The server sends data back
4. Your app shows the result to the user

Example:

- A user opens a football news mobile app
- The app sends an HTTP `GET` request to a football news API endpoint over HTTPS
- The API returns data like match scores, team news, and player stats in JSON
- The mobile app shows that data on the user's screen
```
Weather app -> API request data -> database -> API response data -> weather app
```
So the API works like a **bridge** between your app and another system.

## Best Practices

- Use the `requests` package for simple HTTP requests
- Check `response.status_code` before using the data
- Use `response.json()` when the API returns JSON
- Add `timeout=` so the request does not wait forever
- Handle errors with `try` / `except`
- Do not hardcode secret API keys in your code

## API Concepts


| Term | Meaning |
|------|---------|
| API | A way for programs to communicate |
| API key | A secret value used to identify and authorize your app |
| Endpoint | The URL of the API |
| Request | What your program sends |
| Response | What the server returns |
| JSON | Common data format used by APIs |
| Header | Extra information sent with the request |
| Status code | Number that shows request result |

## API request 

An API request is the message your app sends to the API.

A request can include:

- method like `GET` or `POST`
- URL or endpoint
- headers
- query parameters
- body data

Example:

```python
import requests

response = requests.get(
    "https://api.example.com/news",
    params={"team": "arsenal"},
    headers={"Accept": "application/json"},
    timeout=10
)
```

In this request:

- `GET` is the method
- `"https://api.example.com/news"` is the API URL
- `params=` adds values to the URL
- `headers=` sends extra information

## API URL syntax

An API URL usually has these parts:

```text
https://api.example.com/users/15?active=true
```

| Part | Example | Meaning |
|------|---------|---------|
| Protocol | `https://` | Secure connection |
| Domain | `api.example.com` | API server name |
| Path | `/users/15` | Specific resource |
| Query string | `?active=true` | Extra filter or option |

More examples:

- `https://api.example.com/posts`
- `https://api.example.com/posts/10`
- `https://api.example.com/comments?postId=1`

## API key concept

An API key is a secret code used to identify your app when it calls an API.

Why APIs use keys:

- control who can use the API
- limit requests
- track usage
- protect private data

Common ways to send an API key:

- in headers
- in query parameters

Example in header:

```python
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
```

Example in URL params:

```python
params = {
    "api_key": "YOUR_API_KEY"
}
```

Best practice:

- keep API keys in environment variables
- never hardcode real keys in your project
- never push real keys to GitHub


## Common HTTP methods

| Method   | Purpose                 |
| -------- | ----------------------- |
| `GET`    | Get data                |
| `POST`   | Send new data           |
| `PUT`    | Replace all data        |
| `PATCH`  | Update part of the data |
| `DELETE` | Delete data             |

## REST API

A **RESTful API** is a common API style that uses:

- URLs to represent resources
- HTTP methods like `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`
- JSON to send and receive data

Simple idea:

- resource = the thing you want to work with
- endpoint = the URL for that resource
- method = the action you want to do

Example resource:

```text
/users
/users/10
```

Common REST examples:

| Method | Endpoint | Meaning |
|--------|----------|---------|
| `GET` | `/users` | Get all users |
| `GET` | `/users/10` | Get one user |
| `POST` | `/users` | Create a new user |
| `PUT` | `/users/10` | Replace user data |
| `PATCH` | `/users/10` | Update part of user data |
| `DELETE` | `/users/10` | Delete one user |

Python example:

```python
import requests

response = requests.get("https://api.example.com/users/10", timeout=10)
print(response.json())
```

Why REST is popular:

- simple and easy to understand
- works well with web and mobile apps
- uses standard HTTP rules


## Install `requests`

```bash
pip install requests
```

## Syntax:

```python
import requests

response = requests.get("https://api.example.com/users", timeout=10)

print(response.status_code)
print(response.text)

data = response.json()
print(data)
```

- `requests.get()`: sends a GET request
- `response.status_code`: shows the result like `200` or `404`
- `response.text`: response body as text
- `response.json()`: response body converted to Python data
- `timeout=10`: stop waiting after 10 seconds

## Common status codes


| Code  | Meaning              |
| ----- | -------------------- |
| `200` | Success              |
| `201` | Created successfully |
| `400` | Bad request          |
| `401` | Unauthorized         |
| `403` | Forbidden            |
| `404` | Not found            |
| `500` | Server error         |


## GET request

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=10)

if response.status_code == 200:
    users = response.json()
    print(users[0]["name"])
else:
    print("Request failed")
```

## Send query parameters

Use `params=` to send filters or search values.

```python
import requests

params = {"postId": 1}
response = requests.get(
    "https://jsonplaceholder.typicode.com/comments",
    params=params,
    timeout=10
)

print(response.url)
print(response.json()[:2])
```

## POST request

Use `json=` to send JSON data.

```python
import requests

new_post = {
    "title": "Hello",
    "body": "My first API post",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post,
    timeout=10
)

print(response.status_code)
print(response.json())
```

## Headers

Headers often send token, content type, or app info.

```python
import requests

headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Accept": "application/json"
}

response = requests.get(
    "https://api.example.com/profile",
    headers=headers,
    timeout=10
)
```

## Read JSON data

Most APIs return JSON. Python converts JSON into normal Python objects.

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
data = response.json()

print(type(data))         # dict
print(data["title"])
print(data["completed"])
```

## Error handling

```python
import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=10)
    response.raise_for_status()
    data = response.json()
    print(data[0]["email"])
except requests.exceptions.Timeout:
    print("The request took too long")
except requests.exceptions.HTTPError:
    print("HTTP error happened")
except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")
```

## API key example

Many real APIs need a key.

```python
import os
import requests

api_key = os.getenv("API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(
    "https://api.example.com/data",
    headers=headers,
    timeout=10
)
```

Best practice:

- Store keys in environment variables
- Do not put real keys directly in code
- Do not upload keys to GitHub

## Notes

- APIs usually return JSON, not plain text
- `GET` is for reading data
- `POST` is for creating data
- `params=` adds values to the URL query string
- `json=` sends Python data as JSON
- `raise_for_status()` helps catch bad responses

## Common Pitfalls

| Issue                  | Tip                                   |
| ---------------------- | ------------------------------------- |
| Request hangs too long | Add `timeout=`                        |
| API returns error code | Check `response.status_code`          |
| JSON decode error      | Make sure the response is really JSON |
| Secret key exposed     | Use environment variables             |
| Wrong endpoint         | Check the URL carefully               |


## Building API

Use a web framework like **FastAPI** or **Flask**.  
FastAPI is a popular choice for building JSON APIs in Python.

### Install packages

```bash
pip install fastapi uvicorn
```

- `fastapi`: framework for building APIs
- `uvicorn`: server used to run the FastAPI app

### Create `main.py`

```python
# Import FastAPI framework
from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI()

# Handle GET request to the home page
@app.get("/")
def home():
    # Send JSON response back to the user
    return {"message": "Hello World"}

# Handle GET request to /users
@app.get("/users")
def get_users():
    # Return a list of users
    return [
        {"id": 1, "name": "Jayce"},
        {"id": 2, "name": "Anna"}
    ]

# Handle POST request to /users
@app.post("/users")
def create_user(user: dict):
    # Receive user data and return it back
    return {"message": "User created", "user": user}
```

### Run the API

```bash
uvicorn main:app --reload
```

- `main`: file name is `main.py`
- `app`: FastAPI app variable
- `--reload`: restarts server when code changes

### Test in browser

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/users`
- `http://127.0.0.1:8000/docs`

### How it works

- `@app.get("/")` handles a `GET` request to `/`
- `@app.get("/users")` returns user data
- `@app.post("/users")` receives data and creates a new user
- FastAPI automatically converts Python dictionaries and lists into JSON
- `/docs` shows automatic API documentation

### Example request and response

`POST /users`

Request body:

```json
{
  "name": "Maria",
  "age": 22
}
```

Response:

```json
{
  "message": "User created",
  "user": {
    "name": "Maria",
    "age": 22
  }
}
```