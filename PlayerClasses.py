import random
from games import  *

class HotelGuest:
    def __init__(self, position = [1,15],ID = 'no name'):
        self.play = True
        self.casino_money = 0
        self.satisfaction = 0
        self.alive = True
        self.sleep = 0
        self.type = 'hotel-guest'
        self.ID = ID
        self.position = position
        self.balance = 200.0
        self.start_balance = 200.0
        self.played = 0 # num of games played


    def LoadOnMap(self,map):
        map[self.position[0]][self.position[1]] = 500
        return map

    def move(self,map,ref_map):

        if self.alive == False:
            return map

        if self.sleep != 0:
            self.sleep += -1
            return map

        UpDown_weights = (20,20,60)
        if self.position[0]>int(len(map[0])*3/4) and self.position[1]>int(len(map[0])/2):
            LeftRight_weights = (80,10,10)
        elif self.position[0]>int(len(map[0])*3/4) and self.position[1]<int(len(map[0])/2):
            LeftRight_weights = (10,10,80)
        else:
            LeftRight_weights = (33,33,33)

        if self.balance/self.start_balance < 0.1:
            self.play == False
            UpDown_weights = (20,10,70)
            if self.position[1]>int(len(map[0])/2):
                LeftRight_weights = (80,10,10)
            else:
                LeftRight_weights = (10,10,80)


        moved = True
        count = 0
        while(moved and count<7):
            UpDown = random.choices([-1,0,1], weights = (20,20,60))
            LeftRight = random.choices([-1,0,1], weights = LeftRight_weights)


            if map[self.position[0]+UpDown[0]][self.position[1]+LeftRight[0]] in [0,1,50,60,70]:
                map[self.position[0]][self.position[1]] = ref_map[self.position[0]][self.position[1]]
                map[self.position[0]+UpDown[0]][self.position[1]+LeftRight[0]] = 500
                self.position = [self.position[0]+UpDown[0],self.position[1]+LeftRight[0]]
                moved = False
            count+=1

        return map

    def CheckForGames(self,ref_map):
        if self.play == False:
            return ref_map
        if ref_map[self.position[0]][self.position[1]] != 50:
            return ref_map

        neighbours = []
        for i in range(-1,2):
            for j in range(-1,2):
                x = ref_map[self.position[0]+i][self.position[1]+j]
                neighbours.append(x)

        if 100 in neighbours:
            play_poker(self)
        if 250 in neighbours:
            play_blackjack(self)
        if 300 in neighbours:
            play_slots(self)
        if 350 in neighbours:
            play_roulet(self)
        if 400 in neighbours:
            play_room(self)
        if 450 in neighbours:
            play_bar(self)




    def exit(self,map,ref_map):
        if self.alive == False:
            return map

        '''if (self.balance/self.start_balance) < 0.90: # exit if you loose 90% of your money
            print('exit-money')
            self.alive = False
            map[self.position[0]][self.position[1]] = ref_map[self.position[0]][self.position[1]]
            return map'''

        if ref_map[self.position[0]][self.position[1]] == 70: # exit if you reach the hotel loby
            # print('exit-hotel')
            self.alive = False
            map[self.position[0]][self.position[1]] = ref_map[self.position[0]][self.position[1]]
            map[1,1] -= 1
            self.satisfaction += 200
            return map

        if ref_map[self.position[0]][self.position[1]] == 60: # exit if you reach the exit
            # print('exit-from-exit')
            self.alive = False
            map[self.position[0]][self.position[1]] = ref_map[self.position[0]][self.position[1]]
            map[1,1] -= 1
            self.satisfaction += 200
            return map

        return map


''' --------------------------  CasualPlayer -------------------------- '''



class CasualPlayer:
    def __init__(self, position = [1,15],ID = 'no name'):
        self.play = True
        self.casino_money = 0
        self.satisfaction = 0
        self.alive = True
        self.sleep = 0
        self.type = 'casual-player'
        self.ID = ID
        self.position = position
        self.balance = 1000.0
        self.start_balance = 1000.0
        self.played = 0 # num of games played


    def LoadOnMap(self,map):
        map[self.position[0]][self.position[1]] = 600
        return map

    def move(self,map,ref_map):

        if self.alive == False:
            return map

        if self.sleep != 0:
            self.sleep += -1
            return map

        UpDown_weights = (42,10,48)
        LeftRight_weights = (45,10,45)
        if self.balance/self.start_balance < 0.1:
            self.play == False
            UpDown_weights = (20,10,70)
            if self.position[1]>int(len(map[0])/2):
                LeftRight_weights = (80,10,10)
            else:
                LeftRight_weights = (10,10,80)

        moved = True
        count = 0
        while(moved and count<7):
            UpDown = random.choices([-1,0,1], weights = UpDown_weights)
            LeftRight = random.choices([-1,0,1], weights = LeftRight_weights)


            if map[self.position[0]+UpDown[0]][self.position[1]+LeftRight[0]] in [0,1,50,60,70]:
                map[self.position[0]][self.position[1]] = ref_map[self.position[0]][self.position[1]]
                map[self.position[0]+UpDown[0]][self.position[1]+LeftRight[0]] = 600
                self.position = [self.position[0]+UpDown[0],self.position[1]+LeftRight[0]]
                moved = False
            count+=1

        return map

    def CheckForGames(self,ref_map):
        if self.play == False:
            return ref_map
        if ref_map[self.position[0]][self.position[1]] != 50:
            return ref_map

        neighbours = []
        for i in range(-1,2):
            for j in range(-1,2):
                x = ref_map[self.position[0]+i][self.position[1]+j]
                neighbours.append(x)

        if 100 in neighbours:
            play_poker(self)
        if 250 in neighbours:
            play_blackjack(self)
        if 300 in neighbours:
            play_slots(self)
        if 350 in neighbours:
            play_roulet(self)
        if 400 in neighbours:
            play_room(self)
        if 450 in neighbours:
            play_bar(self)




    def exit(self,map,ref_map):
        if self.alive == False:
            return map

        '''if (self.balance/self.start_balance) < 0.90: # exit if you loose 90% of your money
            print('exit-money')
            self.alive = False
            map[self.position[0]][self.position[1]] = ref_map[self.position[0]][self.position[1]]
            return map'''

        if ref_map[self.position[0]][self.position[1]] == 70: # exit if you reach the hotel loby
            # print('exit-hotel')
            self.alive = False
            map[self.position[0]][self.position[1]] = ref_map[self.position[0]][self.position[1]]
            map[1,1] -= 1
            self.satisfaction += -200
            return map

        if ref_map[self.position[0]][self.position[1]] == 60: # exit if you reach the exit
            # print('exit-from-exit')
            self.alive = False
            map[self.position[0]][self.position[1]] = ref_map[self.position[0]][self.position[1]]
            map[1,1] -= 1
            self.satisfaction += -200
            return map

        return map






''' --------------------------  High Roller -------------------------- '''



class HighRoller:
    def __init__(self, position = [1,15],ID = 'no name'):
        self.play = True
        self.direction = 'L' # or 'R'
        self.casino_money = 0
        self.satisfaction = 0
        self.alive = True
        self.sleep = 0
        self.type = 'high-roller'
        self.ID = ID
        self.position = position
        self.balance = 10000.0
        self.start_balance = 20000.0
        self.played = 0 # num of games played


    def LoadOnMap(self,map):
        map[self.position[0]][self.position[1]] = 700
        return map

    def move(self,map,ref_map):

        if self.alive == False:
            return map

        if self.sleep != 0:
            self.sleep += -1
            return map


        UpDown_weights = (20,30,50)
        LeftRight_weights = (20,60,20)
        if self.position[0]> len(map[0])/2-5 and self.position[0]< len(map[0])/2+5:
            UpDown_weights = (10,80,10)
            if self.position[1] < len(map[0])/2:
                LeftRight_weights = (50,20,30)
            else:
                LeftRight_weights = (30,20,50)

        if self.balance/self.start_balance < 0.1:
            self.play == False
            UpDown_weights = (20,10,70)
            if self.position[1]>int(len(map[0])/2):
                LeftRight_weights = (80,10,10)
            else:
                LeftRight_weights = (10,10,80)

        moved = True
        count = 0
        while(moved and count<7):
            UpDown = random.choices([-1,0,1], weights = UpDown_weights)
            LeftRight = random.choices([-1,0,1], weights = LeftRight_weights)


            if map[self.position[0]+UpDown[0]][self.position[1]+LeftRight[0]] in [0,1,50,60,70]:
                map[self.position[0]][self.position[1]] = ref_map[self.position[0]][self.position[1]]
                map[self.position[0]+UpDown[0]][self.position[1]+LeftRight[0]] = 700
                self.position = [self.position[0]+UpDown[0],self.position[1]+LeftRight[0]]
                moved = False
            count+=1

        return map

    def CheckForGames(self,ref_map):
        if self.play == False:
            return ref_map
        if ref_map[self.position[0]][self.position[1]] != 50:
            return ref_map

        neighbours = []
        for i in range(-1,2):
            for j in range(-1,2):
                x = ref_map[self.position[0]+i][self.position[1]+j]
                neighbours.append(x)

        if 100 in neighbours:
            play_poker(self)
        if 250 in neighbours:
            play_blackjack(self)
        if 300 in neighbours:
            play_slots(self)
        if 350 in neighbours:
            play_roulet(self)
        if 400 in neighbours:
            play_room(self)
        if 450 in neighbours:
            play_bar(self)




    def exit(self,map,ref_map):
        if self.alive == False:
            return map

        '''if (self.balance/self.start_balance) < 0.90: # exit if you loose 90% of your money
            print('exit-money')
            self.alive = False
            map[self.position[0]][self.position[1]] = ref_map[self.position[0]][self.position[1]]
            return map'''

        if ref_map[self.position[0]][self.position[1]] == 70: # exit if you reach the hotel loby
            # print('exit-hotel')
            self.alive = False
            map[self.position[0]][self.position[1]] = ref_map[self.position[0]][self.position[1]]
            map[1,1] -= 1
            self.satisfaction += 200
            return map

        if ref_map[self.position[0]][self.position[1]] == 60: # exit if you reach the exit
            # print('exit-from-exit')
            self.alive = False
            map[self.position[0]][self.position[1]] = ref_map[self.position[0]][self.position[1]]
            map[1,1] -= 1
            self.satisfaction += 200
            return map

        return map
