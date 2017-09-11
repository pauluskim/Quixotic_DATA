# -*- coding: utf-8 -*-
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

from tqdm import tqdm
from os import listdir
from os.path import isfile, join
reflected_path = "/Users/jack/roka/InstagramCrawler/마이홍_reflected/"
post_list = [f for f in listdir(reflected_path) if isfile(join(reflected_path, f))]

influ_fol = {}

for post in tqdm(post_list, desc="READING"):
    with open(reflected_path+post, 'r') as post_file:
        post_file.readline() # First line is a Full url.
        influencer = post_file.readline().strip() # Second line is the influencer id.
        if not influencer in influ_fol:
            influ_fol[influencer] = post_file.readline().strip().split('\t') # Third line is followers of the influencer.

print "Writing"
with open(reflected_path+"influ_followers_map", "w") as map_file:
    for influencer, followers in influ_fol.iteritems():
        map_file.write(influencer+"\t"+"^".join(followers))
