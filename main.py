import myModule as m

def main():

    print("\n------------Test problem 1---------------\n")

    list1 =[5,-10,1,0,12,86,-120,29]
    print ("the min value in",list1," is : ",m.min_value(list1))

    print("\n------------Test problem 2---------------\n")

    list2 = [19,5,42,6,3]
    list_negative = [-5,3,6,12,28]
    list_float = [2.3,12,5,6,4]

    m.sum_of_two_lowest_integers(list2)
    m.sum_of_two_lowest_integers(list_negative)

    m.sum_of_two_lowest_integers(list_float)

    print("\n------------Test problem 3 ---------------\n")
    n= 63
    res = m.sqrt(n)
    if res!= -1 :
        print("the sqrt of ",n ,"is : ",m.sqrt(n))
    else : print("the input value ",n," is negative !")

    print("\n------------Test problem 4 ---------------\n")

    sorted_list= [5,13,16,45,59,100,230,254]
    print("sorted list :", sorted_list)
    target1 = 45
    target2 = 12

    index1 = m.search(sorted_list,target1)
    if index1 == -1:
        print("the targeted value",target1," is not found in the list")
    else:
        print("the index of ",target1," is :",index1)
    
    index2 = m.search(sorted_list,target2)
    if index2 == -1:
        print("the targeted value ",target2,"is not found in the list")
    else:
        print("the index of ",target2," is :",index2)

    print("\n------------Test problem 5  ---------------\n")

    print(" 5! =",m.factorial(5))

    print("\n------------Bonus problem  ---------------\n")

    dna = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print("DNA :",dna)
    print("the repeated sequences :",m.findRepeatedDnaSequences(dna))
    print()



if __name__=="__main__":
    main()