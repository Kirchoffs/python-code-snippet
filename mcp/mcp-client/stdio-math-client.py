import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

class StdioClient:
    def __init__(self, command="python", args=None, env=None):
        if args is None:
            args = ["../mcp-server/stdio-math-server.py"]

        self.server_params = StdioServerParameters(
            command=command,
            args=args,
            env=env,
        )
        self._stdio_client_cm = None
        self.session = None

    async def __aenter__(self):
        self._stdio_client_cm = stdio_client(self.server_params)
        read_stream, write_stream = await self._stdio_client_cm.__aenter__()
        self.session = ClientSession(read_stream, write_stream)
        await self.session.__aenter__()
        await self.session.initialize()
        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        if self.session:
            await self.session.__aexit__(exc_type, exc_value, traceback)
        if self._stdio_client_cm:
            await self._stdio_client_cm.__aexit__(exc_type, exc_value, traceback)

        self._stdio_client_cm = None
        self.session = None

    async def list_tools(self):
        if not self.session:
            raise RuntimeError("Client session is not initialized.")
        raw_output = await self.session.list_tools()
        tools = [
            {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.inputSchema
            }
            for tool in raw_output.tools
        ]
        return tools

    async def add_numbers(self, a: int, b: int):
        if not self.session:
            raise RuntimeError("Client session is not initialized.")
        raw_output = await self.session.call_tool("add", {"a": a, "b": b})
        result = raw_output.content.pop().text
        return result
    
async def main():
    async with StdioClient() as client:
        tools = await client.list_tools()
        print("\nAvailable Tools and Resources:")
        print(json.dumps(tools, indent=2))
        
        result = await client.add_numbers(5, 3)
        print("\n5 + 3 =", result)

if __name__ == "__main__":
    asyncio.run(main())
