#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import pdb
from tqdm import tqdm
import mmap
import time

def main():
    target_id = "tonyhong1004"
    hashtags = ["#마이홍", "#myhong"]
    filepath = "/Users/jack/roka/Instagram-API-python/"+target_id+"_followers.txt"
    resultpath = "/Users/jack/roka/Instagram-API-python/"+target_id+"_converted_users.txt"
    progress = "/Users/jack/roka/Instagram-API-python/"+target_id+"_progress.txt"
    counter = 0
    with open(progress, 'r') as progress_file:
        progress_num = int(progress_file.readline().strip())
    with open(filepath, 'r') as follower_file, open(resultpath, 'a') as result_file:
        line_num = 0
        for line in tqdm(follower_file, total=get_num_lines(filepath)):
            line_num += 1
            if line_num <= progress_num: continue
            user_id = line.strip()
            if has_hashtag(user_id, hashtags, progress_num):
                result_file.write(user_id+"\n")
                counter += 1
            progress_num += 1
            with open(progress, 'w') as progress_file: progress_file.write(str(progress_num))
        result_file.write(str(counter))

def has_hashtag(user_id, hashtags, progress_num):
    do_crawl = True
    while do_crawl:
        if not 'max_id' in locals(): curl_url = "https://www.instagram.com/"+user_id+"/?__a=1"
        else : curl_url = "https://www.instagram.com/"+user_id+"/?__a=1&max_id="+max_id
        response = requests.get(curl_url)

        if response.status_code == 404: return False # Not current user.
        elif response.status_code == 403:
            # IP Blocking. SO we need to wait.
            print str(progress_num) + " : Have to wait cause of 403 status" 
            time.sleep(200)
            continue
        
        try:
            media_json = response.json()["user"]["media"]
        except:
            pdb.set_trace()
        for node in media_json["nodes"]:
            if not "caption" in node: continue
            if any(tag in node["caption"] for tag in hashtags):
                # Conversion !!
                return True

        if media_json["page_info"]["has_next_page"]:
            max_id = media_json["page_info"]["end_cursor"]
            do_crawl = True
        else: do_crawl = False

    return False

def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines


if __name__ == "__main__":
    main()
