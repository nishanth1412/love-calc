from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import mysql.connector

# Define the handler class
class MyHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        # Get the length of the request data
        content_length = int(self.headers['Content-Length'])

        # Extract the request body
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Parse the request body to get the form data
        form_data = parse_qs(post_data)

        # Get the values from the form data
        name1 = form_data['name1'][0]
        name2 = form_data['name2'][0]
        #percetage = form_data['percentage'][0]

        # Connect to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Gagana1!",
            database="abc"
        )

        # Create a cursor object to interact with the database
        mycursor = mydb.cursor()

        # Prepare the SQL query to insert data into the table
        sql = "INSERT INTO love (name1, name2) VALUES (%s, %s)"
        values = (name1, name2)

        # Execute the SQL query
        mycursor.execute(sql, values)

        # Commit the changes to the database
        mydb.commit()

        # Close the database connection
        mydb.close()

        # Send the HTTP response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Write the response HTML
        response_html = "<html><body><h1>Data inserted successfully</h1></body></html>"
        self.wfile.write(response_html.encode())

# Define the HTTP server settings
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)

# Start the HTTP server
print('Starting the server...')
httpd.serve_forever()
