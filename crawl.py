import urllib2,urllib
from HTMLParser import HTMLParser
import Queue
from Queue import Queue
import urlparse
from urlparse import urljoin

###########functions#######################

#### complete_url(url)----> checks for the validity of the url and return the complete url
#	thigs to be checked:-
#		1) '#'
#		2) 'mailto' 
#		3) relative url
#		4) complete url
#-----> can be done by urljoin(base,link) function provided by urlparse module

#### check_dup(url)-----> checks if url is already present or not in url_list

#setting proxy connection
proxy = urllib2.ProxyHandler({'http': 'http://dibya:dibya78@proxy.iitk.ac.in:3128'})
auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
urllib2.install_opener(opener)
#proxy connection made

#declaring variables
wordsearch = ['important','date','submission','deadline']
url_list = Queue()
url_list_all = []
priority_list = Queue()
found = 0;
curr_page_url = "";
curr_depth = 0;max_depth=3		#max limit 3


# get the first url

#enque first link
#url_list.put('http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=24592&copyownerid=2');
#url_list.put('http://2011.comad.in/');
#url_list.put('http://docs.python.org/2/tutorial/errors.html');
url_list.put('')
url_list.put('-----c-----');
print url_list.queue
url_list_all.append('http://groups.drupal.org/node/290703');
############################################################
class MyHTMLParser(HTMLParser):

	def handle_starttag(self,tag,attrs):

		if tag == "a":
			for attr in attrs:
            			if attr[0] == "href":
					url = urljoin(curr_page_url,attr[1])
					if (url not in url_list_all):#check for duplicate.
						print url						
						url_list.put(url)
						url_list_all.append(url)
						print url


	#def handle_endtag(self, tag):
        #	print "End tag  :", tag

	#def handle_data(self, data):
        #	print "Data     :", data

##############################################################

parser = MyHTMLParser()

while(url_list.empty() == 0 and curr_depth < max_depth):

	curr_page_url = url_list.get()
	print '___________',curr_page_url,'___________'
	if(curr_page_url == '-----c-----'):
		 url_list.put('-----c-----')
		 curr_depth = curr_depth+1
	else:
		#fetching link
		#curr_page_url = urlparse.urlsplit(curr_page_url)
		#curr_page_url = curr_page_url.geturl()
		f = urllib2.urlopen(curr_page_url)

		#storing html page in temporary web1 file
		of = open('web1','w')
		of.write(f.read())
		of.close()

		#opening saved html page for parsing
		fin = open('web1','r')

		#parsing the page for hrefs only
		for line in fin.readlines():
			
			parser.feed(line)
	

#	step 0:
#		checking the page for specific keywords



'''
	step 1:
		getting all absolute fresh urls from the page and save them in a stack(BFS)
	step 2:
		recursive calls to all urls till a certain depth
'''
