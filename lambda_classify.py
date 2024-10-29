import json
import boto3
import base64

runtime = boto3.client('runtime.sagemaker')
ENDPOINT = "image-classification-2024-10-28-20-25-29-037"

def lambda_handler(event, context):
    try:
        # Get image data directly from event
        image_data = event['image_data']
        
        # Decode the base64 image data
        image = base64.b64decode(image_data)
        
        # Make prediction using boto3
        response = runtime.invoke_endpoint(
            EndpointName=ENDPOINT,
            ContentType='image/png',
            Body=image
        )
        
        # Get the results and convert to list of floats
        inferences = response['Body'].read().decode('utf-8')
        inferences = json.loads(inferences)  # Convert string to list
        
        # Return results
        return {
            'statusCode': 200,
            'body': {
                'image_data': image_data,
                's3_bucket': event['s3_bucket'],
                's3_key': event['s3_key'],
                'inferences': inferences 
            }
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }