# s3-lambda-data-receiver

## Description:

This CloudFormation Templete creates and setup the Application Load Balancer.

What it is created?

- One ALB
- One TargetGroup
- One Listener
- One Listener Rule
- One SecurityGroup
- Setup permission to invoke Lambda Function

---
## Parameters

This template are parametrized

- **LoadBalancerName:** ALB's name
  - **Default:** lambda-data-receiver-alb
- **NetworkStackName:** The Network's stack name
  - **Default:** Network
- **LambdaStackName:** The Lambda's stack name
  - **Default:** lambda-data-receiver
- **SecurityGroupName:** The SecurityGroup's name
  - **Default:** alb-lambida-data-receiver-sg
- **EnvironmentName:** The environment's name
  - **Default:** production
- **OwnerTeam:** Name of the team responsible for maintaining this template and the infrastructure on AWS
  - **Default:** development
- **Project:** URL's git project
  - **Default:** https://github.com/allanmoraeslambda-data-receiver


---

## How to run
Read the main documentation [README.md](../README.md), section *How to use*.

---

## Outputs

- **DNSName:** The ALB's endpoint.


| Key                | Value                                                                          | Description            | Export name                             |
|--------------------|--------------------------------------------------------------------------------|------------------------|-----------------------------------------|
| DNSName  | http://alb-da-LoadB-URL.elb.amazonaws.com | The ALB's endpoint | -----------  |