def base10_valueGenerator(input_string,ls):
    if len(input_string)%2==0:
        split1=input_string[:len(input_string)//2]
        split2=input_string[len(input_string)//2:]
        split1.upper()
        split2.upper()
        val1=[]
        val2=[]
        for i in split1:
            val1.append(list[i])

        for i in split2:
            val2.append(list[i])



        the_base10_split1=0
        the_base10_split2=0
        for i in range(0,len(val1)):
            the_base10_split1 += val1[i]*26**(len(val1)-i-1)

        for i in range(0,len(val2)):
            the_base10_split2 += val2[i]*26**(len(val2)-i-1)
        print(f'{split1}({the_base10_split1})')
        print(f'{split2}({the_base10_split2})')

        total_base10 = the_base10_split1 + the_base10_split2
        return total_base10

    else:
        return 0

def base26_valueGenerator(d1,d2,ls):
    run1,run2 = True, True
    d1_quo = d1
    d2_quo = d2

    val1_alph = ''
    val2_alph = ''

    while run1 or run2:
        if run1:
            d1_rem = d1_quo%26
            d1_quo = int(d1_quo/26)

            for key,value in ls.items():
                if value == d1_rem:
                    val1_alph = key + val1_alph


            if d1_quo == 0:
                
                run1 = False


        if run2:
            d2_rem = d2_quo%26
            d2_quo = int(d2_quo/26)

            for key, value in ls.items():
                if value == d2_rem:
                    val2_alph = key + val2_alph

            if d2_quo == 0:
                
                run2 = False


    print(f'{d1}({val1_alph})')
    print(f'{d2}({val2_alph})')

    return val1_alph+val2_alph





def start_con():
    user_input = input('Enter choice: \n1-Base26 to Base10  \n2-Base10 to base 26\n')
    if user_input == '1':

        s=str(input("Enter the alphabet\n"))
        s=s.upper()
        result=base10_valueGenerator(s,list)
        print(result)
    elif user_input == '2':
        d1 = int(input("Enter first base10 value\t"))
        d2=  int(input("Enter first base10 value\t"))

        result = base26_valueGenerator(d1,d2,list)
        print(result)

    else:
        print('wrong choice. Try again')
        start_con()


list={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'v':21,'W':22,'X':23,'Y':24,'Z':25}



start_con()
