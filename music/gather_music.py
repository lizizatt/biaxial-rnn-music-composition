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
	print fullurl

	urllib.urlretrieve (fullurl, str(ind) + ".mid")
	#<AHREF="download.php?url=midi/findingcoins.mid">