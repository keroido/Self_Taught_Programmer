#Challenge9

#1

import os

with open("st.rtf","w") as f:
    f.write("Python　から　こんにちは!")
with open("st.rtf","r") as f:
    print(f.read())

#2
word_list = ["Python", "Java", "computer", "hacker", "painter"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
