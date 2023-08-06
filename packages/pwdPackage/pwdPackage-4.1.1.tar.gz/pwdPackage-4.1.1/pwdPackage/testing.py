import unittest
import csv
from passwd import gen_pass

class TestPasswordTester(unittest.TestCase):

    def exclude_csv(self, path):
        """
        Reads data from a CSV file and returns a set of values from the first column.

        Parameters:
            path (str): The path to the CSV file.

        Returns:
            set: A set containing values from the first column of the CSV file.
        """
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            return set(row[0] for row in reader)

    def setUp(self):
        """
        Load the excluded names and places from the CSV files
        """
        self.excluded_names = self.exclude_csv("names.csv")
        self.excluded_places = self.exclude_csv("places.csv")

    def testing(self):
        """
        Test the generated password using the gen_pass function with exclusions
        """
        # Generate a password using the gen_pass function with exclusions
        generated_password = gen_pass()
        
        # Ensure that the generated password is between 6 and 12 characters
        self.assertTrue(6 <= len(generated_password) <= 12)

        # Ensure that the generated password contains at least one lowercase letter
        self.assertTrue(any(char.islower() for char in generated_password))

        # Ensure that the generated password contains at least one uppercase letter
        self.assertTrue(any(char.isupper() for char in generated_password))

        # Ensure that the generated password contains at least one number
        self.assertTrue(any(char.isdigit() for char in generated_password))

        # Ensure that the generated password is not present in the excluded names and places
        self.assertNotIn(generated_password, self.excluded_names.union(self.excluded_places))

if __name__ == "__main__":
    unittest.main()
