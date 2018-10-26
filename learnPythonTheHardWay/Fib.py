class Fib:
	def __init__(self, max):
		self.max = max


	def __next__(self):
		fib=self.a
		if fib > self.max:
			raise StopIteration
		self.a, self.b = self.b, self.a + self.b
		return fib


