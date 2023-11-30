# dynamodb-lambda-data-receiver

## Description:

This CloudFormation Templete creates and setup the DynamoDB Table. 

What it is created?

- One DynamoDB Table

---
## Parameters

This template are parametrized

- **EnvironmentName:** The environment's name
  - **Default:** production
- **DynamoDBTableName:** The DynamoDB's Table name
  - **Default:** persons
- **OwnerTeam:** Name of the team responsible for maintaining this template and the infrastructure on AWS
  - **Default:** development
- **Project:** URL's git project
  - **Default:** https://github.com/allanmoraeslambda-data-receiver  

---

## How to run
Read the main documentation [README.md](../README.md), section *How to use*.

---

## Outputs

This template has outputs and this outputs can be used by anothe Stack.

- **DataReceiverDynamoDBTable:** A reference to the created DynamoDB's table name 
- **DataReceiverDynamoDBTableARN:** A reference to the created DynamoDB's table ARN


| Key                          | Value                                                 | Description                               | Export name                                                 |
|------------------------------|-------------------------------------------------------|-------------------------------------------|-------------------------------------------------------------|
| DataReceiverDynamoDBTable    | persons                                               | A reference to the created DynamoDB table | dynamodb-lambda-data-receiver-DataReceiverDynamoDBTableName |
| DataReceiverDynamoDBTableARN | arn:aws:dynamodb:us-east-2:123456:table/persons | A reference to the created DynamoDB table | dynamodb-lambda-data-receiver-DataReceiverDynamoDBTableARN  |