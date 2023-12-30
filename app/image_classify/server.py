from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import parse_qs, urlparse
import subprocess

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        url_parts = urlparse(self.path)
        query_params = parse_qs(url_parts.query)
        if 'jpg_url' in query_params:
            url = query_params['jpg_url'][0]
            command = "python3 -m image_classify classify " + url
            output = subprocess.check_output(command, shell=True, text=True)
        else:
            output = "ERROR!"

        # Send a 200 OK response
        self.send_response(200)

        # Set the Content-Type header
        self.send_header('Content-Type', 'text/plain')

        # End the headers
        self.end_headers()

        # Send the response body
        self.wfile.write(output.encode('utf-8'))
        '''
        if 'jpg_url' in payload:
            jpg_url = payload['jpg_url']

            # Perform some processing (replace this with your actual logic)
            response_string = f"Received JPG URL: {jpg_url}. Processing complete."

            # Send the response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'result': response_string}).encode('utf-8'))
        else:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Missing "jpg_url" in payload'}).encode('utf-8'))
        '''