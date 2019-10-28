import requests
import time

begin=time.time()
requests.get("http://192.168.2.107")
#time.sleep(1)
print(time.time()-begin)