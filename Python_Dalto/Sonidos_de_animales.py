sounds = {
    "gato":"maullido",
    "perro":"ladrido",
    "vaca":"mu",
    "cerdo":"oink"
}

answer = input("Que animal desea escuchar:  ")
if answer in sounds:
    print(sounds[answer])
else:
    print("No conozco el animal")