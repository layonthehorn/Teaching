

# lists to be shared by both
list_1 = ["My house is on fire.", "My, my you are a cute lion.", "Lion, tiger and bears.", " What a dark day.",
          "Stuck in the sky", "More fire and dragon's breath.", "lions need snuggles."]
list_2 = ["A lion in time.", "What happened to the cat upstairs?", "Vern's untimely demise",
          "Vern suffered some bad radiation poisoning.", "A lion's best friend is sedatives.", "Burn em' out."]

# code without functions

print("finding lion.")
for phrase in list_1:
    if "lion" in phrase:
        print(phrase)

print("finding lion")
for phrase in list_2:
    if "lion" in phrase:
        print(phrase)

# how you define a function



# code with functions.

# the things in the def are parameters
def find_word(list, word):
    print("finding {0}.".format(word))
    for phrase in list:
        if word in phrase:
            print(phrase)


# The things in the call are called arguments.
find_word(list_2, "lion")
find_word(list_2, "lion")

# calling with too many or too few arguments
find_word(list_1, list_1, "Vern")
find_word(list_2)

# Default parameters
def find_word_default(list, word="lion"):
    print("finding {0}.".format(word))
    for phrase in list:
        if word in phrase:
            print(phrase)


find_word_default(list_1)
find_word_default(list_1, "fire")


# Arbitrary Arguments
def arbitrary_function(*args):
    for i in args:
        print(i)


arbitrary_function("lion", "cute", "lions")

# empty function
def empty_function():
    pass

empty_function()


# functions that return something or a fruitful function
def return_function():
    return "A returned string"


# a function that does not return or a unfruitful function
def non_return_function():
    print("a non-returned string.")


print(return_function())
non_return_function()

# lambda functions
# Use lambda functions when an anonymous function is required for a short period of time.
lambda_function = lambda number: number - 1


def proper_def(number):
    return number - 1


print(lambda_function(5))
