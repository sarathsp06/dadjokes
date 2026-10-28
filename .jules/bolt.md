## 2024-05-19 - HTTP Connection Pooling with `requests.Session`
**Learning:** In polling loops making repeated HTTP requests to the same origin, creating new `requests.get()` calls repeatedly creates and destroys TCP/TLS connections. Reusing a `requests.Session()` maintains a persistent HTTP connection pool, eliminating TCP/TLS handshake latency and reducing CPU overhead per request.
**Action:** Always use `requests.Session()` for repeated HTTP requests to the same endpoint or domain.
