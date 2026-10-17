# Test host: serves a directory, answers 401 unless the request carries `Authorization: Bearer beta-secret`.
# usage: authsrv.py DIR PORT LOGFILE   (writes its own log file; never touches stderr, which closes with a CI step)
import http.server, sys, os
os.chdir(sys.argv[1])
PORT = int(sys.argv[2])
LOG = sys.argv[3]
def log(line):
    with open(LOG, "a") as f:
        f.write(line + "\n")
class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        ok = self.headers.get("Authorization") == "Bearer beta-secret"
        log("REQ %s %s auth=%s" % (self.command, self.path, "ok" if ok else "missing-or-wrong"))
        if not ok:
            self.send_response(401); self.send_header("Content-Length", "2"); self.end_headers(); self.wfile.write(b"no"); return
        return super().do_GET()
    def log_message(self, *a): pass
log("listening on %d" % PORT)
http.server.ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
