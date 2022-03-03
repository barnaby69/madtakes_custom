# importing datetime

from datetime import datetime

# key datetime variables

now = datetime.now()
hour = now.hour

# checking the time of day

if hour < 12:
    greeting = "Good morning"
elif hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

# system greets the user

print("--------------------------------------------------------------------------------")
print(greeting, "\n")
print("Welcome to the Cody Ko sentence generator", "\n")
print("Like mad:)libs but custom made", "\n")
print("For this file you are required to input 17 words", "\n")
print("Once you have typed in a word and hit enter you won't be able to change it", "\n")

# system asks the user what variables they want

noun_1 = input("Please input a noun:    ")
name_1 = input("Please input a name:    ")
name_2 = input("Please input another name:  ")
pronoun_1 = input("Please input pronoun (he, she or they) or the second name you listed:    ")
time_1 = input("Please input a time in the year:    ")
time_2 = input("Please input another time in the year:  ")
adverb_1 = input("Please input a adverb ending in ly:   ")
noun_2 = input("Please input a noun:    ")
verb_1 = input("Please input a verb ending in ing:  ")
noun_3 = input("Please input a plural noun: ")
verb_2 = input("Please input a verb:    ")
adverb_2 = input("Please input a adverb:    ")
noun_4 = input("Please input a noun:    ")
noun_5 = input("Please input another noun:  ")
adjective_1 = input("Please input a adjective:  ")
verb_3 = input("Please input a verb:    ")
verb_4 = input("Please input another verb:  ")

# system generates and writes out the custom transcript were c_b = custom block of text

c_b_1 = 'When did you create {n_1} {na_1} asked.' \
    .format(n_1=noun_1, na_1=name_1)
c_b_2 = 'I created it in {t_1} er {t_2} actually {na_2} replied {adv_1}.' \
    .format(na_2=name_2, t_1=time_1, t_2=time_2, adv_1=adverb_1)
c_b_3 = '\"It was kind of a personal project. I just wanted to {v_1} my skills with {n_2}.' \
    .format(n_2=noun_2, v_1=verb_1)
c_b_4 = 'You know {v_2} {n_3} is not a new idea it\'s been around for a long time' \
    .format(n_3=noun_3, v_2=verb_2)
c_b_5 = 'but I though I will just {v_3} it {adv2}.' \
    .format(v_3=verb_3, adv2=adverb_2)
c_b_6 = 'I will do {n_4} frictionless\".' \
    .format(n_4=noun_4)
c_b_7 = 'It automatically adds a {n_5} to any ones {n_3} said {na_1}.' \
    .format(n_5=noun_5, n_3=noun_3, na_1=name_1)
c_b_8 = 'Are you {adj_1}? {na_1} asked before adding did you {v_4} {n_4} your self.' \
    .format(adj_1=adjective_1, na_1=name_1, v_4=verb_4, n_4=noun_4)
c_b_9 = '\"I am pretty {adj_1}. I don\'t know\" {na_2} replayed adding that {p_1} did indeed {v_3} {n_4} himself' \
    .format(adj_1=adjective_1, na_2=name_2, v_3=verb_3, n_4=noun_4, p_1=pronoun_1)

custom_transcript_p1 = "{0}{1}{2}{3}{4}{5}{6}".\
    format(c_b_1, "\n", c_b_2, "\n", c_b_3, "\n", c_b_4, "\n", c_b_5, "\n", c_b_6, "\n", c_b_7, "\n")
custom_transcript_p2 = "{0}{1}".format(c_b_8, "\n", c_b_9)
print("Modified transcript snippet: ", "\n")
print(custom_transcript_p1, "\n", custom_transcript_p1, "\n")

# system prints the original transcript were o_b = original block of text

o_b_1 = "When did you create I'd cap that?"
o_b_2 = "I created it in February er March actually Cody replied."
o_b_3 = "It was kind of a personal project. I just wanted to improve my skills with IOS SDK."
o_b_4 = "You know captioning photos is not a new idea it\'s been around for a long time"
o_b_5 = "but I though I will just do it better."
o_b_6 = "I will do it frictionless\"."
o_b_7 = "It automatically adds a caption to any ones photos said the reporter."
o_b_8 = "Are you funny? The reporter asked before adding did you create it your self."
o_b_9 = "\"I am pretty funny. I don\'t know\"  replayed Cody Ko adding that he did indeed make it himself"
cody_transcript_o_p1 = "{0}{1}{2}{3}{4}{5}{6}". \
    format(o_b_1, "\n", o_b_2, "\n", o_b_3, "\n", o_b_4, "\n", o_b_5, "\n", o_b_6, "\n", o_b_7, "\n", o_b_8, "\n", o_b_9)
cody_transcript_o_p2 = "{0}{1}".format(o_b_8, "\n", o_b_9)
print("Original transcript snippet ", "\n")
print(cody_transcript_o_p1, "\n", cody_transcript_o_p2)
