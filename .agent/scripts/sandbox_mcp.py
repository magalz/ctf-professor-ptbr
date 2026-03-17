import os
import sys
import logging
from mcp.server.fastmcp import FastMCP  # type: ignore

# Ensure we can import from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from sandbox_manager import SandboxManager  # type: ignore

# Suppress logging to stdout/stderr since MCP uses them for protocol
logging.getLogger("sandbox_manager").setLevel(logging.CRITICAL)

# Create an MCP server
mcp = FastMCP("CTF Sandbox")
manager = SandboxManager()

@mcp.tool()
def execute_in_sandbox(command: str) -> str:
    """
    Execute a command inside the isolated CTF Kali Linux Docker Sandbox.
    Use this to safely run commands, compile binaries, or interact with external services.
    Returns the stdout, stderr, and exit code of the command.
    """
    try:
        manager.start()
        code, out, err = manager.execute_command(command)
        result = f"Exit code: {code}\n"
        if out:
            result += f"STDOUT:\n{out}\n"
        if err:
            result += f"STDERR:\n{err}\n"
        return result
    except Exception as e:
        return f"Error executing in sandbox: {e}"

@mcp.tool()
def start_sandbox() -> str:
    """Start the sandbox container manually."""
    if manager.start():
        return "Sandbox started successfully."
    return "Failed to start sandbox."

@mcp.tool()
def stop_sandbox() -> str:
    """Stop the sandbox container."""
    if manager.stop():
        return "Sandbox stopped successfully."
    return "Failed to stop sandbox."

@mcp.tool()
def sandbox_status() -> str:
    """Check if the sandbox container is currently running."""
    if manager.is_running():
        return "Sandbox is currently RUNNING."
    return "Sandbox is currently STOPPED."

if __name__ == "__main__":
    mcp.run()
