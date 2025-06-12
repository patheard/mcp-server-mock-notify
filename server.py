from mcp.server.fastmcp import FastMCP
import httpx
import json
from typing import Optional, Dict, Any
from pydantic import BaseModel


mcp = FastMCP("MockNotifyService MCP")


class NotifyResponse(BaseModel):
    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    status_code: Optional[int] = None


# Configuration
DEFAULT_BASE_URL = "https://notify.ai-jam.cdssandbox.xyz"  # Remote hosted service URL


async def make_request(
    method: str, 
    endpoint: str, 
    api_key: Optional[str] = None, 
    data: Optional[Dict] = None,
    base_url: str = DEFAULT_BASE_URL
) -> NotifyResponse:
    """Helper function to make HTTP requests to the MockNotifyService"""
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["X-API-Key"] = api_key
    
    url = f"{base_url.rstrip('/')}{endpoint}"
    
    try:
        async with httpx.AsyncClient() as client:
            if method.upper() == "GET":
                response = await client.get(url, headers=headers)
            elif method.upper() == "POST":
                response = await client.post(url, headers=headers, json=data)
            else:
                return NotifyResponse(success=False, error=f"Unsupported HTTP method: {method}")
            
            response_data = response.json() if response.headers.get("content-type", "").startswith("application/json") else {"raw": response.text}
            
            return NotifyResponse(
                success=response.status_code < 400,
                data=response_data,
                status_code=response.status_code
            )
    except Exception as e:
        return NotifyResponse(success=False, error=str(e))


@mcp.tool()
async def signup_user(email: str, password: str, base_url: str = DEFAULT_BASE_URL) -> str:
    """
    Register a new user with the MockNotifyService and receive an API key.
    
    Args:
        email: User's email address
        password: User's password
        base_url: Base URL of the MockNotifyService (optional)
    
    Returns:
        JSON string with user creation response including API key
    """
    data = {"email": email, "password": password}
    result = await make_request("POST", "/api/signup", data=data, base_url=base_url)
    
    if result.success:
        return json.dumps(result.data, indent=2)
    else:
        return json.dumps({"error": result.error, "status_code": result.status_code}, indent=2)


@mcp.tool()
async def create_service(name: str, api_key: str, description: str = "", base_url: str = DEFAULT_BASE_URL) -> str:
    """
    Create a new service linked to the user's API key.
    
    Args:
        name: Service name
        api_key: User's API key from signup
        description: Service description (optional)
        base_url: Base URL of the MockNotifyService (optional)
    
    Returns:
        JSON string with service creation response
    """
    data = {"name": name, "description": description}
    result = await make_request("POST", "/api/services", api_key=api_key, data=data, base_url=base_url)
    
    if result.success:
        return json.dumps(result.data, indent=2)
    else:
        return json.dumps({"error": result.error or result.data, "status_code": result.status_code}, indent=2)


@mcp.tool()
async def get_services(api_key: str, base_url: str = DEFAULT_BASE_URL) -> str:
    """
    Get all services for the authenticated user.
    
    Args:
        api_key: User's API key
        base_url: Base URL of the MockNotifyService (optional)
    
    Returns:
        JSON string with list of user's services
    """
    result = await make_request("GET", "/api/services", api_key=api_key, base_url=base_url)
    
    if result.success:
        return json.dumps(result.data, indent=2)
    else:
        return json.dumps({"error": result.error or result.data, "status_code": result.status_code}, indent=2)


@mcp.tool()
async def create_template(
    name: str, 
    subject: str, 
    body: str, 
    service_id: str, 
    api_key: str, 
    base_url: str = DEFAULT_BASE_URL
) -> str:
    """
    Create a message template linked to a service.
    
    Args:
        name: Template name
        subject: Email subject line
        body: Message body content
        service_id: ID of the service to link the template to
        api_key: User's API key
        base_url: Base URL of the MockNotifyService (optional)
    
    Returns:
        JSON string with template creation response
    """
    data = {
        "name": name,
        "subject": subject,
        "body": body,
        "service_id": service_id
    }
    result = await make_request("POST", "/api/templates", api_key=api_key, data=data, base_url=base_url)
    
    if result.success:
        return json.dumps(result.data, indent=2)
    else:
        return json.dumps({"error": result.error or result.data, "status_code": result.status_code}, indent=2)


@mcp.tool()
async def get_templates(api_key: str, base_url: str = DEFAULT_BASE_URL) -> str:
    """
    Get all templates for the authenticated user's services.
    
    Args:
        api_key: User's API key
        base_url: Base URL of the MockNotifyService (optional)
    
    Returns:
        JSON string with list of user's templates
    """
    result = await make_request("GET", "/api/templates", api_key=api_key, base_url=base_url)
    
    if result.success:
        return json.dumps(result.data, indent=2)
    else:
        return json.dumps({"error": result.error or result.data, "status_code": result.status_code}, indent=2)


@mcp.tool()
async def send_email_notification(
    template_id: str, 
    recipient_email: str, 
    api_key: str, 
    base_url: str = DEFAULT_BASE_URL
) -> str:
    """
    Send an email notification using a template.
    
    Args:
        template_id: ID of the template to use
        recipient_email: Email address of the recipient
        api_key: User's API key
        base_url: Base URL of the MockNotifyService (optional)
    
    Returns:
        JSON string with email sending response including message ID
    """
    data = {
        "template_id": template_id,
        "recipient_email": recipient_email
    }
    result = await make_request("POST", "/api/notifications/email", api_key=api_key, data=data, base_url=base_url)
    
    if result.success:
        return json.dumps(result.data, indent=2)
    else:
        return json.dumps({"error": result.error or result.data, "status_code": result.status_code}, indent=2)


@mcp.tool()
async def send_sms_notification(
    template_id: str, 
    recipient_phone: str, 
    api_key: str, 
    base_url: str = DEFAULT_BASE_URL
) -> str:
    """
    Send an SMS notification using a template.
    
    Args:
        template_id: ID of the template to use
        recipient_phone: Phone number of the recipient (e.g., +1234567890)
        api_key: User's API key
        base_url: Base URL of the MockNotifyService (optional)
    
    Returns:
        JSON string with SMS sending response including message ID
    """
    data = {
        "template_id": template_id,
        "recipient_phone": recipient_phone
    }
    result = await make_request("POST", "/api/notifications/sms", api_key=api_key, data=data, base_url=base_url)
    
    if result.success:
        return json.dumps(result.data, indent=2)
    else:
        return json.dumps({"error": result.error or result.data, "status_code": result.status_code}, indent=2)


@mcp.tool()
async def get_message_status(message_id: str, api_key: str, base_url: str = DEFAULT_BASE_URL) -> str:
    """
    Get the delivery status of a previously sent message.
    
    Args:
        message_id: ID of the message to check
        api_key: User's API key
        base_url: Base URL of the MockNotifyService (optional)
    
    Returns:
        JSON string with message status information
    """
    result = await make_request("GET", f"/api/messages/{message_id}/status", api_key=api_key, base_url=base_url)
    
    if result.success:
        return json.dumps(result.data, indent=2)
    else:
        return json.dumps({"error": result.error or result.data, "status_code": result.status_code}, indent=2)


@mcp.tool()
async def get_messages(api_key: str, base_url: str = DEFAULT_BASE_URL) -> str:
    """
    Get all messages for the authenticated user.
    
    Args:
        api_key: User's API key
        base_url: Base URL of the MockNotifyService (optional)
    
    Returns:
        JSON string with list of user's messages
    """
    result = await make_request("GET", "/api/messages", api_key=api_key, base_url=base_url)
    
    if result.success:
        return json.dumps(result.data, indent=2)
    else:
        return json.dumps({"error": result.error or result.data, "status_code": result.status_code}, indent=2)


@mcp.tool()
async def health_check(base_url: str = DEFAULT_BASE_URL) -> str:
    """
    Check the health status of the MockNotifyService.
    
    Args:
        base_url: Base URL of the MockNotifyService (optional)
    
    Returns:
        JSON string with service health information
    """
    result = await make_request("GET", "/api/health", base_url=base_url)
    
    if result.success:
        return json.dumps(result.data, indent=2)
    else:
        return json.dumps({"error": result.error or result.data, "status_code": result.status_code}, indent=2)


if __name__ == "__main__":
    mcp.run(transport='stdio')