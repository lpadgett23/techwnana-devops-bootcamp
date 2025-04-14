import requests

response = requests.get("https://api.github.com/repos/lpadgett23/techwnana-devops-bootcamp/issues")
# print(response.text)
# print(response.json)
# print(type(response.json))
# print(response.json()[0])

my_repo_issues = response.json()

for issue in my_repo_issues:
    print(f"Description of Issue: {issue['title']}\n Status: {issue['state']}\n")

