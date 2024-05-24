from calc_func import do_addition,do_subraction
def main():
    print("welcome to calulater ")
    print ("""
           \nselect the fuction
           1.add
           2.sub
           """ )
    
    user_input= input("select the fuction")

    a=int(input("value of a "))
    b=int(input("value of b "))

    if user_input=="1":
        result =do_addition(a,b)
    elif user_input=="2":
        result= do_subraction(a,b)

    print('Result:',result)

if __name__ == "__main__":
    main()