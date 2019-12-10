import os, ssl
import sysconfig
import urllib.request
import zipfile
import shutil
    
from distutils.core import setup

if os.name == 'nt':
	# We're on Windows
    url = 'https://github.com/cdaf/windows/archive/master.zip'
    emulate_script = 'cdEmulate.bat'
else:
	# We're on Linux
    url = 'https://github.com/cdaf/linux/archive/master.zip'
    emulate_script = 'cdEmulate.sh'

# Fix for Windows server 2016 core issue. TBD: Change to Requests library
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
    
response, header = urllib.request.urlretrieve(url)

prefix = 'windows-master/'
with zipfile.ZipFile(response) as zip:
    for file in zip.namelist():
        if file.startswith(prefix + 'automation' ):
            if not file.endswith('/'):
                zip.extract(file,'build')
scripts = sysconfig.get_path('scripts')
shutil.rmtree(scripts+'/automation', ignore_errors=True)
shutil.move('build/'+prefix+'automation', scripts+'/automation')
shutil.move(scripts+'/automation/'+emulate_script, scripts+'/'+emulate_script)

setup(name='pycdaf',
    version='0.1-alpha',
    packages=[]
)
