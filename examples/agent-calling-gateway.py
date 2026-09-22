from mcp_proxy_for_aws.client import aws_iam_streamablehttp_client
from mcp import MCPClient
service = "bedrock-agentcore"
region = "us-east-1"
mcp_url = "https://gateway-quick-start-0b2449-r4gz2tbqep.gateway.bedrock-agentcore.us-east-1.amazonaws.com/mcp"
mcp_client_factory = lambda: aws_iam_streamablehttp_client(
    endpoint=mcp_url,    # The URL of the MCP server
    aws_region=region,   # The region of the MCP server
    aws_service=service  # The underlying AWS service, e.g. "bedrock-agentcore"
)

with MCPClient(mcp_client_factory) as mcp_client:
    mcp_tools = mcp_client.list_tools_sync()
    agent = Agent(tools=[mcp_tools])
    agent("How to create a pet?")
