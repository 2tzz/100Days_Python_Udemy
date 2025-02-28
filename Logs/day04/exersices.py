import random

random_int = random.randint(1 , 10)

print(random_int)

random_float = random.random() * 10

print (random_float)

random_float = random.uniform(2 , 10 )
print(random_float)


random_int = random.randint(0,1)


if random_int == 1:
    print("Heads")

else :
    print("tails")

friends = ["alice","bob","Charlie","David","Emanuel"]

num = random.randint (0 , 4)

print(friends[num])