from .ApiData import A

__url__ = 'https://data.shuvtai.cn/'


class URL(A):
    def __init__(self, _url):
        A.__init__(
            self,
            {
                'chat': _url + '/chat',
                'new': _url + '/new',
                'apply': _url + '/apply',
            }
        )
        self.chat = _url + '/chat'
        self.new = _url + '/new'
        self.apply = _url + '/apply'
