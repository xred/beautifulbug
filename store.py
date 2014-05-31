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
	os.remove(rule_name)
	return 1

def add_rule(rule_name,url,selector):
	rule_obj = dict()
	rule_obj['url'] = url
	rule_obj['selector'] = selector
	rule_obj['name'] = rule_name
	print DIR+rule_name+SUFFIX
	fp = open(DIR+rule_name+SUFFIX,"w+")
	rule_content = json.dumps(rule_obj)
	fp.write(rule_content)
	fp.close()

# add_rule("wandoujia","http://www.wandoujia.com/apps/com.secretlisa.beidanci","body > div.container > div.detail-wrap > div.detail-top.clearfix > div.num-list > span:nth-child(1) > i");
# add_rule("XLB","https://www.mintpal.com/market/XLB/BTC","#spanLastPrice")
