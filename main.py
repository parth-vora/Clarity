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

#the route mapping
app = webapp2.WSGIApplication([
('/', HomeHandler),
], debug=True)
