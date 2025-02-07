from multiprocessing import Pool
import requests
import time
import json

urls = ["https://jsonplaceholder.typicode.com/todos/1"] * 10000

def fetch(url):
    response = requests.get(url)
    data = response.text
    return json.loads(data)  # Simulate CPU-bound JSON parsing


if __name__ == '__main__':
    start = time.time()
    with Pool(12) as pool:  # Use 4 processes
        results = pool.map(fetch, urls)

    end = time.time()
    print(f"Multiprocessing Time: {end - start:.2f} seconds")