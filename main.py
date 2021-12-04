import requests
print("CODE FROM github.com/z1c3/location")
githubsuyh = input("Your github token:")
githuborgname = input("Your github org name:")
location = input("Your desired custom location:")
headers = {f'Authorization': 'bearer {githubauthtoklen}'}

data = {
    'location': location
}

r = requests.post(f"https://api.github.com/orgs/{githuborgname}", headers=headers, data=data)
a = r.json()
print(a)