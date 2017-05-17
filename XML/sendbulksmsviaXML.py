#!/usr/bin/python
# coding: utf-8

import pycurl, requests
from StringIO import StringIO
"""
    @author SMS CLUB 
    @url www.smsclub.mobi
    @copyright 2017
"""

"""
    works on python2.7.x (and above) with libriary pycurl (sudo apt-get install python-pycurl)
"""
login = 'login'  #string User ID (phone number)
password = 'pass'  #string Password
alphaName = 'gsm1'    #string, sender id (alpha-name) (as long as your alpha-name is not spelled out, it is necessary to use it)
abonent = '380675126767;380997777662'
text = 'Sending SMS from SMSCLUB via python'
        
xml = "<?xml version='1.0' encoding='utf-8'?><request_sendsms><username><![CDATA["+login+"]]></username><password><![CDATA["+password+"]]></password><from><![CDATA["+alphaName+"]]></from><to><![CDATA["+abonent+"]]></to><text><![CDATA["+text+"]]></text></request_sendsms>"
b = StringIO()

c = pycurl.Curl()
c.setopt(c.URL, 'https://gate.smsclub.mobi/xml/')
c.setopt(c.HTTPHEADER, ['Content-type: text/xml; charset=utf-8'])
c.setopt(c.POSTFIELDS, xml)
c.setopt(c.POST, 1)
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
response = b.getvalue()
c.close()
print response
