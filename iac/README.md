# iac-lambda-data-receiver

## Description
This project contains all CloudFormation Stacks, responsible to create and setup the application environmet and deploy the appliction.

### What it is created?
You can read the documentations about each stack.

- Stack: S3
  - Template: [iac-s3.yml](./iac-s3.yml)
  - Documentation: [IAC-S3.md](./docs/IAC-S3.md)
- Stack: DynamoDB
  - Template: [iac-dynamodb.yml](./iac-dynamodb.yml)
  - Documentation: [IAC-DYNAMODB.md](./docs/IAC-DYNAMODB.md)
- Stack: Lambda
  - Template: [iac-lambda.yml](./iac-lambda.yml)
  - Documentation: [IAC-LAMBDA.md](./docs/IAC-LAMBDA.md)
- Stack: Application Load Balancer
  - Template: [iac-alb.yml](./iac-alb.yml)
  - Documentation: [IAC-ALB.md](./docs/IAC-ALB.md)

## How to run
Read the main documentation [README.md](../README.md), section *How to use*.