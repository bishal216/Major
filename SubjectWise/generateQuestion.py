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

def random_combination1(numbers, target_sum):
    combinations = itertools.product(numbers, repeat=len(numbers))
    valid_combinations = [c for c in combinations if sum(c) == target_sum]
    if not valid_combinations:
        print('No valid combination for'+str(numbers)+'and'+str(target_sum))
        return None
    return random.choice(valid_combinations)
def random_combination2(numbers, target_sum):
    combinations = [[2,2,2,2],[2,4,2],[4,4],[2,6],[8]]
    if 8 in numbers:
        if random.random() < 0.4:
            return [8]
    elif 6 in numbers:
        if random.random() < 0.5:
            return [2,6]
    elif 4 in numbers:
        if random.random() < 0.3:
            return [4,4]
        if random.random() > 0.7:
            return [4,2,2]
    else:
        return [2,2,2]
    # for length in range(1, len(numbers) + 1):
    #     combinations = itertools.combinations(numbers, length)
    #     valid_combinations = [c for c in combinations if sum(c) == target_sum]
    #     if valid_combinations:
    #         return random.choice(valid_combinations)
    # print('No valid combination for'+str(numbers)+'and'+str(target_sum))
    # return None
    # possibleCombo = [[2,2,2,2],[2,6],[4,4],[8]]
    # if target_sum < min(numbers):
    #     return None

    # # Generate a random list of numbers until the sum is equal to the target sum
    # while True:
    #     result = []
    #     sum_so_far = 0
    #     for i in range(len(numbers)):
    #         if sum_so_far + numbers[i] > target_sum:
    #             break
    #         result.append(numbers[i])
    #         sum_so_far += numbers[i]

    #     # If the sum is equal to the target sum, return the list of numbers
    #     if sum(result) == target_sum:
    #         return result

    #     random.shuffle(numbers)


def selectQuestions(data, target_sum):
    marks_set = []
    for entry in data:
        # print(entry)
        marks_set.append(int(entry['marks']))
        marks_set = list(set(marks_set))
    for i in range(len(marks_set)):
        marks_set[i] = int(marks_set[i])
        print(marks_set)
    return (random_combination1(marks_set,target_sum))
    
def choose_question(data, mark):
    entries = []
    for entry in data:
        if mark == int(entry['marks']):
            entries.append(entry)
    # print(entries)
    entry = random.choice(entries)
    
    return entry    
    
def generate(subject):
    dist = chooseDistribution(subject)['markDistribution']
    questionSet =[]
    for i,item in enumerate(dist):
        chap = 'SubjectWise/Results/'+subject+'/Chapter'+str(i+1)+'.json'
        with open(chap,encoding='utf-8') as f:
            data = json.load(f)
            n = item/8
            for i in range(int(n)):
                questions = []
                qList =[]
                if(subject == 'OnM'):
                    qList = selectQuestions(data,8)
                if(subject == 'OOAD'):
                    qList = selectQuestions(data,8)
                else : 
                    qList = [2,2,2,2] #selectQuestions(data,8)
                print(qList)
                for q in qList:
                    
                    questions.append(choose_question(data,q))
                marks = "+".join([str(x['marks']) for x in questions])
                question = "".join([x['question'] for x in questions])
                answer = "".join([x['answer'] for x in questions])
                result = {'question': question,'answer':answer,'mark': marks}
                questionSet.append(result)
                questions=[]
    return questionSet         

# generate("OnM") 
# generate("EES")
# generate("OOAD")
# generate("SE")
generate("EPP")