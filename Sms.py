#!/usr/bin/env python -tt
# encoding: utf-8
#
# File: sms.py
#
# Created by Holger Rapp on 2009-03-10.
# Copyright (c) 2009 HolgerRapp@gmx.net. All rights reserved.
#
# Last Modified: $Date$
#

from BeautifulSoup import BeautifulSoup
import cPickle
import cookielib
import os
import re
import urllib2, urllib

#### configuration
username = r"enterusername here!"
password = r"enter password here"

debug = False

class GMXSmsSender(object):
    """
    This class logs into GMX and crawls the site to
    the GMX sending script. It then can send SMS via GMX
    """

    _next_steps = {
        "started": "_login",
        "logged in": "_goto_sms_page",
        "on sms page": "_goto_sms_manager_page",
        "on sms manager page": "_goto_sms_manager_redirect_page",
    }


    def __init__(self):
        policy = cookielib.DefaultCookiePolicy( rfc2965=True, netscape=True )
        cj = cookielib.CookieJar(policy)
        self._opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

        self._status = "started"
        self._logged_in = False

    def next_login_step(self):
        if self._logged_in:
            return

        yield self._status

        while 1:
            ns = self._next_steps.get(self._status, None)

            if ns is None:
                break

            self.__getattribute__(ns)()
            yield self._status

        self._logged_in = True

    def login(self):
        """
        Logs into GMX to send SMS.
        """
        if self._logged_in:
            return

        for status in self.next_login_step():
            pass

    def logout(self):
        """
        Call this when you done with everything. Otherwise GMX
        will show an error then next time you log in
        """
        reply = self._opener.open(self._logout_url)

        self._status = "done"

    @property
    def freesms(self):
        "Returns ( remaining ,total per month)"
        return self._freesms

    def send_sms(self,nr,text):
        self._login()

        nr = re.sub(r'[^\d+]','',nr)
        text = text.encode("latin-1")

        data = {
            "senderType": "number",
            "senderId":   '',
            "receiver":   nr,
            "message":    text,
            "sendLater":  0,
        }
        data = urllib.urlencode( data )

        reply = self._opener.open(self._posturl,data=data)

        if reply.code != 200:
            raise RuntimeError, "Some Problem sending sms"

        site = reply.read()
        if site.find("SMS wurde erfolgreich versendet") == -1:
            raise RuntimeError, "Got a reply, but SMS was not send :("

        self.logout()


    ###########################
    # PRIVATE FUNCTIONS BELOW #
    ###########################
    def _find_logout_link(self, soup):
        logout = soup.find(
            "a", href = lambda x: x and x.find("logout") != -1)
        if logout is None:
            raise RuntimeError, "Couldn't find link to logout page"
        self._logout_url = logout["href"]

    def _find_sms_link(self, soup):
        self._status = "logged in"

        # Find link to sms page
        smsurl = soup.find("a",
                href = lambda x: x and x.find("g.fcgi/sms") != -1)

        if smsurl is None:
            raise RuntimeError, \
                    "Couldn't find link to sms page from mainpage"
        self._smsurl = smsurl["href"]

        if debug:
            print "Found smsurl: %s" % self._smsurl


    def _login(self):
        """
        Logs us into GMX
        """
        user = username
        passwd = password
        try:
            user, passwd = cPickle.load(
                open("%s/.gmxusername.pck" % os.environ["HOME"],"rb"))
        except IOError:
            pass

        data = urllib.urlencode( {"AREA":'1', 'EXT': '', 'EXT2':'',
                'id': user,
                'p': passwd, })

        reply = self._opener.open(
            'https://service.gmx.net/de/cgi/login',data=data)

        text = reply.read()
        if text.find("Ihre Anmeldung zu GMX E-Mail war " \
                     "leider nicht erfolgreich.") != -1:
            raise RuntimeError, "Username or Password wasn't correct!"

        soup = BeautifulSoup(text)

        if debug:
            print "Logged in!"

        # TODO: check reply for "you haven't properly logged out bs"

        self._find_sms_link(soup)
        self._find_logout_link(soup)

        self._status = "logged in"

    def _goto_sms_page(self):
        smsreply = self._opener.open(self._smsurl)
        if smsreply.code != 200:
            raise RuntimeError, \
                    "Opening the SMS page didn't work: %i" % reply.code

        # Find link to popup
        soup = BeautifulSoup(smsreply.read())
        self._smsmanager_url = soup.find("a",
            href=lambda x: x and x.find("sms/manager") != -1)["href"]

        if debug:
            print "Found link to popup: %s" % (self._smsmanager_url)

        if self._smsmanager_url is None:
            raise RuntimeError, "Couldn't find link to SMS Manager (popup)"

        self._status = "on sms page"

    def _goto_sms_manager_page(self):
        manager_reply = self._opener.open(self._smsmanager_url)
        m = re.search(r'''refresh.\s.*url=(.+?)['"]''',manager_reply.read())
        if m is None:
            raise RuntimeError,"Couldn't get the last link to the Interface"
        last_link = m.group(1)
        last_link = last_link.replace("&amp;","&")

        self._sms_manager_redirect_url = last_link

        if debug:
            print "Found last_link: %s" % (last_link)

        self._status = "on sms manager page"


    def _goto_sms_manager_redirect_page(self):
        last_reply = self._opener.open(self._sms_manager_redirect_url)
        if last_reply.code != 200:
            raise RuntimeError, \
                    "Opening the SMS page didn't work: %i" % reply.code

        self._site = last_reply.read()

        # Update our freesms infos
        m = re.search(ur''': noch (\d+) von (\d+)''', self._site)
        self._freesms = tuple(map(int,m.groups()))

        # Get the post url
        self._posturl = "https://www.sms-manager.info/wsm/" + \
                BeautifulSoup(self._site).find("form")["action"]

        self._status = "ready to send"


if __name__ == '__main__':
    from optparse import OptionParser

    def main():
        p = OptionParser("usage: %prog <number> <text>")

        o, args = p.parse_args()

        if len(args) != 2:
            p.error("Need number and text!")

        sms = GMXSmsSender()
        print "Logging in ..."
        sms.login()
        print "Sending SMS ..."
        sms.send_sms(*args)
        print "done."

    main()

