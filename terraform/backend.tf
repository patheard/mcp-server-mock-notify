terraform {
  backend "s3" {
    bucket        = "ai-jam-session-mock-service-tf"
    key           = "mcp-server-mock-notify/terraform.tfstate"
    region        = "ca-central-1"
    use_lockfile  = true
  }
}