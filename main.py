#everything here finished
import random
import time
import sys
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 20)
dice3 = random.randint(1, 50)
random_event = 0
chance = 0
territory = 0
popsat = 10
war = 'not '
stability = 0.0
army = 0
money = 0
random_events = 0
print(dice1)
at_war_with = 'none'
plan = ''
citys = ['Vienna', 'Budapest','Prague', 'Trieste','Krakow','Lviv','Graz','Brno','Berlin', 'Danzig', 'Frankfurt', 'The rhine','Cologne',' Breslau','Essen','Düsseldorf','Hanover','Dortmund','Venice', 'Konstantinopolis', 'Rome','Paris','Egypt']

countrys = {'Austria':4,
            
            'Prussia':7.0,
            'Russia':8.0,
            'France':10.0,
            'Denmark':2.0,
            'Switzerland':1.0,
            'Italy':3.0,
            'Ottoman Empire':6.0,
            'Spain':4.0, 'none': 20}
random_country = list(countrys.keys())
user_input = input('would you like to play war? (yes/no): ')
if user_input == 'yes':
    x = True
while x == True:
    try:
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
        money = 30000
        army = 10000
        stability = 35
        culture = 'German'
        Neighbors = [countrys['Austria'], countrys['Russia'], countrys['France'], countrys['Denmark'], countrys['Switzerland']]
        popsat = 9
        Enemy = 'France'
        citys = ['Berlin', 'Danzig', 'Frankfurt', 'The rhine']
        y = False
    elif country.lower() == 'austria':
        print('You have chosen Austria with hard difficulty.')
        time.sleep(1)
        money = 20000
        army = 4000
        stability = 15
        culture = 'austrian/hungarian'
        Neighbors = [countrys['Prussia'], countrys['Russia'], countrys['Italy'], countrys['Ottoman Empire']]  
        Enemy = 'Ottoman Empire'
        popsat = 6
        d_citys = ['Vienna', 'Budapest','Prague', 'Trieste','Krakow','Lviv','Graz','Brno']
        y = False
    elif country.lower() == 'ottoman empire':
        print('You have chosen Ottoman Empire with insane difficulty.')
        time.sleep(1)
        money = 10000
        army = 1000
        stability = 5
        culture = 'Turkish'
        Neighbors = [countrys['Russia'], countrys['Austria'], countrys['Italy'], countrys['Spain']]
        Enemy = 'Austria'
        popsat = 4
        y = False
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
#finished
def random_event():

    ''' 
    the function for one of the basic loops in this game, the random event loop
    input: nothing, just happens at the start of each turn
    output: a string that changes one of the variables
    '''
    global stability
    global popsat
    global army
    global money
    global random_country
    global random_events
    global war
    global at_war_with
    global plan
    global countrys
    global country
    chance = random.randint(1,6)
    if chance >=3:
        random_events = random.randint(0, 5)
    if round(random_events + stability / 20) == 1:
        print('random event: a famine has struck your country, you lose 5 stability and your people have become unhappy')
        stability = stability - 5
        popsat = popsat - 3
    elif round(random_events + stability / 20) == 2:
        R_E2 = input('random event: your population threatens revolt, however you can pay them off, will you (y/n)')
        if R_E2 == 'y':
            money = money - 5000
            popsat = popsat + 2
            print(f'you pay them off and you lose 5000 economy, you now have ${money} left, your pops gain 2 satisfaction, you have {popsat * 10}% popsat')
        elif R_E2 == 'n':
            popsat = popsat - 3
            army = army - 500
            print(f'your decide to stomp out the revolution but lose some men in the process, you now have {army} soliders and {popsat * 10}% of your people are happy')
    elif round(random_events + stability / 20) == 3:
        R_E3 = input(f'your rival, {Enemy} threatens war if you dont pay them off, will you (y/n)')
        if R_E3 == 'y':
            money = money - 4000
            popsat = popsat - 3
            print('you pay them off, and lose $4000, but your population is unhappy')
        if R_E3 == 'n':
            print(f'{Enemy} has declared war')
            war = ''
            at_war_with = Enemy
    elif round(random_events + stability / 20) == 4:
        R_E4 = input(f'migrants from {Enemy} have found refuge in your country, will you accept them, it may lead to locals getting unhappy (y/n)')
        if R_E4 == 'y':
            popsat = popsat - 1
            money = money + 3000
            war = ''
            at_war_with = Enemy
            print(f'you accept the migrants, but your population becomes unhappy, and {Enemy} has declared war on you!')
        if R_E4 == 'n':
            popsat = popsat + 1
            print(f'you reject the migrants and your population is happy')
    elif round(random_events + stability / 20) == 5:
        R_E5 = input('your population wants a grand celebration for the holidays, will you throw it?(y/n)?')
        if R_E5 == 'y':
            popsat = popsat + 2
            money = money - 4000
            print('you throw a grand celebration, but it takes some investment')
        if R_E5 == 'n':
            popsat = popsat - 2
            money = money + 5000
            print('you keep taxes up, and gain some money, but it hurts your population')
    elif round(random_events + stability / 20) == 6:
        print( f'a king from{random_country[random.randint(0,len(random_country)-1)]} donates $5000')
        money = money + 5000
    elif round(random_events + stability / 20) == 7:
        print(f'some revolutionarys from {Enemy} threaten to join you if you are not paid, while they are shut down some flee to you')
        money = money + 6000
        army = army + 500
    elif round(random_events + stability / 20) == 8:
        R_E8 = input(f'a professional mercinary company from{random_country[random.randint(0,len(random_country))]} offers to join you for a small fee, do you accept(y/n) ')
        if R_E8 == 'y':
            money = money - 4000
            army = army + 6000
            print('you recuit them but it hurts the bank')
        if R_E8 == 'n':
            money = money + 3000
            print('instead of recuiting them, you rob them')
    elif round(random_events + stability / 20) == 9:
        R_E9 = input('a massive earthquake hits a village in your north, do you send money to help them? (y/n)')
        if R_E9 == 'y':
            popsat = popsat - 1
            money = money - 6000
            print('you send some money their way, but they still are a little sad')
        if R_E9 == 'n':
            money = money + 1000
            popsat = popsat - 4
            print('your population is all hurt by this abandonment, and most of them are extremly angry')
    elif round(random_events + stability / 20) == 10:
        R_E10 = print(f'{Enemy} has declared war on you, good luck.')
        war = ''
    else:
        stability = stability - 15
        print('your stability plummets after you lose a political argument')

#finished
def year():
    '''
    Docstring for yearly focus
    input: a choice of what you want to improve/ sacrifice
    output: a string, and some changes in variables
    '''
    global stability
    global popsat
    global army
    global money
    global random_country
    global random_events
    global war
    global at_war_with
    global plan
    global countrys
    global country
    choice = input(f'what do you want to focus on this year? money, army, population, or stability? Or, do you want to declare war?')
    if choice.lower() == 'money':
        money = money + 9000
        popsat = popsat - 1
        print('you raise taxes which leads to your people becoming less happy, but you get money doh')
    elif choice.lower() == 'army':
        money = money - 9000
        army = army + 6000
        print('you invest in a new company for your military')
    elif choice.lower() == 'population':
        popsat = popsat + 3
        money = money - 6000
        print('you lower taxes leading to your population being happy!')
    elif choice.lower() == 'stability':
        stability = stability + 10
        money = money - 5000
        print('you invest in new city walls!')
    elif choice == 'war':
        at_war_with = input(f'who would you like to go to war with, the options are {random_country}')
        print(f'you are now at war with {at_war_with}')
        war = ''
        money = money + 3000
        army = army + 2000
        stability = stability - 4
        popsat = popsat + 1


#finished
def conflict():
    """
    Docstring for conflict
    """
    global stability
    global popsat
    global army
    global money
    global random_country
    global random_events
    global war
    global at_war_with
    global plan
    global countrys
    global country
    while war == '':
        print(f'you are at war with {at_war_with}!!!!!')
        stability -= 2
        army += 500
        money -= 1000
        popsat -= 1
        plan = input('do you want to go on the defence, or offence? (d/o)')
        if plan == 'd':
            stability += 4
            army -= 1000
            money += 1000
            popsat += 1
            print('you go on the defence and gain stability and popsat, but your armys glory seekers quit')

        if plan == 'o':
            stability -= 2
            army += 2000
            money -= 1000
            print('your army gears up for battle. Good luck.')
        battle()
        print(f'after the battle, you have {army} soliders left, and your enemy has {countrys[at_war_with]} strength left')
        time.sleep(2)
    #finished    
def loss():
    global stability
    global popsat
    global army
    global money
    global random_country
    global random_events
    global war
    global at_war_with
    global plan
    global countrys
    global country
    if stability <= 0:
        money -= 10000
        popsat -= 3
        stability += 1
        print('you have lost all stability and your people lose trust in your government, raise it now.')
    if popsat <= 0:
        money -= 8000
        stability -= 4
        popsat += 1
        print('your population is extremly unhappy, and you have to lower taxes, ')
    if money <= 0:
        popsat -= 3
        stability -= 5
        army = 1000
        money += 1
        print('your country goes bankrupt, almost all your soliders quit, and your population is extremly unhappy')
    if money <= 0 and army <= 0 and stability <=0 and popsat<= 5:
        print('your country despretly tries to struggle back to great power status, however your people revolt into open civil war, and your neighbors take the oppertunity to assult you, your country is no more. Try again? ')
        time.sleep(5)
        print('ending game')
        sys.exit()
    
#finished
def battle():
    global stability
    global popsat
    global army
    global money
    global random_country
    global random_events
    global war
    global at_war_with
    global plan
    global countrys
    global country
    print(f'battle starting with {at_war_with}')
    if plan == 'o':
        print(f'you invade {at_war_with}, and they meet you at the battlefield')
        countrys[at_war_with] += 1
        countrys[at_war_with] -= random.randint(0,3) + army/11000
        army -= countrys[at_war_with] * 1200
        stability -= ((countrys[at_war_with] * 5000) - army)/1000
        money -= (countrys[at_war_with] * 1000) - (stability * 200)
        print('you have a battle, and you lose some of your army, and some stability, but your people stay happy, and you keep your money')
    elif plan == 'd':
        print(f'{countrys[at_war_with]} marches onto your turf, you meet them at {citys[random.randint(0,len(citys)-1)]}')
        countrys[at_war_with] -= random.randint(1,2) + army/8000
        popsat -= countrys[at_war_with] - stability / 10
        money -= (countrys[at_war_with] * 2500) - (stability * 350)
        army -= countrys[at_war_with] * 900
        print(f'you have a massive battle on your turf and must pay for damages, but their army is damaged {at_war_with} now has {countrys[at_war_with]}strength left')


def win():
    global stability
    global popsat
    global army
    global money
    global random_country
    global random_events
    global war
    global at_war_with
    global plan
    global countrys
    global country
    random_country = list(countrys.keys())
    if len(random_country) == 0:
        print('you won, and, wow, the game actually works jeez, anyways, congrats you did it, you have become the hegimon of the world and are now seen as the greatest power ever!')
        time.sleep(8)
        print('why are you still here')
        time.sleep(2)
        sys.exit()


def main():
    """
    main loop of game
    """
    global stability
    global popsat
    global army
    global money
    global random_country
    global random_events
    global war
    global at_war_with
    global plan
    global countrys
    global country
    while True:
        print(f'you now have ${money}, {army} soliders, your people are {popsat * 10}% happy, and you are {stability *2}% stable. also you are {war}at war')
        time.sleep(2.5)
        random_event()
        print('loading...')
        time.sleep(3)
        year()
        time.sleep(2)
        loss()
        time.sleep(1)
        conflict()
        countrys[random_country[random.randint(0,len(random_country)-1)]] += 2.2
        print('a random country has developed')
        countrys[random_country[random.randint(0,len(random_country)-1)]] -= 2
        print('a war has lead a random country to lose development')
        if countrys[at_war_with] <= 0:
            countrys.remove([countrys[at_war_with]])
            money += 10000
            popsat += 2
            stability += 10
            army += 5000
            print('you takeover a neighboring country, and gain many benifits')
            at_war_with = ''
            war = 'not'

        



if __name__ == "__main__":
    main()
