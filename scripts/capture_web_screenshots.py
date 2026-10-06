"""
Capture High-Resolution Evidence Screenshots of Web Integration
Launches the Flask web application locally and captures full-page
screenshots of /, /dashboard, /story, and /about using Playwright.
"""

import os
import time
import threading
from werkzeug.serving import make_server
from playwright.sync_api import sync_playwright
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

class ServerThread(threading.Thread):
    def __init__(self, app, host='127.0.0.1', port=5055):
        super().__init__()
        self.server = make_server(host, port, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()

def capture_screenshots():
    output_dir = os.path.join('evidence', 'web_integration')
    os.makedirs(output_dir, exist_ok=True)

    server = ServerThread(app, port=5055)
    server.start()
    time.sleep(1.5) # Wait for server startup

    base_url = 'http://127.0.0.1:5055'

    pages_to_capture = [
        {'route': '/', 'filename': 'home_page.png', 'name': 'Overview / Home'},
        {'route': '/dashboard', 'filename': 'dashboard_page.png', 'name': 'Dashboards'},
        {'route': '/story', 'filename': 'story_page.png', 'name': 'Guided Data Story'},
        {'route': '/about', 'filename': 'about_page.png', 'name': 'Methodology & About'}
    ]

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(viewport={'width': 1440, 'height': 900})
            page = context.new_page()

            for item in pages_to_capture:
                url = base_url + item['route']
                print(f"Navigating to {url} ({item['name']})...")
                page.goto(url, wait_until='networkidle')
                time.sleep(0.5)

                dest_path = os.path.join(output_dir, item['filename'])
                page.screenshot(path=dest_path, full_page=True)
                print(f"Captured {item['filename']} -> {dest_path}")

            browser.close()
    finally:
        server.shutdown()
        server.join()
        print("Server stopped cleanly.")

if __name__ == '__main__':
    capture_screenshots()
