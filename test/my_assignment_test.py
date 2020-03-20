
#test/my_assignment_test.py


import unittest
from amys_lambda.assignment import CustomFrame

class TestCustomFrame(unittest.TestCase):
  

    def test_add_state_name(self):
        custom_df = CustomFrame({"abbrevations": ["CA", "CO", "CT", "TX", "DC"]})
        self.assertTrue('name' not in list(custom_df.columns))

        

        custom_df.add_state_name()
        self.assertTrue('name' in list(custom_df.columns))
        #"california" should exist in a column called "name"
        #self.assertEqual(enlarge(5), 500)
        # self.assertEqual(True, True)
        self.assertEqual(custom_df['name'][0], "California")
        self.assertEqual(custom_df['abbrevations'][0], "CA")



if __name__ == '__main__':
    unittest.main()