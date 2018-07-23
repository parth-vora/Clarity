import webapp2
import os
import random
import jinja2


def get_fortune():
    #add a list of fortunes to the empty fortune_list array
    fortune_list = [
        'There\'s no such thing as an ordinary cat.',
        'Now would be a good time to take up a new sport.',
        'Come back later; I am sleeping.',
        'Your resemblance to a muppet will prevent the world from taking you seriously.',
        'Next time, order the shrimp.'
        ]
    #use the random library to return a random element from the array
    random_fortune = fortune_list[random.randint(0, len(fortune_list) - 1)]
    return(random_fortune)


#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_directory.get_template(
            'templates/fortune_results.html')
        self.response.write(template.render())
    #add a post method
    #def post(self):

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        template1 = jinja_current_directory.get_template(
            'templates/hello.html')
        self.response.write(template1.render())

class GoodbyeHandler(webapp2.RequestHandler):
    def get(self):
        template2 = jinja_current_directory.get_template(
            'templates/goodbye.html')
        self.response.write(template2.render())

#the route mapping
app = webapp2.WSGIApplication([
    #this line routes the main url ('/')  - also know as
    #the root route - to the Fortune Handler
    ('/', HelloHandler),
    ('/farewell', GoodbyeHandler),
    ('/predict', FortuneHandler) #maps '/predict' to the FortuneHandler
], debug=True)
