

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


# code with functions.

# the things in the
def find_word(list, word="lion"):
    print("finding {0}.".format(word))
    for phrase in list:
        if word in phrase:
            print(phrase)

find_word(list_2)
find_word(list_2, "fire")





