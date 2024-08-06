from http.server import BaseHTTPRequestHandler
import subprocess

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        result = subprocess.run(['streamlit', 'run', 'try.py', '--server.port', '8501', '--server.headless', 'true'], capture_output=True, text=True)
        self.wfile.write(result.stdout.encode())
        return
