import httplib 
import urllib 
import urllib2 


headers = {
    'Connection': 'keep-alive',
    'Content-type': 'application/json',
}

data = """{
  "recipients": {
      "values": [
          {
	        "person": {
		        "_path": "/people/HMLrTUBPhu"
			       }
			           }]
				     },
				       "subject": "Congratulations on your new position.",
				         "body": "You are certainly the best person for the job!"
					 }"""

req = urllib2.Request('https://api.linkedin.com/v1/people/~/mailbox?oauth2_access_token=AQVfGDrOBgCipZEDs6btlaKQgJ51IOaNqo1F5mxzkseHrxGZKzJU1DtOb0iW8ihZUiYqRamKABuumqhUQAkn2P583OYtvOS0fyo5GDKMruJdV25rKmomKQ3QqpKgF7nN8eZvi_NmGWjyCXKMO8Pm4MwZCZpnfJUUXoUMF4NYIfVdO6W_n08', data, headers) 
response = urllib2.urlopen(req)
the_page = response.read()

print the_page
print len(the_page)
