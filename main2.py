import webapp2
import os
import random
import jinja2
from google.appengine.ext import ndb

#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template2 = jinja_current_directory.get_template('templates/test.html')
        question_list=[
        "I like to socialize with others",
        "I prefer hanging out instead of staying at home",
        "I have more fun when I'm alone",
        "I do not share my thoughts",
        "I like to stand away from the center of attention",
        "I tend to keep to myself in parties",
        "I like to attend social events where I am involved in the festivities",
        "I feel as if I have a hard time making new friends",
        ]

        template_vars={
        "question_list":question_list,
        }

        self.response.write(template2.render(template_vars))

    def post(self):
        count=1
        answer_list=[]
        total=0
        #assigns all questions to a variable and puts then in a list
        print(self.request)
        for i in range(8):
            answer=int(self.request.get("q"+str(count)))

            total+=answer
            answer_list.append(answer)
            count+=1
         #puts all questions into the database
        for i in range(8):
            index=answer_list[i]
            print index
            user_answer=QuizAnswer(answer=index, total=total)
            user_answer.put()

        template_vars={
            "answer_list": answer_list,
            "total":total,
        }
        template = jinja_current_directory.get_template('templates/test_output.html')
        self.response.write(template.render(template_vars))


class QuizAnswer(ndb.Model):
    answer=ndb.IntegerProperty()
    total=ndb.IntegerProperty()

app = webapp2.WSGIApplication([
('/', HomeHandler),
], debug=True)
