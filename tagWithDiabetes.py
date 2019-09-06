import requests

patientIds = ["smart-1627321", "smart-1685497", "smart-1796238", "smart-1869612", "smart-767980", "smart-967332"]
for patientId in patientIds:
    url = f"http://localhost:8080/baseDstu3/Patient/{patientId}/$meta-add"

    payload = "{\n    \"resourceType\": \"Parameters\",\n    \"parameter\": [\n        {\n            \"name\": \"meta\",\n            \"valueMeta\": {\n                \"tag\": [\n                    {\n                        \"system\": \"https://smarthealthit.org/tags\",\n                        \"code\": \"AtRiskDiabetes\"\n                    }\n                ]\n            }\n        }\n    ]\n}"
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
