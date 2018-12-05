#from Entities import PAC

def Readin():
	#Read in txt line by line
	#Separate on Coma
	#Save to list
	#Create PossibleUpgrade - labeled as int 1 - inf
	pass


class PossibleUpgrade:

	def __init__ (self,GivenName,GivenCost,GivenImage,GivenDescription,GivenModifies,GivenModifier):
		self.Name = GivenName
		self.Cost = GivenCost
		self.Image = GivenImage
		self.Description = GivenDescription
		self.Modifies = GivenModifies
		self.Modifier = GivenModifier
		self.purchaced = False
		#Check all values exist - Alert user to issue
		
	def Display(self):
		pass
		#Sort - Modifies then Cost
		#Show image
		#Call each individually - just give info - main places info
	
	def Buy(self,CurrentCash):
		if CurrentCash >= self.Cost:
			#Can do following - inherits Current properties
			self.purchaced = True
			#PAC.ChangeProperty(self.Modifies, self.Modifier)
			return CurrentCash - self.Cost

		else:
			return CurrentCash 

## Name, Cost, Image, Description, AffecteProperty, Ammount ##