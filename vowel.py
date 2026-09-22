def main():
    x=input("enter text \n")
    
    print(f"there are {vow(x)} vowel in that sentence")
    


def vow(text):
    count=0
    for i in text:
        b =i
        if b =='a':
            count +=1
        elif b=='e':
            count +=1 
        elif b=='i':
            count +=1 
        elif b=='o':
            count +=1 
        elif b=='u':
            count +=1 

    return count

    
main()