# Summary

```
"Write a summary discussing your more relevant options in developing the assignment"
```

## My thoughts on task development:
I found it quite challenging in some aspects and interesting, allowing for the testing of various skills and providing the freedom for deployment. I felt comfortable during execution, even with some challenges, and I tried my best to adhere to each stipulated rule.

---

## Development choices:

- **CloudFormation:** I chose CloudFormation as the automation tool, as I hadn't worked with it before and it was one of the desired options. I could have used Terraform, but it wouldn't have been as challenging.

- **Python:** I followed the recommendation to use Python as the programming language, which I am somewhat accustomed to. I have used it in other instances for automation.

- **Lambda:** I decided to use Lambda to host the applications. I saw no need to spin up an EC2, let alone an EKS, as it is a small and specific application. This reduced the implementation difficulty and future environment maintenance.

- **ALB:** My initial idea was to use API Gateway, but besides complicating the implementation, it would have incurred costs. So, I opted to create an ALB to avoid exposing Lambda directly to the internet.

- **DynamoDB:** I chose this database because it works well with JSON objects and offers greater flexibility.

- **EventBridge Scheduler:** It was the best way I found to schedule Lambda executions for data collection. It's a native AWS solution and easy to work with.

I tried to keep the documentation as simple as possible while also making it concise and easy to understand. I documented all the items that I consider important for the use of the repositories and automation.