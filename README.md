# Anthropic Connector Message Processor Server

This example demonstrates a minimal Message Content Processor (MCP) server implemented in Python using standard libraries. It simulates a custom service that could be integrated with Anthropic's Connector Directory. The server exposes a `/process_message` endpoint to receive and process content, returning a structured JSON response.

## Language

`python`

## How to Run

1. Save the code as `main.py`.
2. Run the server: `python main.py`
3. Send a POST request to `http://localhost:8000/process_message` with a JSON body, e.g., `curl -X POST -H "Content-Type: application/json" -d '{"message": "hello world from anthropic"}' http://localhost:8000/process_message`

## Original Article

This example accompanies the Turkish article: [MCP Sunucunuzu Anthropic'in Bağlayıcı Dizinine Nasıl Gönderirsiniz? (Deneyimleyen Birinden Adım Adım Rehber)](https://fatihsoysal.com/blog/mcp-sunucunuzu-anthropicin-baglayici-dizinine-nasil-gonderirsiniz-deneyimleyen-birinden-adim-adim-rehber/).

## License

MIT — see [LICENSE](LICENSE).
