class Email:
    def __init__(self, login: str, domain: str, eid: int, sender: str, do_action):
        self.__login = login
        self.__domain = domain
        self.__eid = eid
        self.__sender = sender
        self.do_action = do_action
        self.__data = None

    def fetch_data(self) -> dict:
        try:
            data = self.do_action({"action": "readMessage", "login": self.__login, "domain": self.__domain, "id": self.__eid})

            self.__data = {
                'id': self.__eid,
                'sender': self.__sender,
                'body': data['body'],
                'text': data['textBody'],
                'html': data['htmlBody'],
            }

            return self.__data
        except Exception:
            raise f"Error have occurred while fetching Email[eid={self.__eid}] data"
