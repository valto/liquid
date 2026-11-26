#!/usr/bin/env python3
"""Serve the generated /liquid/ project path on loopback only."""
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
import argparse

ROOT=Path(__file__).resolve().parents[1]
class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if not self.path.startswith('/liquid/'):
            self.send_response(302);self.send_header('Location','/liquid/');self.end_headers();return
        self.path=self.path.removeprefix('/liquid')
        super().do_GET()
    def log_message(self,*args):pass

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--port',type=int,default=8790);args=p.parse_args()
    server=ThreadingHTTPServer(('127.0.0.1',args.port),partial(Handler,directory=str(ROOT/'docs')))
    print(f'Preview: http://127.0.0.1:{args.port}/liquid/',flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:server.server_close()
