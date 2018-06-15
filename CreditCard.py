class CreditCard:
	def __init__(self, number=""):
		self.number = str(number)

	def checkLength(self):
		if len(self.number) == 16 or len(self.number) == 15:
			return True
		else:
			return False

	def determineCardType(self):
		if self.checkLength:
			if self.number[0] == '4':
				return "Visa"
			elif self.number[0:2] in ['51','52','53','54','55']:
				return "MasterCard"
			elif self.number[0:2] in ["34", "37"]:
				return "Amex"
			elif self.number[0:4] == "6011":
				return "Discover Card"
			else:
				return "Not Valid"

		else:
			return "Not Valid"

	def validate(self):
		if self.determineCardType == "Not Valid":
			return False
		else:
			
			doubles = list(map(lambda x: int(x)*2, self.number[-2::-2]))
		
			digitSum = [x%10+1 if x > 9 else x for x in doubles]

			fullList = [int(x) for x in self.number[-1::-2]]
			fullList.extend(digitSum)
		
			finalSum = sum(fullList)

			if finalSum%10 == 0:
				return True
			else:
				return False


def main():

	myCard = CreditCard('5515460934365316')
	myCard2 =CreditCard('379179199857686')
	myCard3 = CreditCard('4929896355493470')
	fake = CreditCard('5215460934865316')


	if myCard2.validate():
		print("The", myCard.determineCardType(), ", ", myCard.number," is a valid credit card.")
	else:
		print(myCard.number," is NOT a valid credit card.")

	if myCard2.validate():
		print("The", myCard2.determineCardType(), ", ", myCard2.number,", is a valid credit card.")
	else:
		print(myCard2.number,", is NOT a valid credit card.")

	if fake.validate():
		print("The", fake.determineCardType(), ", ", fake.number,", is a valid credit card.")
	else:
		print(fake.number,", is NOT a valid credit card.")

	if myCard3.validate():
		print("The", myCard3.determineCardType(), ", ", myCard3.number,", is a valid credit card.")
	else:
		print(myCard3.number,", is NOT a valid credit card.")

main()


