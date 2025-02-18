def is_prime(num):
    temp1 = 0
    temp2 = 0
    for i in range(2,(num-1)) :

        if num % 1 == 0 and num % num ==0:
            temp1 += 1

        if num % i == 0 :
            temp2 += 1


    if temp1 > 0 and temp2 == 0 :
        return True
    elif num == 2 :
        return True

    elif temp2 > 0 :
        return False
    
         
print (is_prime(2))