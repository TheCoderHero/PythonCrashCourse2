# Step 1 - Import unittest library
import unittest

# Test function
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")

# Step 2 - Create a class to contain your test
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    # Step 3 - Write function tests and name them beginning with 'test_'
    def test_first_last_name(self):
        formatted_name = get_formatted_name('john', 'tanner')
        # Step 4: Use an assert method to verify your results
        self.assertEqual(formatted_name, 'John Tanner')

# Step 5 - Include this if statement
    # If this is the main program, run the unittest
if __name__ == '__main__':
    unittest.main()

# Assert Methods
# assertEqual(a, b)       Verify that a == b
# assertNotEqual(a, b)    Verify that a != b
# assertTrue(x)           Verify that x is True
# assertFalse(x)          Verify that x is False
# assertIn(item, list)    Verify that item is in list
# assertNotIn(item, list) Verify that item is not in list