# lambda-data-receiver

## Description
This project has all components to deploy an application in AWS.
- **app:** This directory contains the application code. Here is the documentation [README.md](./app/README.md)
- **iac:** This directory contains the CloudFormation templates. Here is the documentation [README.md](./iac/README.md)

### What it is created?
Using this project, you will create this itens:

- One S3 Bucket
- One DynamoDB Table
- One Lambda Function
- One Application Load Balancer
- All Rules, Policies and SecurityGroups
- An Python application, used to receive data and insert into the DynamoDB Table.

---
## How to use
There is a shell scrit in this repo, create to help the creation and deploy.

First, you have configure the AWS Cli and give execution permissions to this script.

```bash
root@ubuntu:lambda-data-receiver$ chmod +x deploy
```

### To create all Stacks and deploy the application:
This option will create all infraestructure, upload and deploy the Python application.
```bash
root@ubuntu:lambda-data-receiver$ ./deploy all
```

### To deploy/update the application:
This option will crate a zip file of the Python application, upload to S3 Bucket and update the Lambda function with the new code.
```bash
root@ubuntu:lambda-data-receiver$ ./deploy update-app
```

### Other options:
This script has another options, if you desire to change a especific item.
```bash
root@ubuntu:lambda-data-receiver$ ./deploy
You can use:
        deploy all: To create the AWS components and deploy the application.

        deploy update-app: To upload and update your application.

        deploy update-s3: To update only the S3 Stack

        deploy update-dynamodb: To update only the DynamoDB Stack

        deploy update-alb: To update only the ALB Stack

        deploy update-lambda-configuration: To update only the Lambda Stack
```

## Manual deploy
You can deploy without the script, using *aws cloudformation* command line. Follow the instructions:

### Create the S3 Stack:
```bash
root@ubuntu:lambda-data-receiver$ aws cloudformation deploy \
    --template-file iac/iac-s3.yml \
    --stack-name s3-data-receiver
```

### Create the DynamoDB Stack:
```bash
root@ubuntu:lambda-data-receiver$ aws cloudformation deploy \
    --template-file iac/iac-dynamodb.yml \
    --stack-name dynamodb-data-receiver
```

### Upload the Python application to S3:
```bash
root@ubuntu:lambda-data-receiver$ cd app

root@ubuntu:lambda-data-receiver/app$ zipname="latest-"$(date +'%Y%m%d%H%M%S')

root@ubuntu:lambda-data-receiver/app$ echo "S3Key=production/python/$zipname.zip" > ../iac/application.parameter

root@ubuntu:lambda-data-receiver/app$ zip -r $zipname.zip lambda_function.py

root@ubuntu:lambda-data-receiver/app$ aws s3 cp $zipname.zip s3://lambda-data-receiver/production/python/

root@ubuntu:lambda-data-receiver/app$ cd ..
```

### Create the Lambda Stack:
```bash
root@ubuntu:lambda-data-receiver$ param=$(cat iac/application.parameter)

root@ubuntu:lambda-data-receiver$ aws cloudformation deploy \
    --capabilities CAPABILITY_NAMED_IAM \
    --template-file iac/iac-lambda.yml --stack-name lambda-data-receiver \
    --parameter-overrides $param
```

### Create the ALB Stack and shows the URL
```bash
root@ubuntu:lambda-data-receiver$ aws cloudformation deploy \
    --capabilities CAPABILITY_NAMED_IAM \
    --template-file iac/iac-alb.yml \
    --stack-name alb-data-receiver

root@ubuntu:lambda-data-receiver$ aws cloudformation describe-stacks \
        --query 'Stacks[?StackName==`alb-data-receiver`][].Outputs[?OutputKey==`DNSName`].OutputValue' \
        --output text
```