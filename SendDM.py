#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

from InstagramAPI import InstagramAPI
import pdb 


if __name__ == "__main__":
    api = InstagramAPI("_______jack______", "pw")
    api.login() # login

    target_user = "bysps"
    api.searchUsername(target_user)
    target_user_info = api.LastJson["user"]
    target_user_pk = target_user_info["pk"]

    api.sendMessage(str(target_user_pk), "안녕 "+ target_user_info["username"] + "나는 봇이야")
