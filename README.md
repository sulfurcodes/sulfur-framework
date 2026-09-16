# Web Server with Python

A minimal HTTP web server built from scratch in Python using raw TCP sockets.

> **Status:** Early development

## About

It is a from-scratch HTTP server built using Python's low-level `socket` module.

The goal isn't to replace production web servers or frameworks like Flask, FastAPI, or Django. It's to understand what actually happens between a client sending an HTTP request and a server returning an HTTP response.

The project starts at the TCP level and gradually builds the basic pieces required to handle HTTP requests and responses.

## Current Features

* TCP server built with Python sockets
* IPv4 support
* Reusable server address with `SO_REUSEADDR`
* Client connection handling
* Raw HTTP request reception
* Basic HTTP request parsing
* HTTP method, path, and version extraction
* `GET /` route
* Basic `404 Not Found` handling
* Basic `405 Method Not Allowed` handling
* HTML response serving

## Project Structure

```text
web-server/
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
Creates the TCP server, binds it to a host and port, listens for connections, accepts clients, and coordinates the request-response cycle.

**`connection.py`**
Handles low-level socket communication and receives raw HTTP request data from clients.

**`httpparser.py`**
Parses the HTTP request line and extracts the method, path, and HTTP version.

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
git clone https://github.com/sulfurcodes/web-server-with-python.git
cd web-server
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

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

Then open:

```text
http://localhost:5000
```

## Example

A browser sending:

```http
GET / HTTP/1.1
```

is parsed into:

```text
Method: GET
Path: /
Version: HTTP/1.1
```

The server then returns an HTTP response containing the HTML page from `server/1_index.html`.

## Why Build This?

Web frameworks abstract away most of the low-level networking and HTTP details.

This project goes underneath that abstraction to understand the fundamentals:

* How TCP connections are created and accepted
* How raw request data is received
* How an HTTP request is structured
* How requests are parsed
* How HTTP responses are constructed
* How a basic routing system can be built on top of these primitives

## Tech Stack

* Python
* TCP/IP sockets
* HTTP

## Scope

This is a **web server project**, not a backend framework.

It is intentionally small and low-level, with the focus on understanding how HTTP communication works rather than building a production-ready server.

## Roadmap

* Improve HTTP request parsing
* Parse HTTP headers
* Handle request bodies
* Support additional HTTP methods
* Improve HTTP response construction
* Add static file serving
* Add persistent connections
* Add concurrent client handling
* Improve error handling

## Author

Built by [sulfurcodes](https://github.com/sulfurcodes).

---

⭐ Explore the code to see how a basic HTTP web server works from the ground up.
