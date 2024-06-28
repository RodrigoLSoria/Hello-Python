# string concatenation (aka hot to put strings together)
# goal: create a string that says = "subscribe to ______________"

# youtuber = "Rodrigo López Soria, tu developer de confianza" # some string variable

# #couple of ways to do this
# print("subscribe to" + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! it makes me so excited all the time because \
    I love to {verb1}, stay hydrated and {verb2} like you are {famous_person}."

madlib = "Computer programming is so {}! it makes me so excited all the time because \
    I love to {}, stay hydrated and {} like you are {}.".format(adj, verb1, verb2, famous_person)

print(madlib)
