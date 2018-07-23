import webapp2
import os
import random
import jinja2


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
        answer=self.request.get("options")
        answer2=self.request.get("options2")
        user_answer=QuizAnswer(self.answer=answer,self.answer2=answer2)
        user_answer.put()
        template_vars={
            "option": answer,
            "option2": answer2,
        }
        template = jinja_current_directory.get_template('templates/test_output.html')
        self.response.write(template.render(template_vars))

class QuizAnswer(ndb.Model):
     answer=nbd.IntegerProperty()
     answer2=nbd.IntegerProperty()


app = webapp2.WSGIApplication([
('/', HomeHandler),
], debug=True)
