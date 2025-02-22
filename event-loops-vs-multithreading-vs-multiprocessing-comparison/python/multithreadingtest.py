import threading
import httpx
import time
import json
from config import NUM_URLS, TEST_URL

urls = [TEST_URL] * NUM_URLS

def fetch(url):
    with httpx.Client() as client:
        response = client.get(url)
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