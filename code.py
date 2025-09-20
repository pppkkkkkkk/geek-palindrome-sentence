class Solution:
	def isPalinSent(self, s):
		# code here
		
		input = s.lower()
		
		validChar = "abcdefghijklmnopqrstuvwxyz0123456789"
		
		validInput = ""
		for char in input:
		    if char in validChar:
		        validInput = validInput+char
		        
		i=0
		j=len(validInput)-1
	
		while j > i:
		    if validInput[i] != validInput[j]:
		        return False
		    j-=1
		    i+=1
		
		return True
		        