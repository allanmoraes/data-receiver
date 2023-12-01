# dynamodb-lambda-data-receiver

## Description:

This CloudFormation Templete creates and setup Lambda Function. 

What it is created?

- One Lambda Function
- Role and policies

---
## Parameters

This template are parametrized

- **NetworkStackName:** The Network's stack name
  - **Default:** Network
- **S3BucketStackName:** The S3's stack name
  - **Default:** s3-lambda-data-receiver
- **DynamoDBStackName:** The DynamoDB's stack name
  - **Default:** dynamodb-lambda-data-receiver
- **EnvironmentName:** The environment's name
  - **Default:** production
- **OwnerTeam:** Name of the team responsible for maintaining this template and the infrastructure on AWS
  - **Default:** development
- **Project:** URL's git project
  - **Default:** https://github.com/allanmoraeslambda-data-receiver
- **S3Key:** S3 key which contains the Python application. There isn't a default value, you have to populate this variable when deploy.
- **LambdaFunctionName:** The Lambda's name
  - **Default:** lambda-data-receiver
- **LambdaSecurityGroupName:** The SecurityGroup's name
  - **Default:** lambda-data-receiver-sg
- **LambdaExecutionRoleName:** The Role's name.
  - **Default:** lambda-data-receiver-role

---

## How to run
Read the main documentation [README.md](../README.md), section *How to use*.

---

## Outputs

- **LambdaFunctionName:** 'Lambda Function's name'
- **LambdaFunctionArn:** 'Lambda Function's ARN'

| Key                | Value                                                                          | Description            | Export name                             |
|--------------------|--------------------------------------------------------------------------------|------------------------|-----------------------------------------|
| LambdaFunctionArn  | arn:aws:lambda:us-east-2:12345:function:production-lambda-data-receiver | Lambda Function's ARN | lambda-data-receiver-LambdaFunctionArn  |
| LambdaFunctionName | production-lambda-data-receiver                                                | Lambda Function's name | lambda-data-receiver-LambdaFunctionName |