#!c:\virtual\vir1\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'coreapi-cli==1.0.6','console_scripts','coreapi'
__requires__ = 'coreapi-cli==1.0.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('coreapi-cli==1.0.6', 'console_scripts', 'coreapi')()
    )
