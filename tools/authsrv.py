# Test host: serves a directory, answers 401 unless the request carries `Authorization: Bearer beta-secret`.
import http.server, sys, os
os.chdir(sys.argv[1])
PORT = int(sys.argv[2])
class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        ok = self.headers.get("Authorization") == "Bearer beta-secret"
        sys.stderr.write("REQ %s %s auth=%s\n" % (self.command, self.path, "ok" if ok else "missing-or-wrong")); sys.stderr.flush()
        if not ok:
            self.send_response(401); self.end_headers(); self.wfile.write(b"no"); return
        return super().do_GET()
    def log_message(self, *a): pass
http.server.ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
