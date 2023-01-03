import random

def play_poker(person):
    play = random.choices([0,1], weights = [85,15])
    if play[0]:
        balance = person.balance
        x = random.choices([i*0.1 for i in range(0,11)], weights = (5,25,20,15,5,5,5,5,5,5,5))
        bet = balance * x[0]
        if bet<10:
            return
        win = random.choices([1.0,-1.0], weights = [17,83])
        person.balance = balance + bet * win[0] * 0.96
        person.sleep = 20
        person.casino_money += bet * win[0] * 0.04
        person.satisfaction += 20
        # print(str(balance)+' poker')

def play_slots(person):
    if person.type in ['hotel-guest','casual-player']:
        play = random.choices([0,1], weights = [95,5])
    if person.type == 'high-roller':
        play = random.choices([0,1], weights = [99.9,0.1])

    if play[0]:
        balance = person.balance
        x = random.choices([i*0.1 for i in range(0,11)], weights = (5,25,20,15,5,5,5,5,5,5,5))
        bet = balance * x[0]
        if bet<5:
            return
        person.balance = balance - bet*(1-0.9151)
        person.sleep = 5
        person.casino_money += bet*(1-0.9151)
        person.satisfaction += 10
        # print(str(person.balance)+' slots')

def play_roulet(person):
    play = random.choices([0,1], weights = [85,15])
    if play[0]:
        balance = person.balance
        x = random.choices([i*0.1 for i in range(0,11)], weights = (5,25,20,15,5,5,5,5,5,5,5))
        bet = balance * x[0]
        if bet<10:
            return
        win = random.choices([1.0,-1.0], weights = [43,57])
        if win[0] == 1.0:
            person.balance = balance + bet * 1.2
            person.casino_money -= bet * 1.2
        if win[0] == -1.0:
            person.balance = balance - bet
            person.casino_money += bet

        person.sleep = 15
        person.satisfaction += 20
        # print(str(balance)+' Roulet')

def play_room(person):
    if person.type in ['hotel-guest','casual-player']:
        play = random.choices([0,1], weights = [99,1])
    if person.type == 'high-roller':
        play = random.choices([0,1], weights = [70,30])

    if person.balance < 200:
        return

    if play[0]:
        person.sleep = 50
        person.satisfaction += 60
        person.balance += - 200
        person.casino_money += 200
        # print(str(person.balance)+' room')

def play_blackjack(person):
    play = random.choices([0,1], weights = [90,10])
    if play[0]:
        balance = person.balance
        x = random.choices([i*0.1 for i in range(0,11)], weights = (5,25,20,15,5,5,5,5,5,5,5))
        bet = balance * x[0]
        if bet<10:
            return
        win = random.choices([1.5,1.0,-1.0], weights = [1,48,51])
        person.balance = balance + bet * win[0]
        person.sleep = 15
        person.casino_money += bet * win[0]
        person.satisfaction += 20
        # print(str(balance)+' blackjack')

def play_bar(person):
    play = random.choices([0,1], weights = [80,20])
    if play[0]:
        free = random.choices([0,1], weights = [90,10])
        if free[0]:
            person.sleep = 5
            person.satisfaction += 50
            # print(str(person.balance)+' bar')
            return
        if person.balance < 10:
            return
        person.sleep = 5
        person.satisfaction += 20
        person.balance += -10
        # print(str(person.balance)+' bar')
