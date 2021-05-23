age = str(input("Are you cigarette addict older than 75 years old?: Y/N")).capitalize()

chronic = str(input("Dou you have a severe chronic desease?: Y/N")).capitalize()

immune = str(input("Is your immune system too weak?: Y/N")).capitalize()

if age == "Y" or chronic == "Y" or immune == "Y":
    print ("You are in the risky group")
if age == "N" and chronic == "N" and immune == "N":
    print ("You are not in the risky group")
    