import sys
from list_comprehender.data_handler import data_handler


class ListComprehender(object):

    def __init__(self):

        data_handler.createTables()
        data_handler.addData()
        self.introduction()
        self.test_comprehension()
        sys.exit()

    def introduction(self):
        introduction_text = "\nList Comprehender\nCreated for Python 3\n"
        print(introduction_text)

    def get_test(self):
        test = data_handler.retrieve_random_test('easy')
        return {'question': test.question, 'answer': test.answer}

    def check_answer(self, user_answer, actual_answer):
        if user_answer == actual_answer:
            print("Correct. Well done!")
        else:
            print('Incorrect. The correct answer was %s.' % actual_answer)

    def test_comprehension(self):

        test = self.get_test()
        print(test['question'], "\n")

        answer = input(">>> ")

        self.check_answer(answer, test['answer'])


if __name__ == '__main__':
    listComprehender = ListComprehender()
