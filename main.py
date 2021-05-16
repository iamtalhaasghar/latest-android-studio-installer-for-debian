# created on 15-May-2021
# iamtalhaasghar
from bs4 import BeautifulSoup
from urllib.request import urlopen
import wget
import os
import tarfile

url = 'https://aur.archlinux.org/packages/android-studio/'
site = urlopen(url)
soup = BeautifulSoup(site.read(), 'html.parser')
packageSources = soup.find(id='pkgsrcslist')

USER_FOLDER = os.path.expanduser('~')

for i in packageSources.find_all('a'):
	link = i.get('href')
	if 'dl.google.com' in link:
		
		#link = 'https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.4.268.tar.xz' # Test download file
		originalFileName = link.split('/')[-1]
		downloadPath = '%s/Downloads/%s' % (USER_FOLDER, originalFileName)
		extractPath = '%s/google' % USER_FOLDER
		
		print('Downloading %s\nNOTE: Do not turn off your computer because the download is not "Resume Again" supported.\nRerun script to start download again if connection goes down for some reason' % originalFileName)
		print('Output Path: ', downloadPath)
		
		filename = wget.download(link, out=downloadPath)
				
		print('\nExtracting %s to %s' % (downloadPath, extractPath))
		tar = tarfile.open(downloadPath)
		
		for member_info in tar.getmembers():
			print ("- extracting: ", member_info.name)
			tar.extract(member_info, extractPath)
		
		tar.close()
		
		print('\ndone')
		print('\nRun android studio using following command:\n%s/android-studio/bin/studio.sh' % extractPath)
		
		break


