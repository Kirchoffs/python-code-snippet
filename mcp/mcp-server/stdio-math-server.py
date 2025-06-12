from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("stdio-math-server", log_level="ERROR")

@mcp.tool()
def add(a: str, b: str) -> str:
    """
    Add two numbers
    """
    return str(int(a) + int(b))

@mcp.tool()
def multiply(a: str, b: str) -> str:
    """
    Multiply two numbers
    """
    return str(int(a) * int(b))

@mcp.tool()
def subtract(a: str, b: str) -> str:
    """
    Subtract two numbers
    """
    return str(int(a) - int(b))

if __name__ == "__main__":
    print("MCP server is running using stdio transport ...")
    mcp.run(transport="stdio")
