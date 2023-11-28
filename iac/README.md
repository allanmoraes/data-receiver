
```bash
aws cloudformation create-stack --stack-name s3-data-receiver-app --capabilities CAPABILITY_NAMED_IAM --template-body file
://iac/iac-s3-app.yml
```

```bash
aws s3 cp ../ZIPFILE s3://S3BucketAppName/production/python/
```

```bash
aws cloudformation update-stack --stack-name dynamodb-data-receiver-app --capabilities CAPABILITY_NAMED_IAM --template-bod
y file://iac/iac-dynamodb.yml
```