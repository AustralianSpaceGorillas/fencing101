"""Run the Fencing101 website with Python 3. No external packages required."""
import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

PAGE = Path(__file__).resolve().parent / "index.html"


class FencingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlsplit(self.path).path
        if path in ("/", "/index.html"):
            try:
                body = PAGE.read_bytes()
            except OSError:
                self.send_error(500, "Website file could not be read")
                return
            content_type = "text/html; charset=utf-8"
        elif path == "/health":
            body = b'{"status":"ok","project":"fencing101"}'
            content_type = "application/json; charset=utf-8"
        elif path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return
        else:
            self.send_error(404, "Page not found")
            return
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def do_HEAD(self):
        self.do_GET()


def main():
    parser = argparse.ArgumentParser(description="Serve the Fencing101 website")
    parser.add_argument("--host", default="127.0.0.1", help="Bind address (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8765, help="Port (default: 8765)")
    args = parser.parse_args()
    if not PAGE.is_file():
        parser.error("index.html must be in the same folder as app.py")
    try:
        server = ThreadingHTTPServer((args.host, args.port), FencingHandler)
    except OSError as error:
        parser.exit(1, f"Could not start server: {error}. Try another --port.\n")
    print(f"Fencing101 is running at http://{args.host}:{args.port}/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping Fencing101.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
