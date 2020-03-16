import random
def make_cards():
    global cards
    cards=[]
    num=[i for i in range(2,11)]
    for _ in ['J','Q','K','A']:
        num.append(_)
    card=[(x,y) for x in ('H','B','D','C') for y in num]
    for i in card:
        cards.append(str(i[0])+str(i[1]))
    cards.append('*BIG')
    cards.append('*SMALL')
    return cards

def get_card():
    card_l=[]
    card_ll=[]
    card_lll=[]
    player_a=random.sample(cards,17)
    for i in cards:
        if i not in player_a:
            card_l.append(i)
    player_b=random.sample(card_l,17)
    for i in card_l:
        if i not in player_b:
            card_ll.append(i)
    player_c=random.sample(card_ll,17)
    for i in card_ll:
        if i not in player_c:
            card_lll.append(i)
    data='玩家A手牌'+str(sorted(player_a))+'\n'+'玩家B手牌'+str(sorted(player_b))+'\n'+'玩家C手牌'+str(sorted(player_c))+'\n'+'剩余手牌'+str(card_lll)
    return data
make_cards()
print(get_card())



