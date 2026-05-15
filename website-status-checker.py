import requests
import time

url = input("Enter website URL: ")

try:
    start = time.time()

    response = requests.get(url)

    end = time.time()
    response_time = end - start

    if response.status_code == 200:
        print("Status: Online ✅")
        print("Response Time:", round(response_time, 2), "seconds")
    else:
        print("Website returned status code:", response.status_code)

except requests.exceptions.RequestException:
    print("Status: Website is unreachable ❌")