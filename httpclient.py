import re


class HttpClient(object):

    def __init__(self, url):
        self.url = url

    def _html_format(self, html_text):
        p = re.compile(r'<[^>]*?>')
        format_text = p.sub('', html_text)
        return format_text
