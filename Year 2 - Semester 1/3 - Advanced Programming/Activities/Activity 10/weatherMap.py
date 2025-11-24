import requests

city = "Dubai"
key = "c2818a5a2fd26aa5fa49daea5a13a59e"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

response = requests.get(url)

if response.status_code == 200 :
    print("Successfully retrieved data.")
else :
    print("Failed to retrieve data. Status code:", response.status_code)