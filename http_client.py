import http.client

h = http.client.HTTPConnection("www.jaygupta.me")
h.request("GET", "/")
data = h.getresponse()
print (data.code)
print (data.headers)
text = data.readlines()
for t in text:
    print(t.decode('utf-8'))
    
# _array = ['bhai', 'bhai', 'bhai']
# _array.append('Kya code likha hai bhai ne, nagar palika ko bulao mc...')

