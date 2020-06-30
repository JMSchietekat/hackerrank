class Difference:
	def __init__(self, a):
		self.__elements = a

	def computeDifference(self):
		self.maximumDifference = 0
		
		for i in range(len(self.__elements)):
			for j in range(i, len(self.__elements)):
				diff = abs(self.__elements[i] - self.__elements[j])
				if (diff > self.maximumDifference):
					self.maximumDifference = diff

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
