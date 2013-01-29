#!/usr/bin/env python3
import http.client, html.parser, sys, random
website = "apps.cs.utexas.edu"
filepath = "/unixlabstatus/"

error_message = """You must specify 32-bit or 64-bit machine:
$ cshosts.py 32
$ cshosts.py 64"""

def findbesthost(bits):
	assert bits == 32 or bits == 64, error_message
	list = []

	class MyHTMLParser(html.parser.HTMLParser):
		def __init__(self):
			super(MyHTMLParser, self).__init__()
			self.writeenable = False
		def handle_starttag(self, tag, attrs):
			if tag == "tr":
				list.append([])
			elif tag == "td":
				self.writeenable = True
		def handle_endtag(self, tag):
			if tag == "td":
				self.writeenable = False
		def handle_data(self, data):
			if self.writeenable:
				list[-1].append(data)

	conn = http.client.HTTPConnection(website)
	conn.request("GET", filepath)
	resp = str(conn.getresponse().read()).replace("\\n", " ").replace("\\t", " ")

	parser = MyHTMLParser()
	parser.feed(resp)

	computerlist = [[], []]

	i = 0
	for item in list:
		firstcolumn = item[0]
		
		# check for title row of 64-bit section:
		if len(item) == 1:
			if item[0] == " Public Linux Workstations - 64-bit ":
				i = 1	# switch to second subarray of computerlist (for 64-bit machines)
		
		# check for key row
		else:
			if item[0] != "Host" and item[1] != "down":
				assert len(item) == 5
				computerlist[i].append(item) # append computer and associated info to correct subarray of computerlist

	besthost = ""
	bestload = float(sys.maxsize)

	bestlist = []
	for item in computerlist[int(sys.argv[1]) // 32 - 1]:
		load = float(item[4])
		if load <= bestload:
			bestload = load
			bestlist.append(item[0])

	besthost = random.choice(bestlist)
	return besthost

if __name__ == "__main__":
	assert len(sys.argv) == 2, error_message
	bits = None
	try:
		bits = int(sys.argv[1])
	except:
		raise AssertionError(error_message)
	print(findbesthost(bits))
