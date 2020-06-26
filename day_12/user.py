class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def user_emails(self):
        user_emails = []
        users_db = open('users.db', 'r')
        for user in users_db.readlines():
            print(user)
            user_emails.append(user.strip('\n').split(',')[1].strip())
        users_db.close()
        return user_emails

    def email_unique(self):
        user_emails = self.user_emails()
        print(user_emails)
        if self.email in user_emails:
            return False
        return True

    def save(self):
        if self.email_unique():
            users_db = open('users.db', 'a')
            users_db.write("{}, {}\n".format(self.name, self.email))
            users_db.close()
            return True
        return False
    
    @classmethod
    def all(cls):
        users = []
        users_db = open('users.db', 'r')
        for user in users_db.readlines():
            name = user.split(",")[0]
            email = user.split(",")[1].strip().strip("\n")
            users.append(User(name, email))

        print("got the users: {}".format(users))
        return users