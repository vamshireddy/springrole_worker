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


def get_skills():
	
	# Parse the json and return the dictionary of the skills
	col = db.skills
	skill_cur = col.find({}, { "friends.skill1" : 1, "friends.skill2" : 2 })
	
	# Convert the cusor to json
	skill_json =  dumps(skill_json);
	

	skills = {};

	"""
	for user in len(skill_parsed):
		for friend in len(skill_parsed[user]["friends"]):
			skills[skill_parsed[user][friend["skill1"]] = 1;
"""
	


while True:
	# This will run forever

	# Get all the skills currently there in the database for the users and populate it in the array of hashmaps.
	
	
	# Get the skills from the DB
	get_skills();

	break

	#TODO
	
	for skill in skills:
		# Get all the jobs of this Skill
		try:
			resp = urlopen("https://api.springrole.com/beta/jobs?access_token=56576a614ac6042cb72b598d137a643b2c14cf14&user_id=ln_AM3R761Gcf&skills="++"&page_size=100000")
			jobs = resp.read()
			# print result
		except URLError,e : 
			print "Error"
		# Got the JObs now!

		# Get the employees for a the current skill
		# TODO


	# Now parse it

	parsed_result = json.loads(result)
	for i in range(0,len(parsed_result["data"])):
		print parsed_result["data"][i]["jid"], parsed_result["data"][i]["requirements"],"\n";
	break


