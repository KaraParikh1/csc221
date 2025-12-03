#Lesson 14 DJ4E

##The 'Big Picture' of a Django Application running on PythonAnywhere
- In Django, create objects, then load them to create web application
- User requests browser page, which is routed to application which may request information from a database
- urls.py defines URL configuration
- settings.py creates settings for web app
- mysite directory contains configuration, other directories are applications
- source code and working directory must be home directory
- WSGI config file must be properly setup to avoid errors
- ensure correct python version and virtual environment
- WSGI config tells browser to read settings.py
   - settings.py allowed_hosts: lists host/domain names your site can serve, * means no filter
   - ROOT_URLCONF: first part of url
- urls.pt sets up global url routing (second part of url)
- include in urlpatterns is defining import imported by settings.py
- every application has urls.py and view.py
   - the application individual urls.py routes to parts of the application
   - after root url then application it looks to individual urls.py
- view recieves request and generates response
- Templates provide presentation logic to views

##Exploring HTTP
- hypertext transfer protocol
- URL: uniform resource locator
- allows for multiple protocols
- protocol://host/document
- order: make a connection, request a document, recieve the document, close the connection
- invented in 1990
- internet standards developed by Internet Engineering Task Force (IETF)
- standards called RFCs
- connect to server on a socket like port 80 or 443, client sends request (GET url protocol), then it gives html usually

##Web Applications and the Request/Response Cycle
- user clicks on page, browser sends GET request, server returns HTML document
- Browser uses: HTML, CSS, DOM, JavaScript, JQuery
Web server uses: Django/Flask/Sqlite3/MySQL

##Using Sockets to Make Network Connections in Python
-socket is network endpoint that lets computers exchange data 
- python built in socket library
- Create a socket object.
- Connect to a remote address and port. - Send a properly formatted request. - Receive and process the response (often in chunks).
- sockets simplify the process and are good for learning

##Building a Simple Web Browser in Python
- import socket
- Create a TCP/IP socket
- Connect the socket to a web server and port 80 (HTTP)
- Send an HTTP GET request
- The request must end with \r\n\r\n to indicate end of headers
- Decode bytes to string and print
- Close the socket

##Building a Simple HTTP Server in Python
- uses Python’s standard library 
- The server listens on a given port for incoming connections.  
- After receiving an HTTP request, the server parses the request, creates HTTP response, and sends back.  
- server can send a simple hard‑coded HTML response for all requests 
- demonstrates at a low level how web server behavior underlies what high‑level framweorks do for you. 
- With such a simple server, you can see the raw HTTP request/response cycle and understand better
