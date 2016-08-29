import argparse
parser = argparse.ArgumentParser()
#parser.add_argument('--in', action='store', dest='inputFileName')



parser.add_argument('--in', action="store", dest='inputFileName')
parser.add_argument('--out', action='store', dest='outputFileName')
#filename = r'/Users/pataridus/python/input/input_cdn.csv'

arguments = parser.parse_args()

filename = arguments.inputFileName
fd = open(filename,'rt')

outfile = arguments.outputFileName
fdout = open(outfile, 'wt')

lines = fd.readlines()
#print lines
fdout.write('cdn,profile,url\n')

#server
server = 'http://cdn.goprimetime.info'
server2 = 'http://cdn2.goprimetime.info'
server3 = 'http://dl.goprimetime.info'

#clients
apple_tv = '.m3u8'
hls_3g = '.m3u8'
hls_wifi = '.m3u8'
tv = 'Manifest'
web = 'Manifest-wh.mpd'
mobile_3g = 'Manifest-m.mpd'
mobile = 'Manifest-mh.mpd'
android_3g = 'Manifest-md.mpd'
android = 'Manifest-mdh.mpd'
chromecast = 'Manifest-cc.mpd'
comigo = 'Manifest-cc.mpd'
nano = 'Manifest-stb.mpd'
est_download = 'file.json'
temp_download = 'file.json'
samsung_tv = '-en-tv.ism/Manifest'

url = []
for line in lines:
	cdn = line.strip().split(',')
	#cdn
	url.append(cdn[0])
	#profile namw
	url.append('Apple TV')

	#print items
	#url = sprintf("http://%s/%s", server, cdn)
	#url
	url1 = "%s/video/1/%s/0/%s%s\n" % (server, cdn[0], cdn[0], apple_tv)
	url.append(url1)
	url.append('HLS 3G')
	url2 = "%s/video/2/%s/0/%s%s\n" % (server, cdn[0], cdn[0], hls_3g)
	#url2 = "%s/video/1/%s/0/%s%s" % (server, cdn[0], cdn[0], hls_3g)
	#url2 = "%s/%s/%s" % (server, cdn[0], web)
	url.append(url2)
	url3 = "%s/video/3/%s/0/%s%s\n" % (server, cdn[0], cdn[0], web)
	url.append('Web')
	url.append(url3)
	#profile = ','.join(url)
		
	profile = ','.join(url)
print profile
fdout.write(profile)
fdout.write('\n')	
	
	






