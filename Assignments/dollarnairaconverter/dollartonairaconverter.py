amount = int(input("Enter dollar amount to convert to naira: "))

def naira_converter(dollar_amount):
	if type (dollar_amount) != float and type (dollar_amount) != int:
		return"invalid input"
		
	result = dollar_amount * 1550
	return result
	
print (naira_converter(1.2))
