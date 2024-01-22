#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != '':
        first = sentence[0]
            return len(sentence), first
        else:
            first = None
            return len(sentence), first
