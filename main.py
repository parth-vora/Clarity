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
        template2 = jinja_current_directory.get_template('/templates/home.html')
        template_vars = {'fortune': random.choice(inspiration)}
        self.response.write(template2.render(template_vars))
    def post(self):
        count=1
        answer_list=[]
        total=0
        #assigns all questions to a variable and puts then in a list
        for i in range(8):
            answer=int(self.request.get("q"+str(count)))
            total+=answer;
            answer_list.append(answer);
            count+=1
        #puts all questions into the database
        for i in range(8):
            index=answer_list[i]
            user_answer=QuizAnswer(answer=index)
            user_answer.put()

        template_vars={
            "answer_list": answer_list,
            "total":total, 
        }
        template = jinja_current_directory.get_template('templates/test_output.html')
        self.response.write(template.render(template_vars))

<<<<<<< HEAD
inspiration = ['Be Happy, Be You! See the Clarity!', 'Failure will never overtake me if my determination to succeed is strong enough -Og Mandino', 'Life is 10% what happens to you and 90% hpow you react to it -Charles Swindoll', 'You  miss 100 percent of the shots you dont take - Wayne Gretsky', 'Problems are not stop signs, they are guidelines', 'Aim for the moon. If you miss, you may hit a star -W. Clement Stone','Only I can change my life. No one can do it for me. -Carol Burnett','If opportunity doesnt knock, build a door - Milton Berle','Tough times never last, but tough people do - Robert H. Schuller','Everyday may not be good but there is something good in everyday. -Alice Morse Earle']
print(random.choice(inspiration))
=======
>>>>>>> 9f755e8ae4e24d345821cbaefff1fa2082f35bb8


class QuizAnswer(ndb.Model):
     answer=ndb.IntegerProperty()


app = webapp2.WSGIApplication([
('/', HomeHandler),
], debug=True)
