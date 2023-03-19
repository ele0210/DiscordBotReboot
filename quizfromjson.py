import json
import random

def get_quiz():
    # quiz_dic = {}
    if random.randint(0, 9) < 4:
        quiz_json_num = random.randint(1, 13)
        quiz_json = open('json/QuizDataSet' + str(quiz_json_num) + '.json', 'r' ,encoding="utf-8_sig")
        quiz_all = quiz_json.readlines()
        quiz_single = json.loads(quiz_all[random.randint(0, len(quiz_all)) - 1])
        quiz_text = quiz_single['question']
        quiz_answer = quiz_single['answer']
        quiz_dic = {'text':quiz_text, 'answer':quiz_answer}
    else:
        quiz_json_num = random.randint(1, 2)
        quiz_json = open('json/QuizSelect' + str(quiz_json_num) + '.json', 'r' ,encoding="utf-8_sig")
        quiz_all = quiz_json.readlines()
        replaced = quiz_all[random.randint(0, len(quiz_all)) - 1].replace('\'', '\"')
        quiz_single = json.loads(replaced)
        quiz_text = quiz_single['question']
        quiz_answer = quiz_single['answer']
        quiz_other = quiz_single['other']
        quiz_dic = {'text':quiz_text, 'answer':quiz_answer, 'other1':quiz_other[0], 'other2':quiz_other[1], 'other3':quiz_other[2]}
    return quiz_dic
