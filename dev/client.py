class Client:
    """Client for Github"""

    def __init__(self, name,login,password,balance) -> None:
        self.name = name 
        self.login = login
        self.password = password
        self.balance = balance