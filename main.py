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
#
# nexus5checker@gmail.com   Checker2013

import webapp2
from google.appengine.api import mail
import logging
from urllib import urlopen

class MainHandler(webapp2.RequestHandler):
    def get(self):
        recipients = 'tedsunnyday@gmail.com'
        #recipients = ['tedsunnyday@gmail.com','maxxxchou@gmail.com']
        #recipients = ['tedsunnyday@gmail.com','nexus5checker@gmail.com']

        #theURL = "https://play.google.com/store/devices/details?id=nexus_5_16gb"
        theURL = "https://play.google.com/store/devices/details?id=nexus_7_16gb_2013"

        contents = urlopen(theURL).read()
        self.response.write(contents)
        self.response.write('checked page below </br>%s</br>' % (theURL,))
        if contents.find("was not found") != -1:
            self.response.write('page is NOT available :(</br>')
        else:
            self.response.write('page is available !!!</br>')


        #if contents.find("buy-button-container") != -1:
        if contents.find("Add to cart") != -1:
            #self.response.write('CAN buy now !!!</br>') 

            sender_address = "tedsunnyday@gmail.com"
            sender_address = "nexus5checker@gmail.com"
            subject = "Nexus 5 is available - Check Google Play Store!"
            body = """Nexus 5 is available now, hurry up!
            https://play.google.com/store/devices 
            https://play.google.com/store/devices/details?id=nexus_5_16gb
            """
            mail.send_mail(sender_address, recipients, subject, body)
            self.response.write('email sent!</br>')
        else:
             self.response.write('CANNOT buy :(</br>')
                
class ConfirmUserSignup(webapp2.RequestHandler):
    def get(self):
        self.response.write('test')
        receiver_address = ["tedsunnyday@gmail.com"]
        sender_address = "tedsunnyday@gmail.com"
        subject = "Confirm your registration"
        body = """ TEST
                Nexus 5 is available now, hurry up!
                https://play.google.com/store/devices 
                https://play.google.com/store/devices/details?id=nexus_5_16gb
                """
        mail.send_mail(sender_address, receiver_address, subject, body)
        self.response.write(' done')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/test', ConfirmUserSignup)

], debug=True)
