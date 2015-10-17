# requirement:python2.7
# more functions will be added in next version

import urllib2


class hosts(object):

    HEADER = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'
    }

    def __init__(self, header=None):
        self.header = header or self.HEADER
        self.reposUrl = 'https://github.com/racaljk/hosts'

    def getRaw(self, url):

        request = urllib2.Request(url, headers=self.header)
        response = urllib2.urlopen(request)
        return response.read()

    def getReadMeFile(self):
        url = 'https://raw.githubusercontent.com/racaljk/hosts/master/README.md'
        content = self.getRaw(url)
        with open('README.MD', 'wb') as f:
            f.write(content)

    def getHostsFile(self):
        url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
        content = self.getRaw(url)
        with open('hosts', 'wb') as f:
            f.write(content)

    def printContributors(self):
        l = ['racaljk', 'andytimes', 'smounives',
             'TimothyGu', 'RellyVadd', 'LyricTian']

        c = [{'author': i,
              'githubpage': 'https://github.com/' + i} for i in l]

        print ':D thanks for all contributors:'
        for x in c:
            for (k, v) in x.items():
                print k + ':' + v
