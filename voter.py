class Voters(object):
	no_of_voters=0
	results={'trump':0,'bush':0,'clinton':0,'sanders':0}

	
	def show_no_of_voters(self,category):
		raise NotImplementedError
	def vote(self,vote_who):
		raise NotImplementedError
	
	def show_results(self,category):
		raise NotImplementedError

class Democrat_voters(Voters):
	no_of_voters=0
	results={'clinton':0,'sanders':0}

	def __init__(self):
		Voters.no_of_voters+=1
		Democrat_voters.no_of_voters+=1
	
	def show_no_of_voters(self,category):
		if(category=='party'):
			print(Democrat_voters.no_of_voters)
			return Democrat_voters.no_of_voters
		else:
			print(Voters.no_of_voters)
			return Voters.no_of_voters
	def vote(self,vote_who):
		vote_who.lower()
		if(not vote_who in Democrat_voters.results):
			print(vote_who+" is not recognised as a candidate in your party")
			return vote_who+" is not recognised as a candidate in your party"
		else:
			Democrat_voters.results[vote_who]+=1
			Voters.results[vote_who]+=1

		

	def show_results(self,category):
		if(category=='party'):
			print(Democrat_voters.results)
			return Democrat_voters.results
		else:
			print(Voters.results)
			return Voters.results


class Republican_voters(Voters):
	no_of_voters=0
	results={'trump':0,'bush':0}

	def __init__(self):
		Voters.no_of_voters+=1
		Republican_voters.no_of_voters+=1
	
	def show_no_of_voters(self,category):
		if(category=='party'):
			print(Republican_voters.no_of_voters)
			return Republican_voters.no_of_voters
		else:
			print(Voters.no_of_voters)
			return Voters.no_of_voters
	def vote(self,vote_who):
		vote_who.lower()
		if(not vote_who in Republican_voters.results):
			print(vote_who+" is not recognised as a candidate in your party")
			return vote_who+" is not recognised as a candidate in your party"
		else:
			Republican_voters.results[vote_who]+=1
			Voters.results[vote_who]+=1

		

	def show_results(self,category):
		if(category=='party'):
			print(Republican_voters.results)
			return Republican_voters.results
		else:
			print(Voters.results)
			return Voters.results


if(__name__=='__main__'):
	dem=Democrat_voters()
	rep=Republican_voters()
	
	dem.show_no_of_voters('party')
	dem.show_no_of_voters('overral')
	dem.show_results('party')
	dem.show_results('overal')
	dem.vote('trump')
	dem.vote('clinton')
	dem.vote('sanders')
	dem.show_results('party')
	dem.show_results('overal')

	rep.show_no_of_voters('party')
	rep.show_no_of_voters('overral')
	rep.show_results('party')
	rep.show_results('overal')
	rep.vote('clinton')
	rep.vote('trump')
	rep.vote('bush')
	rep.show_results('party')
	rep.show_results('overal')



	
