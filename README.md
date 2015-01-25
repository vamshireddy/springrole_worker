# springrole_worker

This worker is a python script, which polls the spring role api and searched for any new jobs of a skill.
If there is a job, then it will search the DB for all the users who have been referred by their friends who match for the current job.


It needs 2 MongoDB collections
1) For storing the details of referrals by a person
SCHEMA: 
  {
	"refId" : "vami",
	"refName" : "vsa",
	"refToken" : "AQVfGDrOBgCipZEDs6btlaKQgJ51IOaNqo1F5mxzkseHrxGZKzJU1DtOb0iW8ihZUiYqRamKABuumqhUQAkn2P583OYtvOS0fyo5GDKMruJdV25rKmomKQ3QqpKgF7nN8eZvi_NmGWjyCXKMO8Pm4MwZCZpnfJUUXoUMF4NYIfVdO6W_n08",
	"friends" : [
		{
			"empId" : "HMLrTUBPhu",
			"empName" : "nataraj",
			"skill1" : "Python",
			"skill2" : "Java",
			"location" : "Bangalore"
		}
	]
}
2) for storring the reffered job ids of a person
{
	"_id" : ObjectId("54c4c8b41d41c8174791cb25"),
	"empId" : "HMLrTUBPhu",
	"jobs_referred" : [123, 215 ]
}
