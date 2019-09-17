class Number:
	def __init__(self, val):
		self.val = val
	
	def print(self, level):
		print(''.ljust(level*4) + self.val)


class Expr:
	def __init__(self, op, left, right):
		self.op = op
		self.left = left
		self.right = right
	
	def print(self, level = 0):
		print(''.ljust(level*4) + self.op)
		if self.left != None:
			self.left.print(level + 1)
		if self.right != None:
			self.right.print(level + 1)


class Parser:



	def match(self, val, throw = True):
		if( self.lookahead[1] == val):
			if self.index < len(self.tokens)-1:
				self.index = self.index + 1
				self.lookahead = self.tokens[self.index]
			else:
				self.lookahead = None

		else:
			raise Exception('syntax error')
				

	def parse(self, tokens):
		self.index = 0
		self.tokens = tokens
		self.lookahead = self.tokens[self.index]
		return self.parseE()


	def parseE(self):
		if self.lookahead != None : 
			self.match("1")	
			if self.lookahead != None:
				expr = self.parseE_()
				return Expr('+', Number("1"), expr)
			else:
				return Number('1')
		raise Exception('syntax error')


	def parseE_(self):
		self.match("+")
		return self.parseE()



# tokens=[("number", "1"), ("op", "+"), ("number", "1"), ("op", "+"), ("number", "1")]
# tokens=[ ("op", "+"), ("number", "1")]
tokens=[ ("number", "1"), ("op", "+"), ("number", "1")]

parser = Parser()
parser.parse(tokens).print()
