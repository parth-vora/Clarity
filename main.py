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

class VideoHandler(webapp2.RequestHandler):
    def get(self):
        template6 = jinja_current_directory.get_template('/templates/videos.html')
        self.response.write(template6.render())
class QuizHandler(webapp2.RequestHandler):
    def get(self):
        template7 = jinja_current_directory.get_template('/templates/quizzes.html')
        self.response.write(template7.render())
class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template2 = jinja_current_directory.get_template('/templates/home.html')
        template_vars = {'fortune': random.choice(inspiration)}
        self.response.write(template2.render(template_vars))
class TestHandler(webapp2.RequestHandler):
    def get(self):
        template5 = jinja_current_directory.get_template('templates/test.html')
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

        self.response.write(template5.render(template_vars))

    def post(self):
        count=1
        answer_list=[]
        total=0
        #assigns all questions to a variable and puts then in a list
        print(self.request)
        for i in range(8):
            answer=self.request.get("q"+str(count))
            print(int(answer))

            total+=int(answer)
            answer_list.append(answer)
            count+=1
         #puts all questions into the database
        # for i in range(8):
        #     index=answer_list[i]
        #     user_answer=QuizAnswer(answer=index, total=total)
        #     user_answer.put()

        template_vars={
            "answer_list": answer_list,
            "total":total,
        }
        template = jinja_current_directory.get_template('templates/test_output.html')
        self.response.write(template.render(template_vars))

inspiration = ['Be Happy, Be You! See the Clarity!', 'Failure will never overtake me if my determination to succeed is strong enough -Og Mandino', 'Life is 10 percent what happens to you and 90 percent how you react to it -Charles Swindoll', 'You  miss 100 percent of the shots you dont take - Wayne Gretsky', 'Problems are not stop signs, they are guidelines', 'Aim for the moon. If you miss, you may hit a star -W. Clement Stone','Only I can change my life. No one can do it for me. -Carol Burnett','If opportunity doesnt knock, build a door - Milton Berle','Tough times never last, but tough people do - Robert H. Schuller','Everyday may not be good but there is something good in everyday. -Alice Morse Earle']
print(random.choice(inspiration))

class QuizAnswer(ndb.Model):
    answer=ndb.IntegerProperty()
    total=ndb.IntegerProperty()

app = webapp2.WSGIApplication([
('/', HomeHandler),
('/quizzes', QuizHandler),
('/videos', VideoHandler),
('/test',TestHandler)
], debug=True)
