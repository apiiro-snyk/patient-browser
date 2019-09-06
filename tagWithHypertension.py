import requests

patientIds = ["b365487f-bfd0-4b2b-ae89-6593f2d89a40", "c88fe185-f98a-4f0d-aabb-c7186e1a4983", "182b1237-d1f0-4bcf-bbf2-1229b596c9ab", "4df8cc40-a014-4e5c-9589-5598dba0681a", "0bca8fbb-a8cd-40bd-8097-cea950689d5a", "b40a7118-c112-4418-86fe-363e5f46620eMRN:", "41291a8a-85e8-4693-a0ba-403b6c2342f5", "7bfb199e-f281-4dc9-aac5-61618cb87bae", "4d5a0f44-e66e-4e53-ac4b-59bfcce6dd5b", "f8f75fb0-c43c-4149-a2f0-4e3c86c9ac94", "30e0da54-48fa-436d-bb7f-429f4ae91273", "dd3ed0d9-9996-43f5-8c1f-4bcbcbd0479c", "f7f6af15-da04-4093-85a1-bb3c410fc7dd", "82cec34b-9acf-4661-876b-6439c435272e", "012ba221-a591-4400-b60e-70d52043073e", "1f5cdfc7-6a03-4a93-93a4-520bde22ae4f", "cbe4a148-b012-4576-8c95-7df3f2eb2c96", "19381553-7516-4ae0-ba2f-43396d38dc33", "33e755e0-7e2d-4fb7-88e8-3a081148eec4", "04284e67-54b1-44cf-a5ae-8fa60e5895a5", "81e3e0eb-f1ac-4160-9f5a-3f2af67b7579", "7b135ced-47d9-4fe5-b4a8-96558dc25441", "9cc921fb-125b-4aa7-b9c1-594c77a0e791", "dfa10832-62db-4d35-b310-74b25b958196", "1aa1522b-ac57-44fd-b9bb-a964632ade49"]
for patientId in patientIds:
    url = f"http://localhost:8080/baseDstu3/Patient/{patientId}/$meta-add"

    payload = "{\n    \"resourceType\": \"Parameters\",\n    \"parameter\": [\n        {\n            \"name\": \"meta\",\n            \"valueMeta\": {\n                \"tag\": [\n                    {\n                        \"system\": \"https://smarthealthit.org/tags\",\n                        \"code\": \"AtRiskHypertension\"\n                    }\n                ]\n            }\n        }\n    ]\n}"
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
