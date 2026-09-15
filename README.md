# Sulfur Framework

A lightweight Python web server and backend framework built from scratch to understand how web servers and HTTP work under the hood.

> **Status:** Veryy Early development

## About

Sulfur Framework is a from-scratch web server project built using Python's low-level `socket` module.

The goal isn't to replace production frameworks like Flask, FastAPI, or Django. The goal is to understand what actually happens between a browser sending an HTTP request and a server returning an HTTP response.

Currently, the project handles TCP connections, receives raw HTTP requests, parses the request line, and generates basic HTTP responses.

## Current Features

* TCP server built with Python sockets
* IPv4 support
* Reusable server address with `SO_REUSEADDR`
* Basic HTTP request parsing
* HTTP method, path, and version extraction
* `GET /` route
* Basic `404 Not Found` handling
* Basic `405 Method Not Allowed` handling
* HTML response serving

## Project Structure

```text
sulfur-framework/
│
├── server/
│   ├── 1_index.html
│   ├── connection.py
│   ├── httpparser.py
│   ├── response.py
│   └── socketserver.py
│
└── README.md
```

### Components

**`socketserver.py`**
Creates the TCP server, listens for incoming connections, and coordinates the request-response cycle.

**`connection.py`**
Handles low-level socket communication and receives raw request data from clients.

**`httpparser.py`**
Parses the raw HTTP request line into the HTTP method, path, and HTTP version.

**`response.py`**
Generates an HTTP response based on the parsed request.

**`1_index.html`**
The HTML page served for the root `/` route.

## Request Flow

```text
Browser
   │
   ▼
TCP Connection
   │
   ▼
connection.py
   │
   ▼
Raw HTTP Request
   │
   ▼
httpparser.py
   │
   ▼
Method + Path + HTTP Version
   │
   ▼
response.py
   │
   ▼
HTTP Response
   │
   ▼
Browser
```

## Running Locally

Clone the repository:

```bash
git clone https://github.com/sulfurcodes/sulfur-framework.git
cd sulfur-framework
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

Start the server:

```bash
python server/socketserver.py
```

You should see:

```text
Listening on port 5000
```

Open:

```text
http://localhost:5000
```

## Example

A request to:

```http
GET / HTTP/1.1
```

is parsed into:

```text
Method: GET
Path: /
Version: HTTP/1.1
```

The server then returns the HTML page from `server/1_index.html`.

## Why Build This?

Most web developers use frameworks without needing to think about what happens underneath them.

This project is an attempt to go one layer deeper:

* How TCP connections are accepted
* How HTTP requests reach a server
* How HTTP requests are structured
* How requests are parsed
* How HTTP responses are constructed
* How routing can eventually be built on top of these primitives

## Tech Stack

* Python
* TCP/IP sockets
* HTTP

## Note

Sulfur Framework is an educational and experimental project. It is **not production-ready** and should not be used as a replacement for established Python web frameworks.

## Author

Built by [sulfurcodes](https://github.com/sulfurcodes).

---

⭐ If you're interested in learning how web servers work from the ground up, feel free to explore the code.
