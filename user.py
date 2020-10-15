class User():
    def __init__(self, client, address, name = None):
        self.client = client
        self.address = address
        self.name = name

    def __rpr__(self):
        return self.name + self.address

    def set_name(self, name):
        self.name = name

    # def set_client(self, new_client):
    #
    # """
    # Associates new socket with User
    # Would be used if a user can sign in again
    # :param new_client: socket
    # :return None
    # """
    #     self.client = new_client
