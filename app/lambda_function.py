import os
import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name=os.environ['AWS_REGION'])
table_name = os.environ['DYNAMODB_TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])

        required_fields = ['id', 'client', 'technology', 'automated']
        for field in required_fields:
            if field not in data:
                return {
                    'statusCode': 400,
                    'body': json.dumps(f'O campo "{field}" é obrigatório.')
                }

        if not isinstance(data['id'], int):
            return {
                'statusCode': 400,
                'body': json.dumps('O campo "id" deve ser um número inteiro.')
            }
        if not isinstance(data['client'], str) or not isinstance(data['technology'], str):
            return {
                'statusCode': 400,
                'body': json.dumps('Os campos "client" e "technology" devem ser strings.')
            }
        if not isinstance(data['automated'], bool):
            return {
                'statusCode': 400,
                'body': json.dumps('O campo "automated" deve ser um booleano.')
            }

        table.put_item(Item=data)

        return {
            'statusCode': 200,
            'body': json.dumps('Dados inseridos com sucesso.')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Ocorreu um erro: {str(e)}')
        }