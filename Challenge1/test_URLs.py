from urllib.error import HTTPError
import urllib.request

# simple method returns the HTTP response code
# 200 is a successful response.
# urllib.request raises an exception if the site is not up,
# but the response code is contained in the HTTPError.
def getSiteResponse(site):
    try:
        return urllib.request.urlopen(site).getcode()
    except HTTPError as err:
        return err.code

# this test reads URLs from a file and tests them one at a time
# for this example, the only URL is 'https://www.google.com/'
def test_urlsFromFile(): 
    lines = open('URLList.txt').readlines()
    lines = [line.rstrip() for line in lines]
    badurls = []
    
    for line in lines:
        httpcode = getSiteResponse(line)
            
        if 200 != httpcode:
            badurls.append(line + " " + str(httpcode))
            
    if len(badurls) > 0:
        [print(url) for url in badurls]
        assert len(badurls) == 0