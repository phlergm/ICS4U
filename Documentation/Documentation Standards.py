#-----------------------------------------------------------------------------
# Name: Humza Anwar
# Purpose: To be a program that includes the use of if statements,
#        looping structures, functions, and arrays to show my
#                   understanding of documentation standards
#
# References:
#
# Author: Humza Anwar
# Created: 20/09/18
# Updated: 1/11/18
#-----------------------------------------------------------------------------    

capricorn = Star_sign('Capricorn',0,0,0,0)
aquarius = Star_sign('Aquarius',0,0,0,0)
pisces = Star_sign('Pisces',0,0,0,0)
aries = Star_sign('Aries',0,0,0,0)
taurus = Star_sign('Taurus',0,0,0,0)
gemini = Star_sign('Gemini',0,0,0,0)
cancer = Star_sign('Cancer',0,0,0,0)
leo = Star_sign('Leo',0,0,0,0)
virgo = Star_sign('Virgo',0,0,0,0)
libra = Star_sign('Libra',0,0,0,0)
scorpio = Star_sign('Scorpio',0,0,0,0)
sagittarius = Star_sign('Sagittarius',0,0,0,0)
capricorn2 = Star_sign('Capricorn',0,0,0,0)

all_Star_signs = [capricorn, aquarius, pisces, aries, taurus, gemini, cancer, 
                  leo, virgo, libra, scorpio, sagittarius, capricorn2]

months_in_year = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "Novermber", "December", "January", "e"]


def find_user_Star_sign(birth_month_index, birth_day):
    '''
    Determines the star sign of the user based on the data entered.

    Parameters
    ----------
    birth_month_index : int
        The user's month of birth
    birth_day : int
        The users day of birthday

    Returns
    -------
    str
        Star sign of the user (e.g. Capricorn)

    '''
    int i = 0
    for x in all_Star_signs:
        user_Star_sign
        if (user_birth_month_index == x.start_month and int(user_birth_day) >=
            x.start_day) or (user_birth_month_index == x.end_month and 
                             int(user_birth_day) <= x.end_day):
            user_Star_sign = x.name_of_sign    
                return user_Star_sign



print("Here are all the star signs, which are you?" )


for x in all_Star_signs:
    print (x.name_of_sign)
	
for x in all_Star_signs:
    x = Star_sign(x.name_of_sign, months_in_year[i], x.start_day, months_in_year[i+1],
                  x.end_day) #Dates do
                            #not follow any rule, set to 0. Will be defined later
    i = i+1

capricorn.start_day = 22
capricorn.end_day = 31 

aquarius.start_day = 20
aquarius.end_day = 18

pisces.start_day = 19
pisces.end_day = 20

aries.start_day = 21
aries.end_day = 19

taurus.start_day = 20
taurus.end_day = 20

gemini.start_day = 21
gemini.end_day = 20

cancer.start_day = 21
cancer.end_day = 22

leo.start_day = 23
leo.end_day = 22

virgo.start_day = 23
virgo.end_day = 22

libra.start_day = 23
libra.end_day = 22

scorpio.start_day = 23
scorpio.end_day = 21

sagittarius.start_day = 22
sagittarius.end_day = 21

capricorn2.start_day = 22
capricorn2.end_day = 31

user_birth_month = input("""What month is your birthday? Make sure to start with a
                   capital letter & spell correctly """)
user_birth_day = input("What day of that month is your birthday ")

user_birth_month_index = months_in_year.index(user_birth_month)

find_user_Star_sign(user_birth_month_index, user_birth_day)
print (user_Star_sign)
