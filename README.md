# MCP Notify

A Model Context Protocol (MCP) server for sending notifications through a mock GC Notify service.

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for Python package management.

1. Install uv or use the provided [devcontainer](https://code.visualstudio.com/docs/devcontainers/tutorial):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Install dependencies:
   ```bash
   uv sync --directory server
   ```

## Running the Server

Start the MCP notify server using uvicorn:

```bash
uv run --directory server uvicorn server:app
```

The server will be available at `http://localhost:8000/notify/mcp/` by default.
