class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def user_emails(self):
        user_emails = []
        with open('users.db', 'r') as users_db:
            for user in users_db.readlines():
                print(user)
                user_emails.append(user.strip('\n').split(',')[1].strip())
        return user_emails

    def email_unique(self):
        user_emails = self.user_emails()
        print(user_emails)
        return self.email not in user_emails

    def email_valid(self):
        # add function logic here, returning False
        # if the email format looks invalid
        email_address = self.email
        split_on_at = email_address.split('@')
        if len(split_on_at) < 2:
            return False

        split_on_dot = [word for word in split_on_at[1].split('.')]
        return len(split_on_dot) >= 2

    def save(self):
        if self.email_unique() and self.email_valid():
            with open('users.db', 'a') as users_db:
                users_db.write("{}, {}\n".format(self.name, self.email))
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