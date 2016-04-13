import sys


class ListComprehender(object):

    def __init__(self):
        self.introduction()
        self.test_comprehension()
        sys.exit()

    def introduction(self):
        introduction_text = "\nList Comprehender\nCreated for Python 3\n"
        print(introduction_text)

    def get_test(self):
        question = "targets = []\nfor follower in followers:\n\ttargets.append(follower)"
        answer = "[follower for follower in followers]"
        return {'question': question, 'answer': answer}

    def check_answer(self, user_answer, actual_answer):
        if user_answer == actual_answer:
            print("Correct. Well done!")
        else:
            print('Incorrect. The answer was %s' % actual_answer)

    def test_comprehension(self):

        test = self.get_test()
        print(test[0], "\n")

        answer = input(">>> ")

        self.check_answer(answer, test[1])


if __name__ == '__main__':
    listComprehender = ListComprehender()
