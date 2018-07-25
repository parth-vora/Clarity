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
        title="Insecurities"
        #Beginning
        template_vars={
        "question_list":question_list,
        "title":title
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
        #End
        template_vars={
            "answer_list": answer_list,
            "total":total,
        }
        template = jinja_current_directory.get_template('templates/test_output.html')
        self.response.write(template.render(template_vars))

class MinoritiesHandler(webapp2.RequestHandler):
    def get(self):
        template2 = jinja_current_directory.get_template('templates/test.html')
        question_list1=[
        "I feel like I can't relate to other people",
        "My appearances always stand out amongst others",
        "I am confident in myself",
        "I feel like I am judged because of my appearance",
        "I feel misunderstood",
        "I think being unique is a good thing",
        "I sometimes wish I looked differently",
        "I am happy that I look differently than others",
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

        title=
        "Academic Insecurities"
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
        "I am confident in myself",
        "When I miss a mark that I set for myself, I think I am not cut out",
        "",
        "",
        "",
        "",
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
        "I sometimes am too hard on myself",
        "I have an ideal image of myself that I strive to reach",
        "I feel like people judge me for the way that I look",
        "I think I should be more confident in myself",
        "The mirror is my nemesis",
        "I care too much about what people think of me",
        "I compare myself to others",
        "I tend to focus more on how much more progress I need to make rather than the progress I have already made",
        ]


        title="Body Consciousness"
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
        #End
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
('/', InsecuritiesHandler),
('/minority', MinoritiesHandler),
('/academic', AcademicHandler),
('/imposter', ImposterHandler),
('/body', BodyHandler),
], debug=True)
