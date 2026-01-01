# AWS Bedrock Chat API

Serverless AI Chat API built with AWS Lambda, API Gateway, and Amazon Bedrock.

## Tech Stack
- AWS Lambda (Python)
- Amazon API Gateway
- Amazon Bedrock (Claude)

## Endpoint
POST /chat

## Example Request
```json
{
  "message": "What is AWS Lambda?"
}

## Example Response
{
  "reply": "AWS Lambda is a serverless compute service..."
}
