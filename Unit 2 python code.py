import unittest  # Importing the unittest module for writing and running tests

# Function to add two numbers and return the result
def add(x, y):
    return x + y

# Main function to prompt user for input and display the result of addition
def main():
    x = int(input("Enter first varirable: "))  # Prompting user for the first number as an integer
    y = int(input("Enter second variable: "))  # Prompting user for the second number as an integer

    result = add(x, y)  # Calling the add_numbers function with user inputs
    print("The result of adding the two numbers is:", result)  # Displaying the result

# Test case class for the calculator functionality
class TestCalculator(unittest.TestCase):
    # Test method to ensure addition works correctly
    def test_addition(self):
        # Test case 1: Adding 2 and 3 should be 5
        self.assertEqual(add(3, 3), 6)
        # Test case 2: Adding -1 and 5 should be 4
        self.assertEqual(add(-1, 10), 9)
        # Test case 3: Adding 0 and 0 should be 0
        self.assertEqual(add(0, 2), 2)

# Checking if the script is run directly
if __name__ == '__main__':
    main()  # Calling the main function to prompt for user input and display the result

    # Running the unit tests using unittest's test runner
    result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCalculator))
    if result.wasSuccessful():
        print("All tests passed!")  # Print this message if all tests passed 

