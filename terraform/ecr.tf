resource "aws_ecr_repository" "mcp_server_mock_notify" {
  name                 = "mcp-server-mock-notify"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
