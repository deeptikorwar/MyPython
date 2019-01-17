import webbrowser #the webbrowser module

ChUrl="https://github.com/google/java-photoslibrary/blob/master/samples"
#ChUrl="https://www.google.com.au"

#change code to read a .md file, find all the URLs and find broken links

#webbrowser.open(ChUrl)

#exception webbrowser.Error

import urllib2

try:
    urllib2.urlopen(ChUrl)
    g = urllib2.urlopen(ChUrl)
    print(g.getcode())
except urllib2.HTTPError as e:
    print(e.code) # can add counter or line number variable here
    print(e.reason)
    if e.code == 404 or 403:
        print("Check your hyperlink: {}".format(ChUrl))
except urllib2.URLError as f:
    print(f.args) # can add counter or line number variable here
