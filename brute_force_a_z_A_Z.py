import hashlib
import sys

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#alphabets = ['a', 'b', 'c', 'd', 'e']


keywords = ""

i = 0

for alpha1 in alphabets:
    for alpha2 in alphabets:
        for alpha3 in alphabets:
            for alpha4 in alphabets:
                for alpha5 in alphabets:
                    for alpha6 in alphabets:
                        keywords = alpha1+alpha2+alpha3+alpha4+alpha5+alpha6
                        result1 = hashlib.sha224(keywords.encode())
                        result2 = hashlib.sha256(keywords.encode())
                        result3 = hashlib.sha1(keywords.encode())
                        result4 = hashlib.md5(keywords.encode())
                        print(keywords)
                        #print(type(keywords))
                        #print(type("aaaaa"))
                        if result1.hexdigest().lower() == "94d8fe2cffbe16b26a3ac857188c729bd3a43544f808ea69cf237f13d25a213a".lower() :
                            print("TROVATA " + keywords)  
                            sys.exit(0)
                        elif result2.hexdigest().lower() == "94d8fe2cffbe16b26a3ac857188c729bd3a43544f808ea69cf237f13d25a213a".lower() :
                            print("TROVATA " + keywords)  
                            sys.exit(0)    
                        elif result3.hexdigest().lower() == "94d8fe2cffbe16b26a3ac857188c729bd3a43544f808ea69cf237f13d25a213a".lower() :
                            print("TROVATA " + keywords)  
                            sys.exit(0)
                        elif result4.hexdigest().lower() == "94d8fe2cffbe16b26a3ac857188c729bd3a43544f808ea69cf237f13d25a213a".lower() :
                            print("TROVATA " + keywords)  
                            sys.exit(0)  
                        else :
                            print("la parola non e " + keywords)          

                        