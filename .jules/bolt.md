# Bolt's Journal - Critical Learnings

## 2025-05-20 - Connection Pooling with `requests.Session()`
**Learning:** Calling `requests.get()` in a tight or repetitive loop opens and closes TCP sockets and re-negotiates TLS handshakes for every HTTP request. Using `requests.Session()` reuses the underlying connection (HTTP Keep-Alive), significantly reducing request latency and CPU overhead.
**Action:** Use `requests.Session()` for repeated HTTP requests to the same origin.
