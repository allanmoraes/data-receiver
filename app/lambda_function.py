import os
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['DYNAMODB_TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])

        required_fields = ['name', 'email']
        for field in required_fields:
            if field not in data:
                return {
                    'statusCode': 400,
                    'body': json.dumps(f'The field "{field}" is required.')
                }

        if not isinstance(data['name'], str) or not isinstance(data['email'], str):
            return {
                'statusCode': 400,
                'body': json.dumps('The fields "name" and "email" should be string type.')
            }

        table.put_item(Item=data)

        return {
            'statusCode': 200,
            'body': json.dumps('Success! Data have been included.')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Something went wrong: {str(e)}')
        }