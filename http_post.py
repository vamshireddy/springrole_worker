import httplib
import urllib
import re

# specify we're sending parameters that are url encoded
headers = { 'Content-Type' : 'application/json' }

# our parameters
params = { 'oauth2_access_token' : 'AQVfGDrOBgCipZEDs6btlaKQgJ51IOaNqo1F5mxzkseHrxGZKzJU1DtOb0iW8ihZUiYqRamKABuumqhUQAkn2P583OYtvOS0fyo5GDKMruJdV25rKmomKQ3QqpKgF7nN8eZvi_NmGWjyCXKMO8Pm4MwZCZpnfJUUXoUMF4NYIfVdO6W_n08' }

# establish connection with the webpage
h = httplib.HTTPConnection('https://api.linkedin.com/')

# url encode the parameters
url_params = urllib.parse.urlencode(params)

# send out the POST request
h.request('POST', 'v1/people/~/mailbox', url_params, headers)

# get the response
r = h.getresponse()

print r

# analyse the response
if re.search("Error", r.read.decode()):
    print("Not found")
else:
    print("Probably found")
    h.close()
