def is_prime(num):
    
    for i in range(2,num-1) :
        temp = 0
        if num % 1 == 0 and num % num ==0 and num % i == 0 :
            temp += 1
    if temp != 0 :
        return False
    
    else :
        return True
        
print (is_prime(4))