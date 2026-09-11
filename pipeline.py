import requests
import json

url = "https://api.github.com/repos/mitre-attack/attack-stix-data"
response = requests.get(url)
print(response.status_code)


#print(data.keys())

#print(json.dumps(data,indent = 4))

if response.status_code == 200:
    data = response.json()
    result = {
    "repository": data["name"],
    "description": data["description"],
    "stars": data["stargazers_count"],
    "open_issues": data["open_issues_count"]
}
    #print(result)
    with open("result.txt","w") as file:
        json.dump(result,file,indent = 4)
else:
    print("Request failed:", response.status_code)