import json
import boto3

bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    message = body.get("message", "")

    prompt_text = f"You are a helpful assistant.\nUser: {message}\nAssistant:"

    response = bedrock.invoke_model(
        modelId="amazon.titan-text-express-v1",
        body=json.dumps({
            "inputText": prompt_text,
            "textGenerationConfig": {
                "maxTokenCount": 256,
                "temperature": 0.7,
                "topP": 0.9,
                "stopSequences": []
            }
        }),
        contentType="application/json",
        accept="application/json"
    )

    body_response = response["body"].read()
    result = json.loads(body_response)

    reply = ""
    if "results" in result and len(result["results"]) > 0:
        reply = result["results"][0].get("outputText", "").strip()

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"reply": reply})
    }

