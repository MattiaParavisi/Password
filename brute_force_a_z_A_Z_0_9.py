import hashlib
import sys

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#alphabets = ['a', 'b', 'c', 'd', 'e']


keywords = ""

i = 0

for alpha1 in alphabets:
    for alpha2 in alphabets:
        for alpha3 in alphabets:
            for alpha4 in alphabets:
                for alpha5 in alphabets:
                    keywords = alpha1+alpha2+alpha3+alpha4+alpha5
                    result1 = hashlib.sha224(keywords.encode())
                    result2 = hashlib.sha256(keywords.encode())
                    result3 = hashlib.sha1(keywords.encode())
                    result4 = hashlib.md5(keywords.encode())
                    print(keywords)
                    #print(type(keywords))
                    #print(type("aaaaa"))
                    if result1.hexdigest().lower() == "44db4be64feb86a9990c1f7fb673ee6102cb51f4495b7f8d86f3e3243a545cb8".lower() :
                        print("TROVATA " + keywords)  
                        sys.exit(0)
                    elif result2.hexdigest().lower() == "44db4be64feb86a9990c1f7fb673ee6102cb51f4495b7f8d86f3e3243a545cb8".lower() :
                        print("TROVATA " + keywords)  
                        sys.exit(0)    
                    elif result3.hexdigest().lower() == "44db4be64feb86a9990c1f7fb673ee6102cb51f4495b7f8d86f3e3243a545cb8".lower() :
                        print("TROVATA " + keywords)  
                        sys.exit(0)
                    elif result4.hexdigest().lower() == "44db4be64feb86a9990c1f7fb673ee6102cb51f4495b7f8d86f3e3243a545cb8".lower() :
                        print("TROVATA " + keywords)  
                        sys.exit(0)  
                    else :
                        print("la parola non e " + keywords)          

                        
