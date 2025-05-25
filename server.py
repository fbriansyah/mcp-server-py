from mcp.server.fastmcp import FastMCP
from utils.database import init_db

# This is the shared MCP server instance
mcp = FastMCP("mix_server")

# Initialize the database
init_db()
