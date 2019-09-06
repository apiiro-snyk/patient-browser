import requests

patientIds = ["8d6b016c-52a4-47b2-a264-b2c784cd1b24", "5fe6f055-ebf9-4ffb-959a-dd2f5351b9ac", "124927e1-4834-43fd-ac65-449d7e5bd270", "23c8bcf2-86dd-4ebf-a044-87651384b83f", "74aa95c2-368a-40d7-ab9d-bc28d1d8c95b", "beea6175-6799-4c7f-8105-03d0fd174f77", "31c544a7-5c48-4e88-8c29-6f8f107513b0", "26bd9767-49d8-4131-9dc5-465e18cf88c6", "3fc67aa4-99a9-432f-8d5a-41ada0318c0d", "2f4a1186-a902-4f8c-8c15-0f0cc40af821", "smart-967332"]
for patientId in patientIds:
    url = f"http://localhost:8080/baseDstu3/Patient/{patientId}/$meta-add"

    payload = "{\n    \"resourceType\": \"Parameters\",\n    \"parameter\": [\n        {\n            \"name\": \"meta\",\n            \"valueMeta\": {\n                \"tag\": [\n                    {\n                        \"system\": \"https://smarthealthit.org/tags\",\n                        \"code\": \"AtRiskCoronaryHeartDisease\"\n                    }\n                ]\n            }\n        }\n    ]\n}"
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
