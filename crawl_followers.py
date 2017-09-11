#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import pdb
import time
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

#api = InstagramAPI("login", "password")

def GetFollowersAndRecord(api, pk, filename, maxid=''):
    try:
        if maxid == '':
            # First request without next max_id
            api.getUserFollowers(pk, dynamic_header=True)
        else: api.getUserFollowers(pk, maxid=maxid, dynamic_header=True)
    except:
        pdb.set_trace()
        GetFollowersAndRecord(api, pk, filename, maxid=maxid)

    followers = api.LastJson

    with open(filename, 'a') as follower_recorder:
        try:
            for follower in followers["users"]:
                follower_recorder.write(follower["username"]+'\t')

        except KeyError:
            # In this case, 400 HTTP status occured.
            # Therefore data were not loaded.
            # {u'status': u'fail', u'message': u'Please wait a few minutes before you try again.'}
            print "Time to wait more than 3 min."
            return maxid

    try:
        return followers["next_max_id"]
    except KeyError:
        return "End"

def main():
    api = InstagramAPI("_______jack______", "ghdlWk37qkqk*")
    api.login() # login

    req_proxy = RequestProxy()
    proxy_index = 0 
    num_proxies = len(req_proxy.proxy_list)
    api.s.proxies = {"http" : "http://"+req_proxy.proxy_list[proxy_index].get_address()}

    target_name = 'tonyhong1004'
    api.searchUsername(target_name)
    target_pk = api.LastJson['user']['pk']
    prev_max_id = 0
    counter = 0
    max_id = GetFollowersAndRecord(api,target_pk, target_name+'_followers.txt')

    while True:
        if max_id == 'End': 
            print "Happy finished."
            break
        elif max_id == prev_max_id:pdb.set_trace() 
        else: 
            proxy_index = (proxy_index + 1)%num_proxies
            counter += 1
        print counter

        prev_max_id = max_id

        api.s.proxies.update({"http" : "http://"+req_proxy.proxy_list[proxy_index].get_address()})
        api.s.headers.update(dict(req_proxy.generate_random_request_headers().items()))
        # 헤더가 바뀌니깐 로그인도 다시해야하는듯
        api.login(force=True, dynamic_header=True) # login
        #print ("ip: ", api.s.proxies)
        #print ("header: ", api.s.headers)
        max_id = GetFollowersAndRecord(api, target_pk, target_name+'_followers.txt', maxid=max_id)

if __name__=="__main__":
    main()
