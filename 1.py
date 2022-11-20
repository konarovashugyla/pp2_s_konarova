'''Define a class which has at least two methods: getString:
to get a string from console input printString: to print the string
in upper case.
'''
class Problem1:
    def getString( self, stroka):
        self.name= stroka
    def printString(self):
        s = self.name.upper()
        return s