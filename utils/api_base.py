class ApiBase:
    def __init__(self, session, url):
        self.session = session
        self.url = url
        self.response = None

    def api_request(self, method, **kwargs):
        self.response = self.session.request(method, self.url, **kwargs)