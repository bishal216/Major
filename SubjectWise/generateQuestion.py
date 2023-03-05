import json
import random
import itertools
# OnM

def chooseDistribution(subject):
    with open('SubjectWise\distribution.json') as f:
        data = json.load(f)
    entries = []
    for entry in data:
        if entry['subject'] == subject:
            entries.append(entry)
    entry = random.choice(entries)
    return entry    

def random_combination(numbers, target_sum):
    combinations = itertools.product(numbers, repeat=len(numbers))
    valid_combinations = [c for c in combinations if sum(c) == target_sum]
    if not valid_combinations:
        return None
    return random.choice(valid_combinations)

def selectQuestions(data, target_sum):
    marks_set = []
    for entry in data:
        marks_set.append(entry['mark'])
        marks_set = list(set(marks_set))
    for i in range(len(marks_set)):
        marks_set[i] = int(marks_set[i])
    return list(random_combination(marks_set,target_sum))
    
def choose_question(data, mark):
    entries = []
    for entry in data:
        if mark == int(entry['mark']):
            entries.append(entry)
    entry = random.choice(entries)
    return entry    
    
def generate(subject):
    dist = chooseDistribution(subject)['markDistribution']
    questionSet =[]
    for i,item in enumerate(dist):
        chap = 'SubjectWise/Results/OnM/chapter'+str(i+1)+'.json'
        with open(chap) as f:
            data = json.load(f)
            n = item/8
            for i in range(int(n)):
                questions = []
                qList = selectQuestions(data,8)
                for q in qList:
                    questions.append(choose_question(data,q))
                marks = "+".join([x['mark'] for x in questions])
                question = "".join([x['question'] for x in questions])
                answer = "".join([x['answer'] for x in questions])
                result = {'question': question,'answer':answer,'mark': marks}
                questionSet.append(result)
                questions=[]
    for i,item in enumerate(questionSet):
        print(str(i+1)+'.'+str(item)+'/n')
        return questionSet         

# generate("OnM") 