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

