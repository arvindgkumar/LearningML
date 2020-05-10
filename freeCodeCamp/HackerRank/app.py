print('Hello World') #TODO thi line
character_name = "Arvind"
character_age = 31.0
is_male=False
print(character_name + " is struggler with Coding at this age "+str(character_age))
phrase = "Arvind Academy"
print(phrase.index("Ac"))
print(phrase.replace("Academy","Working"))

friends =["Arvind","Gottapally","Kumar"]
print(friends[-1])
print(friends[-2])

for letter in "Arvind learning":
    print(letter)


number_grid= [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
for row in number_grid:
    for col in row:
        print(col)