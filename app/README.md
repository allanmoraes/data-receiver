# data-receiver

```json
{
  "id": 123,
  "client": "Nome do Cliente",
  "technology": "Tecnologia Utilizada",
  "automated": true
}
```

```bash
curl -X POST -H "Content-Type: application/json" -d '{"id": 123, "client": "Nome do Cliente", "technology": "Tecnologia Utilizada", "automated": true}' https://your-api-endpoint.execute-api.us-east-1.amazonaws.com/your-resource
```

```Python
import requests
import json

url = 'https://your-api-endpoint.execute-api.us-east-1.amazonaws.com/your-resource'
data = {"id": 123, "client": "Nome do Cliente", "technology": "Tecnologia Utilizada", "automated": true}

headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.status_code)
print(response.json())
```