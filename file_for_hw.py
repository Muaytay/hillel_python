from requests import get
import time
t = time.time()
ip = get('https://api.ipify.org').text
print('My public IP address is: {}'.format(ip))
t1 = time.time() - t
print(f"It takes {t1} seconds to get an ip adress")
