class Solution:
	def isPalinSent(self, s):
		# code here
		
		input = s.replace(" ","")
		input = input.lower()
		
		validChar = "abcdefghijklmnopqrstuvwxyz"
		
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
		        