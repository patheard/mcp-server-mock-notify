# MCP Server for GC Notify

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

## Running locally

Start the MCP notify server using uvicorn:

```bash
uv run --directory server uvicorn server:app
```

The server will be available at `http://localhost:8000/notify/mcp/`.


## Running as an AWS Lambda function

The Terraform creates a function with a function URL:

```bash
DOCKER_TAG="$AWS_ACCOUNT_ID.dkr.ecr.ca-central-1.amazonaws.com/mcp-server-mock-notify"

# Build the Docker image
docker build -t $DOCKER_TAG -f ./server/Dockerfile ./server

# Create the function
cd terraform
terraform init
terraform apply -target=aws_ecr_repository.mcp_server_mock_notify
docker push $DOCKER_TAG
terraform apply
```

