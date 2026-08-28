import http.server
import os
import subprocess
import sys
import threading
import time

PORT = int(os.environ.get("PORT", 8080))


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, *args):
        pass


def start_http():
    http.server.HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()


if __name__ == "__main__":
    threading.Thread(target=start_http, daemon=True).start()
    while True:
        code = subprocess.run([sys.executable, "main.py"]).returncode
        print(f"main.py exited with code {code}, restarting in 10 seconds...")
        time.sleep(10)
