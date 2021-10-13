from bs4 import BeautifulSoup as bs
import json
import re

path_name = "nptel_html.html"

with open(path_name,"r") as f:
    text = f.read()

soup = bs(text,"html.parser")

questions_list = list()
quizz = dict()
choices = list()
multi_select = False


title = soup.select("a.gcb-nav-course-title")[1].get_text()



def multi(question):
    for i in range(len(question)):
        for j in answer:
            if type(j) is list:
                multi_select = True
            else:
                multi_select = False
            return multi_select
                
def choicess(answer):
    if multi_select:
        for j in answer:
            if type(j) is list:
                choices.append(len(j))
    else:
        choices.append(1)
    return list(set(choices))

for x in soup:
    img_list = list()
    for i,que in enumerate(x.select("div.qt-question")):
        my = list()
        if que.find_all("img"):
            imgs = que.find("img").get('src')




for x in soup:
    question_body_list = list()
    question = [que.get_text() for que in x.select("div.qt-question") if x.select("div.qt-question")]
    answer = [re.sub("[a-zA-Z]\.\s*","",ans.get_text(strip=True)) for ans in x.select("div.faculty-answer")]
    option = [re.sub("[a-zA-Z]\.\s*","",opt.get_text(strip=True,separator="\n")).split("\n") for opt in x.select("div.qt-choices")]
    for i,que in enumerate(x.select("div.qt-question")):
        img_list = list()
        if que.find_all("img"):
            img_list.append(que.find("img").get('src'))
        quiz = {"question_body": {
                "images":img_list,												
                "question_subparts": [],
                'explanation':[],
                "question": question[i]
                },
                "options":[{"is_correct" :True if q == answer[i] else False,"value":q} for q in option[i]],#quizzes,
                #"answers" : answer[i] # uncomment this line to see the answers
                }
        questions_list.append(quiz)
        quizz['metadata'] = {'source':{'url':'NPTEL',"type":'pdf'},'title':title,"explanation":False,'total_questions':len(question),'choices':choicess(answer),'multi_select':multi(question)}
        quizz['quizzes'] = questions_list


json_obj = json.dumps(quizz)
with open("nptel_sample.json","w") as s:
    s.write(json_obj)    

print('Json File Created Succesfully \U0001F601.')
		
