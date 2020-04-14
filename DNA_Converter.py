def AskUser(x):
    #ask for user input store in a list
    value = input('DNA sequence with no spaces is needed: ')
    value = value.lower()
    # using ascii to change letters into numbers
    for character in value:
        number = ord(character) - 96
        x.append(number)

 
# converting DNA to mRNA
def DNA2mRNA (x):
    for n,i in enumerate(x):
        if i == 1:
            x[n]=21
    
        elif i == 20:
            x[n]=1
    
        elif i == 7:
            x[n]=3
    
        else:
            x[n]=7


def splitThree(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  

def mRNA2Amino(x):
    for n,i in enumerate(x): # this is to convert the mRNA to Amino acids
        if i == [21,21,21] or i ==  [21,21,3]:
            x[n]=[95,112,104,101]    #phe

        elif i == [21,21,3] or i ==  [21,21,7] or i ==  [3,21,21] or i ==  [3,21,3] or i ==  [3,21,1] or i ==  [3,21,7]:
            x[n]=[95,108,101,117]    #leu
        
        elif i == [1,21,21] or i ==  [1,21,3] or i ==  [1,21,1]:
            x[n]=[95,105,108,101]    #ile
        
        elif i == [1,21,7]:
            x[n]=[95,109,101,116]    #met

        elif i == [7,21,21] or i ==  [7,21,3] or i ==  [7,21,1] or i ==  [7,21,7]:
            x[n]=[95,118,97,108]     #val
        
        elif i == [21,3,21] or i ==  [21,3,3] or i ==  [21,3,1] or i ==  [21,3,7] or i ==  [1,7,3] or i ==  [1,7,21]:
            x[n]=[95,115,101,114]    #ser
        
        elif i == [3,3,21] or i ==  [3,3,3] or i ==  [3,3,1] or i ==  [3,3,7]:
            x[n]=[95,112,114,111]    #pro

        elif i == [1,3,21] or i ==  [1,3,3] or i ==  [1,3,1] or i ==  [1,3,7]:
            x[n]=[95,116,104,114]    #thr

        elif i == [7,3,21] or i ==  [7,3,3] or i ==  [7,3,1] or i ==  [7,3,7]:
            x[n]=[95,97,108,97]      #ala

        elif i == [21,1,21] or i ==  [21,1,3]:
            x[n]=[95,116,121,114]    #tyr

        elif i == [21,1,1] or i ==  [21,1,7] or i ==  [21,7,1]:
            x[n]=[33,115,116,112]    #stop which will be changed to !stp for simplicity

        elif i == [3,1,21] or i ==  [3,1,3]:
            x[n]=[95,104,105,115]    #his
        
        elif i == [3,1,1] or i ==  [3,1,7]:
            x[n]=[95,103,108,110]    #gln

        elif i == [1,1,21] or i ==  [1,1,3]:
            x[n]=[95,97,115,110]     #asn
        
        elif i == [1,1,1] or i ==  [1,1,7]:
            x[n]=[95,108,121,115]    #lys

        elif i == [7,1,21] or i ==  [7,1,3]:
            x[n]=[95,97,115,112]     #asp

        elif i == [7,1,1] or i ==  [7,1,7]:
            x[n]=[95,103,108,117]    #glu

        elif i == [21,7,21] or i ==  [21,7,3]:
            x[n]=[95,99,121,115]      #cys
        
        elif i == [21,7,7]:
            x[n]=[95,116,114,112]    #trp
            
        elif i == [3,7,21] or i ==  [3,7,3] or i ==  [3,7,1] or i ==  [3,7,7] or i ==  [1,7,1] or i ==  [1,7,7]:
            x[n]=[95,97,114,103]     #arg
            
        else:
            x[n]=[95,103,108,121]    #gly


def main():
    x=[]
    AskUser(x)

    DNA2mRNA(x)

    x = list(splitThree(x, 3)) 

    mRNA2Amino(x)

    # changing it to one list
    flatList = [item
    for elem in x
    for item in elem
    ]

    amino = "" 
    for val in flatList: 
        amino = amino + chr(val) 

 
    amino = (amino.split("!"))
    print (amino)


if __name__ == "__main__":
    main()
