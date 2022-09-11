import requests
from tempmailx_godwhitelight.src.email import Email


class TempMail:
    def __init__(self):
        self.req_client = requests.session()

        self.email: str = ''
        self.login: str = ''
        self.domain: str = ''

        self.gen_email()

    def gen_email(self) -> None:
        try:
            self.email = self.do_action({"action": 'genRandomMailbox'})[0]
            self.login = self.email.split('@')[0]
            self.domain = self.email.split('@')[1]
        except Exception:
            raise 'Error have occurred while generating email'

    def do_action(self, params: dict):
        return self.req_client.get('https://www.1secmail.com/api/v1/', params=params).json()

    def fetch_emails(self) -> list[Email]:
        try:
            dat = self.do_action({"action": "getMessages", "login": self.login, "domain": self.domain})

            return [Email(self.login, self.domain, ml['id'], ml['from'], self.do_action) for ml in dat]
        except Exception:
            raise 'Error have occurred while fetching emails'
