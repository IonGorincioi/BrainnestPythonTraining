# server side

# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print ("Socket successfully created")

# reserve a port on your computer in our
# case it is 40674 but it can be anything
port = 40674

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print (f"socket binded to {port}")

# put the socket into listening mode
s.listen(5)
print ("socket is listening")

# a forever loop until we interrupt it or
# an error occurs
while True:

    # Establish connection with client.
    c, addr = s.accept()
    print ('Got connection from', addr )

    # send a thank you message to the client.
    c.send(b'Thank you for connecting')

    # Close the connection with the client
    c.close()


# client side

# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 40674

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server
print(s.recv(1024))

# close the connection
s.close()



# Import libraries
import requests

# Sending Request
req = requests.get('https://www.google.com/')

# Show results
print(req.text[:2000])


# Beautiful Soup
import requests
from bs4 import BeautifulSoup

# Sending Request
req = requests.get('https://www.google.com/')

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(req.text, 'html.parser')

# Find and print the title tag
title_tag = soup.find('title')
print(title_tag.text)

# Find and print the first paragraph of text on the page
paragraph = soup.find('p')
print(paragraph.text)

# Find all the links on the page and print their URLs
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

# Find all the images on the page and print their source URLs
images = soup.find_all('img')
for image in images:
    print(image.get('src'))



# Import Libraries
import requests

# Creating Session
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/419735271')

# Getting Response
r = s.get('http://httpbin.org/cookies')

# Show Response
print(r.text)



# Import Libraries
import requests

# Error Handling
try:
	
	# Creating Request
	req = requests.get('https://www.google.com/', timeout=0.000001)
	
except requests.exceptions.RequestException as e:
	
	# Raising Error
	raise SystemExit(e)



import requests

try:
    # Creating Request
    req = requests.get('https://www.google.com/', timeout=5)
    
    # Checking Status Code
    if req.status_code == 200:
        print("Request successful")
    else:
        print(f"Request failed with status code {req.status_code}")
except requests.exceptions.RequestException as e:
    # Raising Error
    raise SystemExit(e)


# Import libraries
import http.server
import socketserver

# Defining PORT number
PORT = 8080

# Creating handle
Handler = http.server.SimpleHTTPRequestHandler

# Creating TCPServer
http = socketserver.TCPServer(("127.0.0.1", PORT), Handler)

# Getting logs
print("serving at port", PORT)
http.serve_forever()

# client side
import requests

response = requests.get('http://127.0.0.1:8080')
print(response.text)

# another version
import requests

response = requests.get('http://127.0.0.1:8080/data.json')
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error retrieving file: {response.status_code} {response.reason}")




# DNS Look-up

# Import libraries
import dns.resolver

# Finding A record
result = dns.resolver.resolve('google.com', 'A')

# Printing record
for val in result:
	print('A Record : ', val.to_text())


# Import libraries
import dns.resolver

# Finding PTR record
result = dns.resolver.resolve('116.62.218.34.in-addr.arpa', 'PTR')

# Printing record
for val in result:
	print('PTR Record : ', val.to_text())


# Import libraries
import dns.resolver

# Finding NS record
result = dns.resolver.resolve('google.com', 'NS')

# Printing record
for val in result:
	print('NS Record : ', val.to_text())


# Import libraries
import dns.resolver

# Finding MX record
result = dns.resolver.query('tryhackme.com', 'MX')

# Printing record
for val in result:
	print('MX Record : ', val.to_text())



import socket

# Define the target host and the ports to scan
host = 'example.com'
port_list = [53, 80, 8080, 443]

# Loop over the ports and check if they are open
for port in port_list:
    # Create a new socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a timeout of 1 second
    s.settimeout(1)
    
    # Attempt to connect to the target host and port
    try:
        s.connect((host, port))
        print(f"Port {port} is open")
    except:
        print(f"Port {port} is closed")
    
    # Close the socket object
    s.close()



import os

hostname = "google.com"
response = os.system("ping -n 4 " + hostname)

if response == 0:
    print(hostname, "is up!")
else:
    print(hostname, "is down.")

