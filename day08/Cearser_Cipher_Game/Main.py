
    ################################simple word decorder $ encorder by 2tzzz#################################################

from art import logo


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


print(logo)

direction = input("type 'encode' to encrypt , type 'decode' to decrypt :\n").lower()



def encode_process(text , shift):
    


    text_list = []
    output_list = []
    char_position = 0
    
    l_count = 0

    for  i in text :
        text_list.append(i)
    
    print(text_list)

    for j in text_list :

        for k in alphabet : 
            

            char_position = alphabet.index(k)
                
            if j == k and (char_position + shift <= 26) :
                
                char_position = char_position + shift
                output_list.append(alphabet[char_position])
                char_position = 0
                

            elif j == k and (char_position + shift > 26):
                
                char_position = char_position + shift - 26
                output_list.append(alphabet[char_position])
                char_position = 0

            elif j != k :
                l_count += 1
                if l_count == 26 :
                    output_list.append(j)

            else :
                output_list.append(' ')
        
        l_count = 0
   
    encr_word = ''
    for l in output_list:
        encr_word += l


    print (f"your encrypted word : {encr_word}")




def decode_process(input_text , reverseshift) :
    
    input_list = []
    output_list2 = []
    char_position2 = 0
    
    l_count = 0

    for  i in input_text :
        input_list.append(i)
    
    print(input_list)

    for l in input_list :

        for n in alphabet : 
            

            char_position2 = alphabet.index(n)
                
            if l == n  :
                
                char_position2 = char_position2 - reverseshift
                output_list2.append(alphabet[char_position2])
                char_position2 = 0
                

            elif l != n :
                l_count += 1
                if l_count == 26 :
                    output_list2.append(l)

            else :
                output_list2.append(' ')
        
        l_count = 0
   
    dec_word = ''
    for l in output_list2:
        dec_word += l


    print (f"your decoded word : {dec_word}")



if direction == 'encode':
    text = input("type your messege : \n").lower()
    shift = int(input("Type the shift number :"))
    encode_process(text , shift)

elif direction == 'decode':
    input_text = input("type your messege to decode : \n").lower()
    reverseshift = int(input("Type the reverseshift number :"))
    decode_process(input_text , reverseshift)


