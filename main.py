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

class InsecuritiesHandler(webapp2.RequestHandler):
    def get(self):
        template2 = jinja_current_directory.get_template('templates/test.html')
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
class IntrovertHandler(webapp2.RequestHandler):
    def get(self):
        template5 = jinja_current_directory.get_template('templates/test.html')
        question_list=[
        "I don't like to socialize with others",
        "I prefer staying at home instead of hanging out",
        "I have more fun when I'm alone",
        "I do not share my thoughts",
        "I like to stand away from the center of attention",
        "I tend to keep to myself in parties",
        "I feel obligated to speak at social events",
        "I feel as if I have a hard time making new friends",
        ]
        title="Insecurities"
        #Beginning
        template_vars={
        "question_list":question_list,
        "title":title
        }

        self.response.write(template5.render(template_vars))

    def post(self):
        count=1
        answer_list=[]
        total=0
        #assigns all questions to a variable and puts then in a list
        for i in range(8):
            answer=int(self.request.get("q"+str(count)))

            total+=answer
            answer_list.append(answer)
            count+=1
         #puts all questions into the database
        for i in range(8):
            index=answer_list[i]
            user_answer=QuizAnswer(answer=index, total=total)
            user_answer.put()
        #End
        outputs=[
        "You are an extrovert! You are able to meet others and should not be afraid to share your thoughts. If anyone says something else, remember that just because they are entitled to their own opinions, it doesn't mean that it is true! You're great and keep being you!",
        "You are doing great! You don't have to be an extrovert to have fun. Introverts are proven to have higher levels of cognitive ability. Be proud of who you are!",
        "Do not even stress about it! You are a wonderful person no matter what others might say. Just because you aren't in the center of attention, doesn't mean anything. People will be glad to meet you and get to know you! Keep on going strong! you are going places!"
        ]
        template_vars={
            "answer_list": answer_list,
            "total":total,
            "outputs":outputs
        }
        template = jinja_current_directory.get_template('templates/test_output.html')
        self.response.write(template.render(template_vars))

class MinoritiesHandler(webapp2.RequestHandler):
    def get(self):
        template2 = jinja_current_directory.get_template('templates/test.html')
        question_list1=[
        "I feel like I can't relate to other people",
        "My appearances always stand out amongst others",
        "I am not confident in myself",
        "I feel like I am judged because of my appearance",
        "I feel misunderstood",
        "I think being unique is a bad thing",
        "I sometimes wish I looked differently",
        "I am not happy that I look differently than others",
        ]
        title="Minorities"
        #Beginning
        template_vars={
        "question_list":question_list1,
        "title":title
        }
        self.response.write(template2.render(template_vars))
    def post(self):
        count=1
        answer_list=[]
        total=0
        #assigns all questions to a variable and puts then in a list
        for i in range(8):
            answer=int(self.request.get("q"+str(count)))
            total+=answer
            answer_list.append(answer)
            count+=1
         #puts all questions into the database
        for i in range(8):
            index=answer_list[i]
            user_answer=QuizAnswer(answer=index, total=total)
            user_answer.put()
        #End
        template_vars={
            "answer_list": answer_list,
            "total":total,
        }
        template = jinja_current_directory.get_template('templates/test_output.html')
        self.response.write(template.render(template_vars))

class AcademicHandler(webapp2.RequestHandler):
    def get(self):
        template2 = jinja_current_directory.get_template('templates/test.html')
        question_list1=[
        "I feel like my peers are smarter than me",
        "It takes me longer to process and learn things",
        "When I solve problems I usually get them wrong",
        "I work better with hands on activities",
        "Academics isn't my strong suit",
        "I don't do as well as I would like in academics",
        "I feel uncomfortable when people talk about their successes",
        "I get nervous when my teacher calls on me for the answer",
        ]

        title="Academic Insecurities"
        #Beginning
        template_vars={
        "question_list":question_list1,
        "title":title
        }
        self.response.write(template2.render(template_vars))
    def post(self):
        count=1
        answer_list=[]
        total=0
        #assigns all questions to a variable and puts then in a list
        for i in range(8):
            answer=int(self.request.get("q"+str(count)))
            total+=answer
            answer_list.append(answer)
            count+=1
         #puts all questions into the database
        for i in range(8):
            index=answer_list[i]
            user_answer=QuizAnswer(answer=index, total=total)
            user_answer.put()
        #End
        template_vars={
        "answer_list": answer_list,
        "total":total,
        }
        template = jinja_current_directory.get_template('templates/test_output.html')
        self.response.write(template.render(template_vars))

class ImposterHandler(webapp2.RequestHandler):
    def get(self):
        template2 = jinja_current_directory.get_template('templates/test.html')
        question_list1=[
        "I feel I don't deserve to be at the positions that I am in",
        "I feel like people are going to think I'm not qualified",
        "I am not confident in myself",
        "When I don't reach a goal that I set for myself, I think I am not cut out",
        "I feel like people are going to realize I don't belong in the position that I am in",
        "When I recieve praise for my work, I don't think I deserve it",
        "I make excuses for why I was able to sucessfully do something",
        "My work has to be perfect in order for me to show someone",
        ]

        title="Imposter Syndrome"
        #Beginning
        template_vars={
        "question_list":question_list1,
        "title":title
        }
        self.response.write(template2.render(template_vars))
    def post(self):
        count=1
        answer_list=[]
        total=0
        #assigns all questions to a variable and puts then in a list
        for i in range(8):
            answer=int(self.request.get("q"+str(count)))
            total+=answer
            answer_list.append(answer)
            count+=1
         #puts all questions into the database
        for i in range(8):
            index=answer_list[i]
            user_answer=QuizAnswer(answer=index, total=total)
            user_answer.put()
        #End
        template_vars={
        "answer_list": answer_list,
        "total": total,
        }
        template = jinja_current_directory.get_template('templates/test_output.html')
        self.response.write(template.render(template_vars))

class BodyHandler(webapp2.RequestHandler):
    def get(self):
        template2 = jinja_current_directory.get_template('templates/test.html')
        question_list1=[
        "I am too hard on myself",
        "I have an ideal image of myself that I strive to reach",
        "I feel like people judge me for the way that I look",
        "I think I should be more confident in myself",
        "The mirror is my nemesis",
        "I care too much about what people think of me",
        "I compare myself to others",
        "I tend to focus more on how much more progress I need to make rather than the progress I have already made",
        ]
        points=0
        user=User(points=0)
        user.put()
        title="Body Consciousness"
        #Beginning
        template_vars={
        "question_list":question_list1,
        "title":title,
        "points": user.points,
        }
        self.response.write(template2.render(template_vars))
    def post(self):
        count=1
        answer_list=[]
        total=0
        #user.points=12
        #assigns all questions to a variable and puts then in a list

        points=self.request.get("points")

        #print(points+"$")
        #points+=100
        for i in range(8):
            answer=int(self.request.get("q"+str(count)))
            total+=answer
            answer_list.append(answer)
            count+=1
         #puts all questions into the database
        for i in range(8):
            index=answer_list[i]
            user_answer=QuizAnswer(answer=index, total=total)
            user_answer.put()

        #End
        template_vars={
        "answer_list": answer_list,
        "total":total,
        #"points":points
        }
        template = jinja_current_directory.get_template('templates/test_output.html')
        self.response.write(template.render(template_vars))
inspiration = ['Be Happy, Be You! See the Clarity!', 'Failure will never overtake me if my determination to succeed is strong enough -Og Mandino', 'Life is 10 percent what happens to you and 90 percent how you react to it -Charles Swindoll', 'You  miss 100 percent of the shots you dont take - Wayne Gretsky', 'Problems are not stop signs, they are guidelines', 'Aim for the moon. If you miss, you may hit a star -W. Clement Stone','Only I can change my life. No one can do it for me. -Carol Burnett','If opportunity doesnt knock, build a door - Milton Berle','Tough times never last, but tough people do - Robert H. Schuller','Everyday may not be good but there is something good in everyday. -Alice Morse Earle']
print(random.choice(inspiration))

class QuizAnswer(ndb.Model):
    answer=ndb.IntegerProperty()
    total=ndb.IntegerProperty()
class User(ndb.Model):
    #username
    points=ndb.IntegerProperty()
app = webapp2.WSGIApplication([
('/insecurities', InsecuritiesHandler),
('/minority', MinoritiesHandler),
('/academic', AcademicHandler),
('/imposter', ImposterHandler),
('/body', BodyHandler),
('/', HomeHandler),
('/quizzes', QuizHandler),
('/videos', VideoHandler),
('/introvert',IntrovertHandler),
], debug=True)
