#!/usr/bin/python3.5

n2w1 = {	0: 'Zero',
			1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
n2w2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']


def num2word(num):
	num = str(num)
	string = ""
	if(len(num) == 1):
		string = n2w1[int(num[-1])]
	elif(len(num) > 1):
		n = int(num[-2:])
		if(n < 20 and n > 0):
			string = n2w1[n]
		elif(n > 19):
			n = int(num[-2])
			string = n2w2[n-2]
			n = int(num[-1])
			if(n > 0):
				string += "-"+n2w1[n]
		if(len(num) > 2):
			n = int(num[-3])
			if(n > 0):
				if(len(string) > 0):
					string = " and " + string
				string = n2w1[n] + " hundred" + string
	if(len(num) > 3):
		string = "one thousand"
				

	print(string)
	return string.lower()
			
			

summ = 0
for x in range(1, 1001):
	summ += len(num2word(x).replace(" ", "").replace("-", ""))

print(str(summ))

