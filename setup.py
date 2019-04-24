import os
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

prefix = 'windows-master/'
response, header = urllib.request.urlretrieve(url)
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
