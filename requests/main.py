import requests

website = "https://jsonplaceholder.typicode.com/posts/1"
print(requests.get(website).json())

response = requests.put(website, data={
    "id": 1,
    "userid":12,
    "title": "my new post",
    "body": "body for my post DZ"

})

print(response.json())