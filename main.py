import http.server
import socketserver
import json
import os
import time

PORT = int(os.environ.get("PORT", 8000))

class MCPHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type='application/json'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_POST(self):
        if self.path == '/process_message':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                request_payload = json.loads(post_data)
                message_content = request_payload.get('message', 'No message provided')
                
                # --- Core concept: Simulate Message Content Processing (MCP) ---
                # This is where your custom logic for the MCP server would go.
                # For example, fetching data from a database, calling another API,
                # applying business rules, or performing complex text analysis.
                processed_content = f"Processed by MCP: '{message_content.upper()}'"
                
                # Simulate adding additional context or data relevant to the processing
                additional_data = {
                    "timestamp": time.time(),
                    "original_length": len(message_content),
                    "source_system": "Custom_MCP_Service"
                }

                response_payload = {
                    "status": "success",
                    "processed_message": processed_content,
                    "metadata": additional_data
                }
                
                self._set_headers(200)
                self.wfile.write(json.dumps(response_payload).encode('utf-8'))
            except json.JSONDecodeError:
                self._set_headers(400)
                self.wfile.write(json.dumps({"status": "error", "message": "Invalid JSON payload"}).encode('utf-8'))
            except Exception as e:
                self._set_headers(500)
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"status": "error", "message": "Not Found"}).encode('utf-8'))

    def do_GET(self):
        # A simple GET endpoint for health check or service description
        if self.path == '/':
            self._set_headers(200)
            self.wfile.write(json.dumps({
                "service_name": "Anthropic MCP Connector Example",
                "description": "This is a mock Message Content Processor (MCP) server designed to demonstrate how a custom service could expose an API for Anthropic's Connector Directory. It processes incoming messages and returns a modified version.",
                "status": "running"
            }).encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"status": "error", "message": "Not Found"}).encode('utf-8'))


def run_server():
    with socketserver.TCPServer(('', PORT), MCPHandler) as httpd:
        print(f"Serving MCP server at http://localhost:{PORT}/")
        print(f"Send POST requests to http://localhost:{PORT}/process_message")
        print("Press Ctrl+C to stop the server.")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
