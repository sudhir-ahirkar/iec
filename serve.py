#!/usr/bin/env python3
"""Local preview server with pretty URLs and enquiry POST → /thank-you.

Production still uses Netlify Forms — do not use this on the live host."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = 8095

PRETTY = {
    "/about": "/about.html",
    "/exports": "/exports.html",
    "/imports": "/imports.html",
    "/products": "/products.html",
    "/services": "/service.html",
    "/service": "/service.html",
    "/markets": "/markets.html",
    "/contact": "/contact.html",
    "/quote": "/quote.html",
    "/privacy": "/privacy.html",
    "/thank-you": "/thank-you.html",
}


def resolve(path: str) -> str:
    raw = path.split("?", 1)
    clean = raw[0].rstrip("/") or "/"
    mapped = PRETTY.get(clean, raw[0] if clean != "/" else "/")
    if len(raw) > 1:
        return mapped + "?" + raw[1]
    return mapped


class PreviewHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = resolve(self.path)
        return super().do_GET()

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        if length:
            self.rfile.read(length)
        self.send_response(303)
        self.send_header("Location", "/thank-you")
        self.end_headers()


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", PORT), PreviewHandler)
    print(f"Preview: http://127.0.0.1:{PORT}/")
    print("Pretty URLs such as /about and /services are mapped locally.")
    server.serve_forever()
