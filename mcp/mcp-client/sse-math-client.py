import aiohttp
import asyncio
import json
import logging

class SSEClient:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.messages_url = f"{base_url}/messages"
        self.sse_url = f"{base_url}/sse"

    async def list_tools(self):
        """
        List all available tools from the MCP server.
        """
        try:
            introspection_message = {
                "type": "request",
                "action": "introspect",
                "data": {}
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(self.messages_url, json=introspection_message) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get("data", {})
                    else:
                        error_text = await response.text()
                        logging.error(f"Failed to get tools. Status code: {response.status}")
                        logging.error(f"Error response: {error_text}")
                        return None
        except Exception as e:
            logging.error(f"Error listing tools: {e}")
            return None

    async def add_numbers(self, a: int, b: int):
        """
        Use the add tool to sum two numbers.
        """
        message = {
            "type": "request",
            "action": "execute",
            "tool": "add",
            "data": {"a": a, "b": b}
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(self.messages_url, json=message) as response:
                result = await response.json()
                return result.get("data")

async def main():
    client = SSEClient()
    
    tools = await client.list_tools()
    print("\nAvailable Tools and Resources:")
    print(json.dumps(tools, indent=2))
    
    result = await client.add_numbers(5, 3)
    print("\n5 + 3 =", result)
    
if __name__ == "__main__":
    asyncio.run(main())
