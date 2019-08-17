months_in_the_year = ["January", "February", "March", "April", "May", "June", 
					  "July", "August", "September", "October", "Novermber", "December"]

all_star_signs = [Aquarius, Pisces, Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio,
				  Sagittarius, Capricorn]

print("Here are all the star signs, which are you?" )

for x in months_in_the_year: 
	print (str(x))
	
	
	
birth_month = input("""What month is your birthday? Make sure to start with a 
                    capital letter & spell correctly """)
birth_day = input("What day of that month is your birthday ")

birth_month_index = months_in_the_year.index(birth_month) 
