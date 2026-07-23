Read the Apache-style access log from /app/access.log and generate a JSON report at /app/report.json.

Treat each non-empty line as one request. Use the first whitespace-delimited field as the client IP address. Extract the request path from the quoted HTTP request line (between the HTTP method and the protocol version).

Write a single valid JSON object to /app/report.json with exactly these keys:

- total_requests
- unique_ips
- top_path

Requirements:
- total_requests must be an integer.
- unique_ips must be an integer.
- top_path must be a string.

Success criteria:

1. total_requests equals the number of non-empty log entries in /app/access.log.
2. unique_ips equals the number of distinct client IP addresses in /app/access.log.
3. top_path equals the most frequently requested path in /app/access.log.