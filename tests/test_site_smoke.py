import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.html = self.head = self.title = self.body = False
        self.in_title = False
        self.title_text = []
    def handle_starttag(self, tag, attrs):
        self.html |= tag.lower() == "html"
        self.head |= tag.lower() == "head"
        self.body |= tag.lower() == "body"
        if tag.lower() == "title": self.in_title = self.title = True
    def handle_endtag(self, tag):
        if tag.lower() == "title": self.in_title = False
    def handle_data(self, data):
        if self.in_title: self.title_text.append(data)

class SiteSmokeTest(unittest.TestCase):
    def test_index_has_document_shell_and_nonempty_title(self):
        source = (ROOT / "index.html").read_text(encoding="utf-8")
        parser = PageParser()
        parser.feed(source)
        parser.close()
        self.assertTrue(parser.html)
        self.assertTrue(parser.head)
        self.assertTrue(parser.body)
        self.assertTrue(parser.title)
        self.assertTrue("".join(parser.title_text).strip())

if __name__ == "__main__":
    unittest.main()
