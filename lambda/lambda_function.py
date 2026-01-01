import json
import boto3

bedrock = boto3.client(
    service_name="bedrock_runtime",
    region_name="us-east-1"
)

def lambda_handler(evet, context):
    body = json.loads(event["body"])
    message = body.get("message")

prompt =  prompt = f"""
    You are a helpful AI assistant.
    User: {message}
    Assistant:
    """

    response = bedrock.invoke_model(
        modelId="anthropic.claude-v2",
        body=json.dumps({
            "prompt": prompt,
            "max_tokens_to_sample": 300,
            "temperature": 0.7
        }),
        contentType="application/json",
        accept="application/json"
    )

    result = json.loads(response["body"].read())
    answer = result["completion"]

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"reply": answer})
    }
