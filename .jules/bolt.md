## 2026-07-22 - HTTP Connection Reuse in Python Requests
**Learning:** Re-creating HTTP connections (`requests.get(...)`) in a loop incurs repeated TCP and TLS handshakes, adding ~85ms of network overhead per request.
**Action:** Use `requests.Session()` to enable HTTP Keep-Alive and connection pooling across sequential API requests.
