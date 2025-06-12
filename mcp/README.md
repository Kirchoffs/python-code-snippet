# Notes
## Python
```
>> python -m pip install mcp
```

## Cline
cline_mcp_settings.json:
```json
{
  "mcpServers": {
    "math-server": {
      "disabled": false,
      "timeout": 60,
      "type": "stdio",
      "command": "/path/to/python",
      "args": [
        "/path/to/stdio-math-server.py"
      ],
      "autoApprove": [
        "add",
        "subtract",
        "multiply"
      ]
    }
  }
}
```
