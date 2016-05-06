#!/usr/bin/env python3
import http.client, html.parser, random, sys
website = "apps.cs.utexas.edu"
filepath = "/unixlabstatus/"

def findbesthost(fav_host=None, threshold=0.3):
    threshold = float(threshold)
    class MyHTMLParser(html.parser.HTMLParser):
        def __init__(self):
            super(MyHTMLParser, self).__init__()
            self.writeenable = False
            self.minload = float("inf")
            self.hosts = []
            self.found_fav = False


        def handle_starttag(self, tag, attrs):
            if tag == "tr":
                self.count = 0
            elif tag == "td":
                self.writeenable = not self.found_fav


        def handle_endtag(self, tag):
            if tag == "td":
                self.writeenable = False


        def handle_data(self, data):
            if self.writeenable:
                data = data.strip()
                if self.count == 0:
                    self.host = data
                elif self.count == 4:
                    if data:
                        try:
                            load = float(data)
                            if self.host == fav_host and load <= threshold:
                                self.hosts = [self.host]
                                self.found_fav = True
                            elif load < self.minload:
                                self.minload = load
                                self.hosts = [self.host]
                            elif load == self.minload:
                                self.hosts.append(self.host)
                        except Exception as e:
                            pass
                self.count += 1

    conn = http.client.HTTPConnection(website)
    conn.request("GET", filepath)
    resp = str(conn.getresponse().read())

    parser = MyHTMLParser()
    parser.feed(resp)

    return random.choice(parser.hosts)

if __name__ == "__main__":
    args = sys.argv[1:]
    print(findbesthost(*args))
