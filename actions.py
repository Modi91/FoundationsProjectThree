        # UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = input('What is your name? ')
my_age = input('How old are you? ')
my_bio = input('Tell me something about you. ')
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)
    options()

def options():
            # your code goes here!
    print('-'*20)
    print("Would you like to: ")
    print('1) Create a new club.\n or:')
    print('2) Browse and join clubs.\n or:')
    print('3) View existing clubs.\n or: ')
    print('4) Display members of a club.\n or:')
    print('-1) Close application.')


    c = input()
            
    if c == '1':
        create_club()
    elif c == '2':
        view_clubs()
        join_clubs()
    elif c == '3':
        view_clubs()
    elif c == '4':
        view_club_members()
    elif c == '-1':
        print('GoodBye!')
        quit()
    else:
        c = input('Invalid option')
            

def create_club():
    # your code goes here!
            
    club_name = input('Pick a name for your new club: ')
    club_discription = input('What is your club about? ')
    # club(club_name, discription)
    new_club = Club(club_name, club_discription)
    new_club.recruit_member(myself)
    new_club.assign_president(myself)
    clubs.append(new_club)
    print('Enter the number of people you would like to recruit to your new club (-1 to stop)')
    print('-'*20)
    for i, p in enumerate(population):
        print('[%s] %s' % (i+1 , p.name))
    while True:
        e = input()
        if int(e) >= 1 and int(e) <= len(population):
            new_club.recruit_member(population[int(e)-1])
            print('member added successfully.')
        elif e == '-1':
            break
        else:
            print('Try again..')
        
    text = ("""Here is your club: 
               %s
               %s
               Members:
               """ % (new_club.name, new_club.description) )
    print(text)
    new_club.print_member_list()
    options()





def view_clubs():
    # your code goes here!
    for club in clubs:
        text=("""
            Name: %s
            Description: %s
            Members: %s""" %(club.name, club.description, len(club.member)))
        print(text)


            

def view_club_members():
    # your code goes here!
    flag=False
    view_clubs()
    club_name=input('Enter a club name whos members you want to see: ')
    for club in clubs:
        if club.name.lower() == club_name.lower():
            club.print_member_list()
            flag=True
    if flag==False:
            print("Club name doesn't exist")
            view_club_members()
    options()


            

def join_clubs():
    # your code goes here!
    
    view_clubs()
    flag=False
    club_name = input('Enter the name of a club you want to join: ')
    for club in clubs:
        if club.name.lower() == club_name.lower():
            club.recruit_member(myself)
            flag=True
    if flag==False:
            print("Club name doesn't exist")
            join_clubs()
            
            

def application():
    introduction()
    # your code goes here!
    options()
           



            
