import threading
import requests
import time
import json

urls = ["https://jsonplaceholder.typicode.com/todos/1"] * 10000

def fetch(url):
    response = requests.get(url)
    data = response.text
    return json.loads(data)  # Simulate CPU-bound JSON parsing

threads = []
start = time.time()

for url in urls:
    thread = threading.Thread(target=fetch, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()
print(f"Multithreading Time: {end - start:.2f} seconds")