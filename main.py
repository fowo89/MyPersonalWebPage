#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

class AboutMe(BaseHandler):
    def get(self):
        personal_info = {"name": "Tomo", "age": "29", "education": "mechanical engineer", "employment": "Hella Saturnus", "town": "Kamnik", "goals": "to become a great programmer"}
        return self.render_template("aboutme.html", personal_info)

class MyProjects(BaseHandler):
    def get(self):
        return self.render_template("myprojects.html")

class Blog(BaseHandler):
    def get(self):
        return self.render_template("blog.html")

class Contact(BaseHandler):
    def get(self):
        contact_info = {"street": "Stari Grad 1a", "town": "Kamnik", "country": "Slovenija", "email": "strasniligenj@tojeto.si", "instagram": "@strasniligenj", "facebook": "facebook.com/strasniligenj", "snapchat": "@strasniligenj"}
        return self.render_template("contact.html", contact_info)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/aboutme', AboutMe),
    webapp2.Route('/myprojects', MyProjects),
    webapp2.Route('/blog', Blog),
    webapp2.Route('/contact', Contact),
], debug=True)
