import math
import requests
print(math.sqrt(144))

result=math.sin(math.pi*2)
print(result)

response=requests.get("https://api.github.com")
print(response.status_code)