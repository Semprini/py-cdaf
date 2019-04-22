import os

from distutils.core import setup

def find_packages(srcdir):
    package_list = []
    badnames=["__pycache__",]
    for root, dirs, files in os.walk(srcdir):
        if not any(bad in root for bad in badnames):
            if "__init__.py" in files:
                package_list.append( root.replace("/",".").replace("\\",".").strip('.') )
    return package_list

if os.name == 'nt':
	# We're on Windows
	cdaf_packages = find_packages('automation_windows/')
else:
	# We're on Linux
	cdaf_packages = find_packages('automation_linux/')
	
	

setup(name='cdaf',
    version='0.1-alpha',
    packages=cdaf_packages
)
