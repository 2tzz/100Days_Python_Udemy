class User :
    def __init__(self,user_id , username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self):
        self.followers += 1 
        self.following += 1

    def report (self):

        print (self.id , self.username , self.followers , self.following)


user_1  = User('001' , 'pamkaya')


user_1.report()

user_1.follow()

user_1.report()
