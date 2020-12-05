class Solution:
    def find_median(self, v):
	    median = 0
		# Code here
		v.sort()
		n = len(v)
		if n%2 == 0:
		    median = (v[n//2] + v[(n//2)-1])//2
		else:
		    median =  v[n//2]
	    return median	    

