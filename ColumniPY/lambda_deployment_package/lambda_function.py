import jwt
import json

def handler(event, context):
    # Check if 'authorizationToken' is present in the event dictionary
    if 'authorizationToken' not in event:
        return {
            'statusCode': 400,
            'body': 'Missing authorizationToken in the request.'
        }

    token = event['authorizationToken']
    try:
        decoded = jwt.decode(token, 'cc-columni-23', algorithms=['HS256'])
        principalId = decoded['sub']
        policyDocument = {
            'Version': '2023-12-01',
            'Statement': [{
                'Action': 'execute-api:Invoke',
                'Effect': 'Allow',
                'Resource': event['methodArn']
            }]
        }
    except jwt.ExpiredSignatureError:
        principalId = 'unauthorized'
        policyDocument = {
            'Version': '2023-12-01',
            'Statement': [{
                'Action': 'execute-api:Invoke',
                'Effect': 'Deny',
                'Resource': event['methodArn']
            }]
        }
    except jwt.InvalidTokenError:
        principalId = 'unauthorized'
        policyDocument = {
            'Version': '2023-12-01',
            'Statement': [{
                'Action': 'execute-api:Invoke',
                'Effect': 'Deny',
                'Resource': event['methodArn']
            }]
        }

    # CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    }

    return {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps({
            'principalId': principalId,
            'policyDocument': policyDocument
        })
    }


