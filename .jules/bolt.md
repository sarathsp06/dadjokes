## 2026-03-30 - Connection Reuse with requests.Session()
**Learning:** Re-using `requests.Session()` across repeated HTTP requests to the same origin avoids setting up a new TCP connection and performing a TLS handshake on every request, reducing latency per request by ~50% or more.
**Action:** Always use `requests.Session()` when polling or fetching endpoints repeatedly in Python.
