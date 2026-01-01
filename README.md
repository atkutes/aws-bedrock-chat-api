# AWS Bedrock ChatBot

A fully functional AI-powered chatbot using **AWS Lambda**, **API Gateway**, and **Amazon Bedrock Titan Text Express v1**.

This project demonstrates how to deploy a **serverless AI application** using AWS managed LLM services. The chatbot responds to user input in real-time and can easily be integrated into web or mobile applications.

---

## Features

- **Serverless architecture**: No EC2 instances required – just AWS Lambda functions.
- **Real-time AI responses**: `/chat` endpoint handles user messages and returns AI-generated replies.
- **Easy integration**: Tested via `curl` and ready for further development.
- **GitHub-ready**: Complete source code available.

---

## Architecture

1. **AWS Lambda**: Handles incoming requests and calls Amazon Bedrock to generate responses.
2. **API Gateway**: Provides a public endpoint (`/chat`) for HTTP POST requests.
3. **Amazon Bedrock**: Titan Text Express v1 model generates AI text responses.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/atkutes/aws-bedrock-chat-api
cd aws-bedrock-chatbot

## Configuration Notes

Model ID: amazon.titan-text-express-v1 (ensure your AWS account has access)

Region: us-east-1

Timeout: 15 seconds (adjust if needed for longer responses)

Max Tokens: 256 (adjust for longer AI responses)