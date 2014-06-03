#!/usr/bin/env python
#coding=utf-8

import sys
reload(sys) 
sys.setdefaultencoding('utf8')

import os
import time
import json

DIR = "./rules/"
SUFFIX = ".rules"

def list_rules():
	rules_list = os.listdir(DIR);
	return rules_list

def read_rule(rule_name):
	fp = open(DIR+rule_name,"r");
	rule_content = fp.read()
	rule_obj = json.loads(rule_content)
	return rule_obj

def delete_rule(rule_name):
	try:
		os.remove(DIR+rule_name+SUFFIX)
		return "success"
	except Exception, e:
		return "fail"


def add_rule(rule_name,url,selector,cookie):
	try:
		rule_obj = dict()
		rule_obj['url'] = url
		rule_obj['selector'] = selector
		rule_obj['name'] = rule_name
		rule_obj['cookie'] = cookie
		fp = open(DIR+rule_name+SUFFIX,"w+")
		rule_content = json.dumps(rule_obj)
		fp.write(rule_content)
		fp.close()
		return "success"
	except Exception, e:
		return "fail"
		


#add_rule("wandoujia","http://www.wandoujia.com/apps/com.secretlisa.beidanci","body > div.container > div.detail-wrap > div.detail-top.clearfix > div.num-list > span:nth-child(1) > i");
# add_rule("XLB","https://www.mintpal.com/market/XLB/BTC","#spanLastPrice","__cfduid=d89d38faf312501122304036416165dee1395979292408; __utma=264820115.202194311.1395979293.1399386482.1399535755.25; __utmz=264820115.1395979293.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); session_id=dkngoiv0njhbsts4ao7mkbh0i7; visid_incap_152969=x4nEeWfATBiAaxIVJhRoktyJiFMAAAAAQUIPAAAAAAAkzhq+qaIvmKasjRKukbQr; MintPal=9utj1ltfgfuinif932avthglh6; visid_incap_152968=W5SOr0tcS+e5Uy2+xCsSSSz1flMAAAAAQUIPAAAAAABcrHXjSntyYOgd2SeyiWvE; incap_ses_200_152968=QjXQPcQIBRzhhEqvE4vGAl+gjVMAAAAAXYSpykYyq4o98WZtrAb7fw==")
