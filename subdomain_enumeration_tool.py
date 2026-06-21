import requests 
import threading

domain = 'youtube.com'
with open('subdomains.txt', 'r') as file:
    subdomains = file.read().splitlines()

discovered_subdomains = []

lock = threading.Lock() 
def check_subdomain(subdomain):
    url = f'http://{subdomain}.{domain}'
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("Discovered subdomain:", url)
        with lock:
            discovered_subdomains.append(url)

threads = []

for subdomain in subdomains:
    thread = threading.Thread(target=check_subdomain, args=(subdomain,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

with open('discovered_subdomains.txt', 'w') as file:
    for subdomain in discovered_subdomains:
        file.write(subdomain + '\n')