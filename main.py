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
        template2 = jinja_current_directory.get_template(
            'templates/test.html')
        self.response.write(template2.render())
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



class QuizAnswer(ndb.Model):
     answer=ndb.IntegerProperty()


app = webapp2.WSGIApplication([
('/', HomeHandler),
], debug=True)
