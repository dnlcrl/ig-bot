#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Best Times to Post on Instagram by Day of the Week
Sunday: 5:00 p.m. -> 11:00 PM -> 23:00
Monday: 7:00 p.m. & 10:00 p.m. -> 1 am & 4 am -> 01:00 $ 04:00
Tuesday: 3:00 a.m. & 10:00 p.m. -> 9 pm & 4 am -> 21:00 $ 04:00
Wednesday: 5:00 p.m. -> 11:00 PM  -> 23:00
Thursday: 7:00 a.m. & 11:00 p.m. -> 1 am & 5 am  -> 01:00 & 05:00
Friday: 1:00 a.m. & 8:00 p.m. -> 7 pm & 2 am -> 19:00 & 02:00
Saturday: 12:00 a.m. & 2:00 a.m. -> 6:00 am & 8:00 am -> 06:00 & 08:00
'''


from InstagramAPI import InstagramAPI
from random import randint, uniform, choice
from time import sleep
import tweepy
from datetime import datetime
import os
from urllib import request
from random import shuffle

CONSUMER_KEY = os.environ.get('TW_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TW_CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('TW_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('TW_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

FOLLOWERS_THRESHOLD = 2 * 1000
GRAMITLATER_DIR = os.environ.get('GRAMITLATER_DIR')

IG_USER = os.environ.get('IG_USER')
IG_PASS = os.environ.get('IG_PASS')

SCHEDULE = {
    6: (23,),
    0: (None,),
    1: (1, 4, 21,),
    2: (4, 23,),
    3: (None,),
    4: (1, 5, 19,),
    5: (2, 6, 8,)
}

app = {}

# load hashtags
with open('hashtags', 'r') as f:
    hashtags = f.read().splitlines()
with open('relatedhashtags', 'r') as f:
    relatedhashtags = f.read().splitlines()
shuffle(relatedhashtags)

# load following users
with open('following', 'r') as f:
    following = f.read().splitlines()

following = [int(fo) for fo in following]


def about_an_hour():
    return 5400 + randint(-1800, 1800)


def about_a_minute():
    return 90 + randint(-30, 30)


def about_a_second():
    return uniform(1.5, 2.6)


try:
    ig = InstagramAPI(IG_USER, IG_PASS)
    ig.login()  # login
except Exception as e:
    raise e


def maybe_post_update():
    wd = datetime.today().weekday()
    h = datetime.today().hour
    if 'wd' in app and app['wd'] == wd:
        if 'h' in app and app['h'] == h:
            return
    if h in SCHEDULE[wd]:
        post_updte()
        app['wd'] = wd
        app['h'] = h


def post_updte():
    _dir = GRAMITLATER_DIR
    gram_files = [i for i in os.listdir(_dir) if i.startswith('gramitlater')]
    if len(gram_files) == 0:
        print('No more grams!')
        return
    shuffle(gram_files)
    g = gram_files[0]
    with open(_dir + g, 'r') as f:
        content = f.read()
        g_els = content.split('\n')
        fname = 'media.' + g_els[2].split('.')[-1]
        request.urlretrieve(g_els[2], fname)
        f = request.urlopen(g_els[1]).read()
        tags = ''.join(
            ['#' + t + ' ' for t in relatedhashtags[:randint(2, 4)]])
        caption = g_els[0] + ' #' + g_els[3] + ' ' + tags
        try:
            ig.uploadPhoto(fname, caption)
            os.remove(_dir + g)
            api.update_status(status='%s: Picture uploaded!' % datetime.now())
        except Exception as e:
            import pdb
            pdb.set_trace()
            raise e


def like_and_follow():
    tag = choice(hashtags)
    print('Tag selected: ', tag)
    ig.tagFeed(tag)
    sleep(about_a_second())

    response = ig.LastJson

    items = response["items"]
    users_ids = [item["user"]["pk"] for item in items]
    users_ids = [_id for _id in users_ids if _id not in following]

    for user_id in users_ids[:randint(10, 15)]:
        # numero di follower
        ig.getUsernameInfo(user_id)
        sleep(about_a_second())
        follower_count = ig.LastJson['user']['follower_count']
        print('Follower Conut: ', follower_count)

        if follower_count < FOLLOWERS_THRESHOLD:

            ig.getUserFeed(user_id)
            sleep(about_a_second())
            feed = ig.LastJson['items']
            _ids = [el['id'] for el in feed][:randint(7, 11)]
            for post_id in _ids:
                ig.like(post_id)
                print('Post ', post_id, ' liked!')
                #.update_status(status='%s: Media liked!' % datetime.now())
                sleep(about_a_second())
            ig.follow(user_id)
            following.append(user_id)
            with open('following', 'a') as f:
                f.write('\n' + str(user_id))

            print('User ', user_id, ' followed!')
            try:
                api.update_status(status='%s: User followed!' % datetime.now())
            except Exception as e:
                print('Tweepy error:')
                print(e)
            app['count'] += 1
            print('sleeping a minute or so..')
            sleep(about_a_minute() * 0.75)
    if app['count'] >= app['folbeforesleep']:
        app['folbeforesleep'] = randint(18, 22)
        api.update_status(status='%s: Going to sleep!' % datetime.now())
        print('sleeping an hour or so..')
        sleep(about_an_hour())


def main():
    app['count'] = 0
    app['folbeforesleep'] = randint(18, 22)
    while True:
        try:
            maybe_post_update()
            like_and_follow()

        except Exception as e:
            api.update_status(status='%s: Bot Crashed!!!' % datetime.now())
            raise e

if __name__ == '__main__':
    main()
