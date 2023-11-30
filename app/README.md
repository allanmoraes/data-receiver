# lambda-data-receiver

## Description
This Python application receives a JSON data and insert into DynamoDB Table.

It runs in Python 3.8 or higher.

The table name is setup in a Lambda Function as environment variable.

CI/CD idea: [CICD.md](./CICD.md)

---

## How to use
```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name": "allan", "email": "email@aws.com"}' \
  http://alb-da-LoadB-URL.elb.amazonaws.com
```
---
## How to deploy
Read the main documentation [README.md](../README.md), section *To deploy/update the application*.