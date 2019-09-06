import requests

patientIds = ["00cb2782-fa11-47b5-bf03-5feabd37918a", "d52b2971-23af-4b8c-adf6-f6e00874012b", "7807a02f-57c9-4bd8-8f3b-6c39b08f9b1e", "84c25364-654b-4fc3-b70d-ff4cf271e66c", "95b7791e-28f8-4352-98ed-02cda4883d29", "055bb26f-4b2b-4d2e-8565-ac586566045f", "33c208e1-fe69-48ee-9443-355cd451d4b5", "fa6b8e38-5372-4d2b-91e2-86484af55e31", "c38e31fc-c704-4ade-85f3-c8b66a07fa60", "ded22492-0979-49fe-9daf-79a88d7cc08b", "4c399f55-347b-48ed-859b-af598b86d80a", "ac19525d-013e-4817-ad47-5e5831df6811", "2ad53e05-d637-4dfc-8eba-a30adc6c43b8", "e5a4c695-9ede-4db4-ba50-46c7f26d7cca", "78481466-85cc-419f-bc28-1521d1bdd4e2", "c10e6039-cd50-4370-831f-dbf51cdff145", "15c97586-ed5f-481e-b8ec-a06435ae22de", "047b3aef-fe06-46c4-bc32-18a294872f32", "eeeace5e-3547-463f-9f71-e9925d8aa72a", "05f8d2f9-0790-4d76-9048-c09b2493c998", "15fe27c1-bf9d-4dc7-9301-a70587fb0f60", "3f27c752-3142-4e67-bd64-4f4d4f2f2b40", "3cdcd228-174d-47b4-ac4f-e905c7ec7ac8", "smart-1577780", "smart-8888802"]
for patientId in patientIds:
    url = f"http://localhost:8080/baseDstu3/Patient/{patientId}/$meta-add"

    payload = "{\n    \"resourceType\": \"Parameters\",\n    \"parameter\": [\n        {\n            \"name\": \"meta\",\n            \"valueMeta\": {\n                \"tag\": [\n                    {\n                        \"system\": \"https://smarthealthit.org/tags\",\n                        \"code\": \"AtRiskAsthmatics\"\n                    }\n                ]\n            }\n        }\n    ]\n}"
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
