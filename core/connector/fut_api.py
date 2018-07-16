import fut


class FutApi:
    def __init__(self):
        email = 'pototskyvanya@gmail.com'
        password = 'Kolasa621963'
        secret = 'kolasa'
        platform = 'xbox360'

        self.session = fut.Core(email=email, passwd=password, secret_answer=secret, platform=platform, debug=True, cookies='../connector/cookies.txt', token='../connector/token.txt')

    def get_session(self):
        return self.session
