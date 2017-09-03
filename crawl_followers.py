#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import pdb
import time

#api = InstagramAPI("login", "password")
api = InstagramAPI("_______jack______", "pwd")
api.login() # login

# Get tonyhong pk by api.getSelfUsersFollowing()
# PK of tonyhong : 1252702687
# PK of bamsong : 709906896
target_pk = 709906896
target_name = 'bamsong'

def GetFollowersAndRecord(pk, filename, maxid=''):
    if maxid == '':
        # First request without next max_id
        api.getUserFollowers(pk)
    else: api.getUserFollowers(target_pk, maxid=max_id)
    followers = api.LastJson

    with open(filename, 'a') as follower_recorder:
        try:
            for follower in followers["users"]:
                follower_recorder.write(follower["username"]+'\n')

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

prev_max_id = 0
counter = 0
max_id = GetFollowersAndRecord(target_pk, target_name+'_followers.txt')

while True:
    if max_id == 'End': 
        print "Happy finished."
        break
    elif max_id == prev_max_id: time.sleep(200)
    else: counter += 1
    print counter

    prev_max_id = max_id
    max_id = GetFollowersAndRecord(target_pk, 'followers.txt', maxid=max_id)

