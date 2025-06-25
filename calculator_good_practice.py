class Calculator:
    """ A calculator class for basic operations. """

    def add(self, a, b):
        """ Returns the sum of two numbers"""
        return a + b
    
    def subtract(self, a, b):
        """ Returns the difference of two numbers"""
        return a - b

    def multiply(self, a, b):
        """Returns the product of two numbers"""
        return a * b

    def divide(self, a, b):
        """Returns the quotient of two numbers"""
        return a / b




    def main():
        """Collect user input and return numbers and operation."""
        calc = Calculator() # Create a Calculator instance
        
        # Displays operation choices to the user
        print("Simple Calculator")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

        # Get user's operation choice
        choice = input("Enter your choice: ")

        # Prompt user for two numeric inputs
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        # Map choices to corresponding Calculator methods
        operations = {
            "1": calc.add,
            "2": calc.subtract,
            "3": calc.multiply,
            "4": calc.divide
        }

    
