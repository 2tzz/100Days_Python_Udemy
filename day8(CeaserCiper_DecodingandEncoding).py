# def greet():
#     print("hellow")
#     print("how are you")
#     print("bye")


# greet()

# # def greet_with_name(name) :

# #     print(f"hellow {name} !")
# #     print(f"how are you {name} ?")
# #     print(f"bye  {name} !")

# # greet_with_name('thiyura')

# # def life_in_weeks(age):
    
# #     return (90 - age ) * 12 * 4
    
    
# # yourage = int(input("enter your age : "))

# # x=life_in_weeks(yourage)

# # print(f"you have {x} weeks left.")

# def greet_with_location(name,location):

#     print(f"hellow {name} !")
#     print(f"greetings from {location} ! ")


# greet_with_location('thiyura', 'ingiriya')

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("type 'encode' to encrypt , type 'decode' to decrypt :\n").lower()
text = input("type your messege : \n").lower()
shift = int(input("Type the shift number :"))


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


encode_process(text , shift)

def decode_process(input_text , reverseshift) :
    
    input_list = []
    output_list2 = []
    char_position2 = 0
    
    l_count = 0

    for  i in input_text :
        input_list.append(i)
    
    print(input_list)

    for j in input_list :

        for k in alphabet : 
            

            char_position2 = alphabet.index(k)
                
            if j == k and (char_position2 - reverseshift >= 0) :
                
                char_position2 = char_position2 - reverseshift
                output_list2.append(alphabet[char_position2])
                char_position2 = 0
                

            elif j == k and (char_position2 - reverseshift < 0):
                
                char_position2 = char_position2 - reverseshift 
                output_list2.append(alphabet[char_position2])
                char_position2 = 0

            elif j != k :
                l_count += 1
                if l_count == 26 :
                    output_list2.append(j)

            else :
                output_list2.append(' ')
        
        l_count = 0
   
    encr_word = ''
    for l in output_list2:
        encr_word += l


    print (f"your encrypted word : {encr_word}")



