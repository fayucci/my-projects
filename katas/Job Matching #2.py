def match(job, candidates):
    def matches_equity(candidate): 
        if candidate['desires_equity']:
            return job['equity_max'] > 0 
        else: return True

    def matches_locations(candidate):
        candidate_locations = {candidate['current_location'], *candidate['desired_locations']}
        if candidate_locations.intersection({*job['locations']}):
            return True
        else: return False
    
    return list(filter(lambda c:matches_equity(c) and matches_locations(c), candidates))


#matches_locations({'current_location': 'New York', 'desired_locations': ['San Francisco', 'Los Angeles']})

candidates = [{
  'desires_equity': True, 
  'current_location': 'New York',
  'desired_locations': ['San Francisco', 'Los Angeles']
}, {
  'desires_equity': False, 
  'current_location': 'San Francisco',
  'desired_locations': ['Kentucky', 'New Mexico'] 
}]
job1 = { 'equity_max': 0, 'locations': ['Los Angeles', 'New York'] }
job2 = { 'equity_max': 1.2, 'locations': ['New York', 'Kentucky'] }

print(match(job2, candidates))