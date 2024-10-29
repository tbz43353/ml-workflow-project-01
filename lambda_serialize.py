import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # DONE implement
    # Get the s3 address from the Step Function event input
    key = event['s3_key']
    bucket = event['s3_bucket']
    
    # Download the data from s3 to /tmp/image.png
    s3.download_file(bucket, key, '/tmp/image.png')
    
    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data.decode('utf-8'),  # Convert bytes to string for JSON serialization
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }