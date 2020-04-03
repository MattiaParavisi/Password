import hashlib
import sys

alphabets = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

keywords = ""

for alpha1 in alphabets:
    for alpha2 in alphabets:
        for alpha3 in alphabets:
            for alpha4 in alphabets:
                for alpha5 in alphabets:
                    keywords = alpha1+alpha2+alpha3+alpha4+alpha5
                    print(keywords)
                    if keywords == "azzzz" :
                        print("TROVATA " + keywords)  
                        sys.exit(0)
                             

                        
