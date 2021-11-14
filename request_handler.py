from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from posts import get_all_posts, get_single_post, delete_post, create_post, update_post


class HandleRequests(BaseHTTPRequestHandler):
    # Jon B: Setting the headers for our request handler
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
    # This is for the requests other than GET. It will allows us to do the other methods.

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()


# We are missing do_PUT, do_GET, do_DELETE, do_POST

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
