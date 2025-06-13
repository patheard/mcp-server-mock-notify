module "mcp_server_mock_notify" {
  source    = "github.com/cds-snc/terraform-modules//lambda?ref=v10.5.1"
  name      = "mcp_server_mock_notify"
  ecr_arn   = aws_ecr_repository.mcp_server_mock_notify.arn
  image_uri = "${aws_ecr_repository.mcp_server_mock_notify.repository_url}:latest"

  memory        = 1024
  timeout       = 10
  architectures = ["arm64"]

  environment_variables = {
    DEFAULT_BASE_URL = "https://notify.ai-jam.cdssandbox.xyz"
  }

  billing_tag_value = "mcp_server_mock_notify"
}

resource "aws_lambda_function_url" "mcp_server_mock_notify" {
  function_name      = module.mcp_server_mock_notify.function_name
  authorization_type = "NONE"
}
