#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext='Logout'
            current_user=users.get_current_user().email()
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            current_user = None

        template_values = {
            'active_nav':'Main',
            'login_url':url,
            'login_text':url_linktext,
            'user':current_user
        }
        template = JINJA_ENVIRONMENT.get_template('base.html')
        self.response.write(template.render(template_values))
        
class TimeHandler(webapp2.RequestHandler):
    def get(self):
        if users.get_current_user():
            url = users.create_logout_url('/')
            url_linktext='Logout'
            current_user=users.get_current_user().email()
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            current_user = None

        template_values = {
            'active_nav':'Time',
            'login_url':url,
            'login_text':url_linktext,
            'user':current_user
        }
        
        template = JINJA_ENVIRONMENT.get_template('time.html')
        self.response.write(template.render(template_values))
        
class ClientHandler(webapp2.RequestHandler):
    def get(self):
        if users.get_current_user():
            url = users.create_logout_url('/')
            url_linktext='Logout'
            current_user=users.get_current_user().email()
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            current_user = None

        template_values = {
            'active_nav':'Clients',
            'login_url':url,
            'login_text':url_linktext,
            'user':current_user
        }
        template = JINJA_ENVIRONMENT.get_template('clients.html')
        self.response.write(template.render(template_values))
        
class ShipmateHandler(webapp2.RequestHandler):
    def get(self):
        if users.get_current_user():
            url = users.create_logout_url('/')
            url_linktext='Logout'
            current_user=users.get_current_user().email()
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            current_user = None

        template_values = {
            'active_nav':'Shipmates',
            'login_url':url,
            'login_text':url_linktext,
            'user':current_user
        }
        template = JINJA_ENVIRONMENT.get_template('shipmates.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/time' , TimeHandler),
    ('/clients' , ClientHandler),
    ('/shipmates' , ShipmateHandler),
], debug=True)
