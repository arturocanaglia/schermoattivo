import requests

url='https://maxs19.fun/watchfree/wpju4cyygca9/plkcqr4jlsd3/cC9LVmhuL3lWSE5ZWkVWT0p0bjhrdz09'
r1 = requests.get(url, stream=True)
filename = "stream.avi"

num=0
if(r1.status_code == 200):
    with open(filename,'wb') as f:
        for chunk in r1.iter_content(chunk_size=1024):
            num += 1
            f.write(chunk)
            if num>5000:
                print('end')
                break

else:
    print("Received unexpected status code {}".format(r.status_code))