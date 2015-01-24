from urllib2 import Request, urlopen, URLError
import json
from pymongo import MongoClient
from bson.json_util import dumps

# Create a mongo client
mongo = MongoClient()
# Connect to the DB
db = mongo['mydb']
# Get the collection


# Fetch the jobs which are there in the springrole


def get_skill_structure():
	
	skills = {};

	# Parse the json and return the dictionary of the skills
	col = db.skilly
	skill_cur = col.find({}, { "friends.empName": 1, "friends.skill1" : 1, "friends.skill2" : 2 , "friends.empEmail":1, "friends.jobs":1 })
	
	for i in skill_cur:
		for j in i["friends"]:
			emp_name = j["empName"]
			emp_email = j["empEmail"]
			s1 = j["skill1"]
			s2 = j["skill2"]
			job_arr = j["jobs"]
			
			t = ( emp_name, emp_email, job_arr);
	
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

		if skill != "C" :
			continue
		# Get all the jobs of this Skill
		try:
			resp = urlopen("https://api.springrole.com/beta/jobs?access_token=56576a614ac6042cb72b598d137a643b2c14cf14&user_id=ln_AM3R761Gcf&skills="+skill+"&page_size=100000")
			jobs = resp.read()
			# print result
		except URLError,e : 
			print "Error"
		# Got the JObs now!
		parsed_result = json.loads(jobs)
		print skills[skill],"\n\n"
		print parsed_result["data"];
		# Get the employees for a the current skill
		# TODO
		print "\n\n\n"
	
	break;


	# Now parse it

	parsed_result = json.loads(result)
	for i in range(0,len(parsed_result["data"])):
		print parsed_result["data"][i]["jid"], parsed_result["data"][i]["requirements"],"\n";
	break


