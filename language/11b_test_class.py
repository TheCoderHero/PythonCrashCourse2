# Step 1 - import unittest from python lib
import unittest

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

question = "What is your native language?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("Thank you to everyone who participated in the survey.")
my_survey.show_results()

# Testing the CLASS
# Step 2 - Create a Test Class
class TestAnonymousSurvey(unittest.TestCase):
    # Step 3 - Create methods to test
    def test_store_single_response(self):
        question = "What is your native language?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        # Step 4 - Use assert Methods to test class methods
        self.assertIn('English', my_survey.responses)

    def test_store_multiple_responses(self):
        question = "What is your native language?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'French']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

# Step 5 - Add the main if statement
if __name__ == '__main__':
    unittest.main()

    # RETURN TO PAGE 186(ish) Chapter 11 "Testing a Class" TO FINISH THIS FILE