class Secret:

    def __init__(self, secret, password):
        self.__secret = secret
        self.__password = password

    def get_secret(self, password):
        if password == self.__password:
            print(self.__secret)
        else:
            print("GO AWAY MOM")

my_secret = Secret("Sit down, Be humble", "kendrick")
my_secret.get_secret("kendrick")
my_secret.get_secret("lamar")
