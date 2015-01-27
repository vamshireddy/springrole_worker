# springrole_worker

This worker is a python script, which polls the spring role api and searches for any new jobs of a skill.
If there is a job, then it will search the DB for all the users who have been referred by their friends who match for the current job. After that, this worker sends a linkedin message to the matched person on behalf of the user who referred him.
This linkedin message will have a springrole URL which includes who referred the person. That way the person who referred a friend will get the credit, if his/her friend gets a job or interview.


It needs 2 MongoDB collections
* For storing the details of referrals by a person
```
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
```
* for storring the reffered job ids of a person
```
{
	"_id" : ObjectId("54c4c8b41d41c8174791cb25"),
	"empId" : "HMLrTUBPhu",
	"jobs_referred" : [123, 215 ]
}
```
