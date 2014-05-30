#!/usr/bin/env python
#coding=utf-8

import sys
reload(sys) 
sys.setdefaultencoding('utf8')

import os
import time
import json

def list_rules():
	rules_list = os.listdir("./rules");
	print rules_list

def read_rule(rule_name):
	fp = open(rule_name,"r");
	rule_content = fp.read()
	rule_obj = json.loads(rule_content)
	return rule_obj

def delete_rule(rule_name):
	os.remove(rule_name)
	return 1

def add_rule(rule_name,url,selector):
	rule_obj = dict()
	rule_obj['url'] = url
	rule_obj['selector'] = selector
	fp = open(rule_name,"w+")
	rule_content = json.dumps(rule_obj)
	fp.write(rule_content)
	fp.close()

add_rule("./rules/google.rules","http://google.com","div>body")


# read_rule("./rules/baidu.rules")
# delete_rule("./rules/google.rules")

time.sleep(10)