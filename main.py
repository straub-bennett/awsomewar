

import time
import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 20)
dice3 = random.randint(1, 50)
random_event = 0
chance = 0
territory = 0
popsat = 10
print(dice1)

countrys = {'Austria':4,
            'Prussia':7,
            'Russia':8,
            'France':10,
            'Denmark':2,
            'Switzerland':1,
            'Italy':3,
            'Ottoman Empire':6,
            'Spain':4}
x = True
while x == True:
    try:
        user_input = input('would you like to play war? (yes/no): ')
        if user_input.lower() == 'no':
            break
        if user_input.lower() == 'yes':
            print('Starting a new game of war...')
            x = False
    except:
        print('An error occurred. Please try again.')
        time.sleep(1)
y = True
while y == True:
    country = input('What country do you want to play as?  (Prussia/easy, Austria/hard, Ottoman Empire/insane): ')
    if country.lower() == 'prussia':
        print('You have chosen Prussia with easy difficulty.')
        time.sleep(1)
        y = False
        money = 30000
        army = 10000
        stability = 35
        culture = 'German'
        Neighbors = [countrys['Austria'], countrys['Russia'], countrys['France'], countrys['Denmark'], countrys['Switzerland']]
        popsat = 9
        Enemy = countrys['France']
        countrys.pop['Prussia']
    elif country.lower() == 'austria':
        print('You have chosen Austria with hard difficulty.')
        time.sleep(1)
        y = False
        money = 20000
        army = 4000
        stability = 10
        culture = 'austrian/hungarian'
        Neighbors = [countrys['Prussia'], countrys['Russia'], countrys['Italy'], countrys['Ottoman Empire']]  
        Enemy = countrys['Ottoman Empire']
        popsat = 6
        countrys.pop['austria']
    elif country.lower() == 'ottoman empire':
        print('You have chosen Ottoman Empire with insane difficulty.')
        time.sleep(1)
        y = False
        money = 15000
        army = 1000
        stability = 5
        culture = 'Turkish'
        Neighbors = [countrys['Russia'], countrys['Austria'], countrys['Italy'], countrys['Spain']]
        Enemy = countrys['Austria']
        countrys.pop['Ottoman Empire']
        popsat = 4
    else:
        print('Invalid choice. Please try again')
        continue
print(f'You start with ${money}, {army} soldiers, and {stability} stability. your arch enemy is {Enemy} and your people are {popsat * 10}% happy. Good luck!')
print('loading...')
time.sleep(4)
tutorial = input('Would you like a quick tutorial? (yes/no): ')
if tutorial.lower() == 'yes':
    print('In this game, you will manage your country by making strategic decisions to grow your economy, build your army, and maintain stability. Your goal is to become the hegimon of Europe and Asia. The game is turn based, and each turn you will have to make a stratigic desicion to grow your economy, militry, or stability. your economy represents how well you can do other actions such as recruting an army, or increaseing stabiliy, which pretty much represetns the health of your country. Your military represents how well you can defend yourself from other countries or attack them. Good luck and have fun!')
if tutorial.lower() == 'no':
    print('Skipping tutorial...')
    time.sleep(1.5)
time.sleep(2)
print('final loading...')
time.sleep(2.5)
print('now, a key aspect of the game is random events, this is just a random situation, however it can be used to your advantage.')
time.sleep(3.5)
def random_event():
    ''' 
    the function for one of the basic loops in this game, the random event loop
    input: nothing, just happens at the start of each turn
    output: a string that changes one of the variables
    '''
    chance = random.randint(1,6)
    if chance >=3:
        random_event = random.randint(1, 5)
    if round(random_event + stability/20) == 1:
        print('random event: a famine has struck your country, you lose 5 stability and your people have become unhappy')
        stability -= 5
        popsat -= 3
    if round(random_event + stability/20) == 2:
        R_E2 = input('random event: your population threatens revolt, however you can pay them off, will you (y/n)')
        if R_E2 == 'y':
            money -= 5000
            popsat += 2
            print(f'you pay them off and you lose 5000 economy, you now have ${money} left, your pops gain 2 satisfaction, you have {popsat * 10}% popsat')
        if R_E2 == 'n':
            popsat -= 3
            army -= 500
            print(f'your decide to stomp out the revolution but lose some men in the process, you now have {army} soliders and {popsat * 10}% of your people are happy')
    if round(random_event + stability/20) == 3:
        R_E3 = input(f'your rival, {Enemy} threatens war if you dont pay them off')

    



