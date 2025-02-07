import threading
import httpx
import time
import json
from concurrent.futures import ThreadPoolExecutor
from config import NUM_URLS, TEST_URL

urls = [TEST_URL] * NUM_URLS

def fetch(url):
    with httpx.Client() as client:
        response = client.get(url)
        data = response.text
        return json.loads(data)  # Simulate CPU-bound JSON parsing

start = time.time()

# Replace manual thread creation with ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=12) as executor:
    results = list(executor.map(fetch, urls))

end = time.time()
print(f"Multithreading Time: {end - start:.2f} seconds")