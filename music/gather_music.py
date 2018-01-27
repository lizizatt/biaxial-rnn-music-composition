import urllib2 
import urllib


url = "http://johnwilliams.free.fr/"
response = urllib2. urlopen(url + "midi.php?critere=film") 
html = str(response.read())
midi = ".mid"
ind = html.find(midi)
href = "A HREF=\""
while (ind > -1):
	fullurl = url + html[html.find(href) + len(href) : ind + len(midi)]
	html = html[ind + len(midi) + 1:]
	ind = html.find(midi)

        name = ""
        k = len(fullurl) - len(midi) - 1
        while fullurl[k] != '/':
                name = fullurl[k] + name
                k = k - 1

        print name
	urllib.urlretrieve (fullurl, name + ".mid")
	#<AHREF="download.php?url=midi/findingcoins.mid">
