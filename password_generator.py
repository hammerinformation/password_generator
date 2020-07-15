##
#   https://github.com/hammerinformation
##
import random

special_characters=["_","-",">","@","#","€","?","<","[","]",",",";",".","~","'"]

letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
"q","r","s","t","u","v","w","x","y","z"]



     
    

def generate():
    print("Hammerinformation Password Generator")
    characters=[]
    password=""
    print("-"*25)
    
    x=random.randint(10,25);
    for i in range(x):
        if(i%2==0):
            l=random.choice(letters);
            password+=l
            password+=str(random.randint(1,100))
        else:
            l1=random.choice(letters);
            password+=l1.upper();
            password+=random.choice(special_characters);
        
    return password

print(generate())
