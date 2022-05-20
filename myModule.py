import math
from xml.etree.ElementPath import find

#HELPERS : 
def check_integers(myArray):
    '''
    checks if an array contain only integers
         parameters : myArray(array) : array of values
         returns : check(bool) :True if all the values are integers, else : False
    '''
    for x in myArray:
        check=isinstance(x,int)
        if not check: # once we found a negative value we exit the loop
            return check
    return check

def check_positive_values(myArray):
    '''
    checks if all the array elements are positive
        parameters : myArray(array) : array of values
        returns : positive_array(bool) : True if all array values are positive, else : False
    '''
    positive_array= False
    for x in myArray:
        if x>0:
            positive_array= True
        else:
            positive_array=False
            return positive_array
    return positive_array

def item_count_list(liste,item):
    '''
    calculates the number of an item occurences in a given list
    '''
    count=0
    for element in liste:
        if(element==item): 
            count+= 1
    return count


#PROBLEM 1 : 
def min_value(values):
    '''
    loop over a list of values and search for the min value in it
        params : values(list)
        returns : min(int)
    '''
    min = values[0]
    for v in values:
        if v< min:
            min = v
    return min


#PROBLEM 2 : 

def sum_of_two_lowest_integers(myArray):
    '''
    Calculates the two lowest positive integers in an array of minimum 4 positive integers
    and print the sum
    we first verrify if the given array doesn't contain any negative or a non integer values
    and make sure it contains atleast 4 values 
        Parameters : myArray(array) : array of minimum 4 positive integers
        
    '''
    if len(myArray)<4 :
        print("Make sure your array contains 4 elements !")
    else:
        is_integers=check_integers(myArray)
        is_positive =check_positive_values(myArray)

        if is_positive and is_integers:
            min1 =min_value(myArray)
            myArray.remove(min1) #we remove the first min value from tha array
            min2= min_value(myArray)
            sum= min1 + min2
            print(" the sum of two lowest positive numbers in" ,myArray)
            print("is :",sum)
        else:
            print("the array contains negative or a non integer values" ,myArray)



#PROBLEM 3: 

def sqrt_binary_search(n, start, limit):
    '''
    Recursive function that returns sqrt of a number using binary search
    we will cal it in the sqrt() function if th input value is a non perfect square
      Parameters : 
           n(int) : positive integer
           start(int) : the index from wich the search begins
           limit(int) : the index from wich the search ends
      Returns :

    '''
 
    mid = (start + limit) / 2
    res = mid * mid
    
    # if mid = sqrt ,return mid
    if ((res == n) or (abs(res - n) < 0.000001)): #we use 6 decimal places as a precision
        return mid
 
    # if res is < n, search on the right half
    elif (res < n):
        return sqrt_binary_search(n, mid, limit)
 
    # Else : search left half
    else:
        return sqrt_binary_search(n, start, mid)
 
# Function to
def sqrt(n):
    '''
     returns the sqrt of a non negative integer

    '''
    if n<0: return -1
    i = 1
    found = False

    while (found == False):
            # if n is a perfect square
            if (i * i == n):
                
                found = True
                return i
         
            elif (i * i > n):
                # sqrt exists in [i-1,i] , we do a recursif binary search in [i-1 , i]
                res = sqrt_binary_search(n, i - 1, i)
                res_trunc =(int(res)) # we can also use the math.trunc() built-in function
                found = True
                return res_trunc
            i += 1


#PROBLEM 4: Search in sorted list

def binary_search(liste,start,limit,target):
    '''
    returns index of the targeted element in a list if it exists using binary search, else : returns -1

              parmeters : liste (list) : sorted list
                          target (int) : the item searched
                          start(int) : index from wich the search starts
                          limit(int) : index in wich the search ends

              returns :   mid(int) : the target's index if found , else :-1
    '''
    #check if the search is not ended
    if limit >= start :

        mid= (start + limit) //2
        #if target exist at the middle of the list
        if liste[mid] == target:
            return mid

        # if the target is greater than the mid value , we search in the right sublist
        elif target > liste[mid]:
            return binary_search(liste,mid+1,limit,target)
        #else we search in the left sublist
        else:
            return binary_search(liste,start,mid-1,target)

    #if the search has ended and the target is not found   
    else:
        return -1



def search(liste,target):
    '''
    search for a target in an array using the binary_search function
    '''
    size = len(liste)
    return binary_search(liste, 0,size,target)

#PROBLEM 5: factorial


def factorial(n):
   '''
   calculates the factorial value of a positive integer recursively
       Parameters : n(int): positive integer
       Return : n : if n=1, else:  returns the factorial value
   '''
   if n == 1:
       return n
   else:
       return n*factorial(n-1) #recursivité


#BONUS PROBLEM :

def findRepeatedDnaSequences(str):
    '''
    Return all the repeated 10-letter long sequences that occur more than once in a DNA molecule
               parameters :
                     str (string) : represent the DNA sequence
               returns :
                     repeated_sequences (list) : a list the repeated 10-letter sequences
    '''
    limit=len(str)-10
    sub_list =[]
    repeated_sequences=[]
    # a loop to slice all the 10-letter substrings in the input string
    for i in range(0,limit):
        sub=str[i:(10+i)]
        sub_list.append(sub)
    
   # a loop to count ocurrences of each substring in the sub_list
    for sub in sub_list:
        count_sub=item_count_list(sub_list,sub)
        if (count_sub >1) and (sub not in repeated_sequences):
            repeated_sequences.append(sub) # store the repeated substring in a list

    return repeated_sequences














