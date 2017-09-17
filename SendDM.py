#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

from InstagramAPI import InstagramAPI
import pdb 

def influencer_list(file_path):
    influ_with_meta_list = []
    with open(file_path, "r") as f:
        f.readline()
        for line in f:
            line_list = line.strip().split(',')
            influ_with_meta_list.append(line_list)
    return influ_with_meta_list


if __name__ == "__main__":
    api = InstagramAPI("_______jack______", "pw")
    api.login() # login


    influ_with_meta_list = influencer_list("/Users/jack/roka/InstagramCrawler/api_influ_with_engagement_rate_min/test.csv")
    for influ_with_meta in influ_with_meta_list:
        target_user     = influ_with_meta[0]
        engagement_rate = influ_with_meta[1]
        comment_count   = influ_with_meta[2]
        like_count      = influ_with_meta[3]
        follower_count  = influ_with_meta[4]

        #api.searchUsername(target_user)
        #target_user_info = api.LastJson["user"]
        #target_user_pk = target_user_info["pk"]

        #api.sendMessage(str(target_user_pk), "안녕 "+ target_user_info["username"] + "나는 봇이야")
