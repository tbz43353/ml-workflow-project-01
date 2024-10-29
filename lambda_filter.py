import json


THRESHOLD = .90


def lambda_handler(event, context):
    
    # Grab the inferences from the event
    # The inferences are already in list format
    inferences = event['inferences']
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = max(inferences) > THRESHOLD
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        return {
            'statusCode': 200,
            'body': event
        }
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")
        