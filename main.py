from Regex.regex_main import regex_main
from t5base.questiongenerator import QuestionGenerator
from t5base.questiongenerator import print_qa
from spacy import load
import nltk

qg = QuestionGenerator()
def generate_MCQ_question(text,numOfQues=10,ansstyle = 'all'):
    qalist =qg.generate(text,use_evaluator=True, answer_style = ansstyle,num_questions = int(numOfQues))

    for item in qalist:
        if isinstance(item["answer"], str):
            item["questiontype"] = 1
        else:
            item["questiontype"] = 0
            new_answers = {}
            for i, answer in enumerate(item["answer"]):
                answer_text = answer["answer"]
                option_key = f"option{i+1}"
                new_answers[option_key] = answer_text
                if answer["correct"]:
                    is_correct = option_key
            item["answer"] = new_answers
            item["isCorrect"] = new_answers[is_correct]
        # item["show"] = True
        item["answers"] = item.pop("answer") 
    print(qalist)
    return qalist
def main():

    # text = open('sampleText/owl_rescue.txt','r', encoding='utf8').read()
    # text = 'This is a sample text. Hopefully it can generate a question.'
    # qg = QuestionGenerator()
    # qalist =qg.generate(text,use_evaluator=True, answer_style = 'multiple_choice')
    # print(qalist)
    qalist = [{'question': 'What language was the rescue?', 'answer': [{'answer': 'Bad Segeberg', 'correct': False}, {'answer': 'German', 'correct': True}, {'answer': 'Germany', 'correct': False}, {'answer': '12', 'correct': False}], 'questiontype': 0, 'show': True}, {'question': 'How many members of the eagle owl rescue team were involved?', 'answer': [{'answer': '12', 'correct': False}, {'answer': 'six', 'correct': True}, {'answer': '40m', 'correct': False}, {'answer': 'two', 'correct': False}], 'questiontype': 0, 'show': True}, {'question': 'How many firefighters were involved in the eagle owl rescue?', 'answer': [{'answer': 'Lübeck', 'correct': False}, {'answer': 'two', 'correct': False}, {'answer': 'six', 'correct': False}, {'answer': '12', 'correct': True}], 'questiontype': 0, 'show': True}, {'question': 'How many people were involved in the rescue?', 'answer': [{'answer': '131ft', 'correct': False}, {'answer': '12', 'correct': False}, {'answer': 'six', 'correct': False}, {'answer': 'two', 'correct': True}], 'questiontype': 0, 'show': True}, {'question': 'What day was the eagle owl hooting from the well?', 'answer': [{'answer': 'Saturday', 'correct': True}, {'answer': '40m', 'correct': False}, {'answer': '131ft', 'correct': False}, {'answer': '12', 'correct': False}], 'questiontype': 0, 'show': True}, {'question': 'how deep is the owl?', 'answer': [{'answer': '131ft', 'correct': False}, {'answer': '40m', 'correct': True}, {'answer': 'Kalkberg', 'correct': False}, {'answer': 'Saturday', 'correct': False}], 'questiontype': 0, 'show': True}, {'question': 'how high is the owl?', 'answer': [{'answer': 'Lübeck', 'correct': False}, {'answer': 'two', 'correct': False}, {'answer': '131ft', 'correct': True}, {'answer': 'six', 'correct': False}], 'questiontype': 0, 'show': True}, {'question': 'Where did the owl come from?', 'answer': [{'answer': 'Germany', 'correct': True}, {'answer': 'two', 'correct': False}, {'answer': 'The Bad Segeberg', 'correct': False}, {'answer': 'Lübeck', 'correct': False}], 'questiontype': 0, 'show': True}, {'question': 'what is the name of the town?', 'answer': [{'answer': 'Bad Segeberg', 'correct': True}, {'answer': 'The Bad Segeberg', 'correct': False}, {'answer': '131ft', 'correct': False}, {'answer': 'Kalkberg', 'correct': False}], 'questiontype': 0, 'show': True}, {'question': 'what is the name of the town?', 'answer': [{'answer': '131ft', 'correct': False}, {'answer': 'Germany', 'correct': False}, {'answer': '12', 'correct': False}, {'answer': 'Lübeck', 'correct': True}], 'questiontype': 0, 'show': True}]
    for item in qalist:
        if isinstance(item["answer"], str):
            item["questiontype"] = 1
        else:
            item["questiontype"] = 0
            new_answers = {}
            for i, answer in enumerate(item["answer"]):
                answer_text = answer["answer"]
                option_key = f"option{i+1}"
                new_answers[option_key] = answer_text
                if answer["correct"]:
                    is_correct = option_key
            item["answer"] = new_answers
            item["isCorrect"] = new_answers[is_correct]
        item["show"] = True
        item["answers"] = item.pop("answer")
    print(qalist)
    # {
    #         "questionType": 0,
    #         "question": "what is question 1",
    #         "answers": {
    #             "option1": "first option",
    #             "option2": "second option",
    #             "option3": "third option",
    #             "option4": "fourth option"
    #         },
    #         "isCorrect": "first option",
    #         "show": true
    #     }
    # print_qa(qalist)
if __name__ == "__main__":
    main()
