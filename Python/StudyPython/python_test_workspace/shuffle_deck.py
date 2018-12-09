import random

nums = list(range(1,11)) + 'Jack Queen King'.split()
suits = 'Heart Diamonds Clubs Spades'.split()

deck = [(x,v) for x in nums for v in suits]

print(deck,len(deck))
print("Begin!")
alls = {"lantian":[],"taqini":[],"DaDa":[],"chenpeng":[]}
while len(deck):
    for i in alls.keys():
        alls[i].append(deck.pop())

print("lantian:",alls["lantian"])
print("taqini:",alls['taqini'])
print("DaDa:",alls['DaDa'])
print("chenpeng:",alls['chenpeng'])
