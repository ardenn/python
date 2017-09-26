import bcrypt


class Account:

    def __init__(self, password):
        self.__pass = password

    def change_pass(self, old_pass, new_pass):
        if bcrypt.checkpw(old_pass.encode("utf-8"), self.__pass):
            self.__pass = bcrypt.hashpw(
                new_pass.encode("utf-8"), bcrypt.gensalt())
            return True
        else:
            return False

passwd = input("Enter your account password: ")
hashed = bcrypt.hashpw(passwd.encode("utf-8"), bcrypt.gensalt())
android = Account(hashed)

while True:
    print("Change your password")
    old = input("Enter Old Password: ")
    new = input("Enter New Password: ")
    if android.change_pass(old, new):
        print("Password changed successfully")
        break
    else:
        print("Sorry! Wrong old password!")
        continue
