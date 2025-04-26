# plotting.py
import http.server
import socketserver
import threading
import webbrowser
import tempfile
import os
import tempfile
import matplotlib.pyplot as plt
import mpld3
import httpplot.example_plots as ex


def serve_html(html: str, port: int = 8000):
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".html") as tmp:
        tmp.write(html)
        tmp_path = tmp.name

    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def do_get(self):
            if self.path == '/':
                self.path = '/' + os.path.basename(tmp_path)
            return super().do_GET()
        
        def log_message(self, format, *args):
            pass # suppress logging
        
    def start_server():
        with socketserver.TCPServer(("", port), CustomHandler) as httpd:
            print(f"Serving at port {port}")
            httpd.serve_forever()

    thread = threading.Thread(target=start_server, daemon=True)
    thread.start()


    webbrowser.open(f"http://localhost:{port}/")

    input("Press enter to stop server and clean up")

    thread.join(0.1)
    os.remove(tmp_path)


if __name__ == "__main__":
    html = "<html><body><h1>Hello!</h1></body></html>"
    serve_html(html)
