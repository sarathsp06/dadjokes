## 2026-10-27 - Reuse HTTP Connections with requests.Session

**Learning:** Repeated calls using `requests.get()` establish new TCP connections and TLS handshakes each time, introducing ~40-50% overhead for sequential HTTP requests to the same endpoint.
**Action:** Use a persistent `requests.Session()` instance to enable HTTP keep-alive connection pooling across repeated API requests.
