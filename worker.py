from urllib2 import Request, urlopen, URLError
import httplib
import urllib
import urllib2
import json
from pymongo import MongoClient
from bson.json_util import dumps

# Create a mongo client
mongo = MongoClient()
# Connect to the DB
db = mongo['mydb']
# Get the collection


# Fetch the jobs which are there in the springrole


def send_msg( p, title, job_id, slug ):
	

	link = slug+"/apply?user_id="+str(p[4])
	tup = ( str(p[1]), str(title), link )
	msg ="""{
	  "recipients": {
	      "values": [
	          {
		        "person": {
			"_path": "/people/%s"
				   }
				           }]
					     },
					       "subject": "I have a job suggestion for you!.",
					         "body": "You are certainly the best person for the job! %s Click this link to apply for it %s"}"""%tup
	print msg
	headers = {
	    	'Connection': 'keep-alive',
	        'Content-type': 'application/json',
	}
	req_link = 'https://api.linkedin.com/v1/people/~/mailbox?oauth2_access_token='+str(p[2])
	
	print req_link
	try:
		req = urllib2.Request(req_link, msg, headers)
		response = urllib2.urlopen(req)
		the_page = response.read()
	
		if( len(the_page) == 0 ):
		# Sucess
			return True
		else:
			return False
	# ref id is accesstoken
	# emp id is the linkedin generated msg id	

def get_skill_structure():
	skills = {};
	# Parse the json and return the dictionary of the skills
	col = db.springskills
	skill_cur = col.find({}, { "friends.empName": 1, "friends.skill1" : 1, "friends.skill2" : 2 , "friends.empId":1, "friends.location":1, "refId":1, "refName":1, "refToken":1 })
	
	for i in skill_cur:
		
		# Get the refereer id
		ref_token = i["refToken"]
		refname = i["refName"]
		refId = i["refId"]
		
		for j in i["friends"]:
			emp_name = j["empName"]
			emp_Id = j["empId"]
			s1 = j["skill1"]
			s2 = j["skill2"]
			loc = j["location"]
			
			t = ( emp_name, emp_Id, ref_token , refname, refId, loc );
	
			s1 = str(s1)
			s2 = str(s2)

			value = skills.get(s1, None);

			if( value == None ) :
				skills[s1] = []
				skills[s1].append(t);
			else :
				skills[s1].append(t);

			value = skills.get(s2, None);
			
			if( value == None ) :
				skills[s2] = []
				skills[s2].append(t);
			else :
				skills[s2].append(t);
	return skills
	
while True:
	# This will run forever

	# Get all the skills currently there in the database for the users and populate it in the array of hashmaps.
	
	# Get the skills from the DB
	skills = get_skill_structure();

	print skills.keys();
	

	for skill in skills.keys():
		try:
			resp = urlopen("https://api.springrole.com/beta/jobs?access_token=56576a614ac6042cb72b598d137a643b2c14cf14&user_id=ln_AM3R761Gcf&skills="+skill+"&page_size=100000")
			jobs = resp.read()
			# print result
		except URLError,e : 
			print "Error"
		# Got the Jobs now!
		parsed_jobs = json.loads(jobs)
		
		# Get the people who should be reffered for this skill
		people = skills[skill]

		# For each job for this skill, check who all are eligible and send them mails
		
		for job in parsed_jobs["data"]:
			job_id = job["jid"]
			
			print "Searching People for job : "+str(job_id)+"....................................."

			for p in people :

				# For each person p, check if the job request is already sent
				# p[0] --> empName
				# p[1] --> empId
				# p[2] --> refToken
				# p[3] --> refName
				# p[4] --> refId
				# p[5] --> location
				col1 = db.springjobs
				
				print "Person : "+str(p[0])+" referred by "+str(p[3])+" his/her email :"+str(p[1])

				job_r_cur = col1.find({ "empId" : p[1] }, { "jobs_referred":1 })
				
				if job_r_cur.count() == 0 :
					# the emp object is not present
					print "His/her object is not found in the referrals sent DS"
					print "Creating one"
					# create an entry and add it to the db collection emp_jobs_new	
					post_id = db.springjobs.insert( { "empId" : p[1], "jobs_referred": [ ] } )
					print "Insert Sucess"
					print post_id
				
				# Emp entry is present now
				# Now check if the emp_object has the job
				job_r_cur = col1.find({ "empId" : p[1] }, { "jobs_referred":1 })
				
				print "Now checking if the job "+str(job_id)+" is already there in "+str(job_r_cur[0]["jobs_referred"])

				if job_id not in job_r_cur[0]["jobs_referred"]:
					# if job id not present
					print "its not present"
					if send_msg(p, job["title"], job_id, job["job_url"]):
						# Success
						print "Sent the message"
						# populate the new job to the database
						db.springjobs.update({ "empId":p[1]}, { '$push' : { "jobs_referred" : job_id } })
				else:
					print "Job referral "+str(job_id)+" Already sent for "+str(p[0])
				# The message has been sent, if its not already sent before
		# Goto next skill
