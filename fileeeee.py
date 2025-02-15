x = open('newfile.txt', 'r')
print(x.read())

y = open("anotherfile.txt", "w")
y.write("gibberish")

y = open("anotherlife.txt", "w")
y.write("gibberishish\n")

z = open("anotherlife.txt", "a")
z.write("what if i start speaking comprehensive sentences\n")

q = open("newestfile.txt", "w")
q.write("look another new file\n")

import os
# os.remove("anotherfile.txtl")
os.rmdir("gerbeg")