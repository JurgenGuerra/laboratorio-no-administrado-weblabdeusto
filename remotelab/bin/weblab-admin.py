#!/home/unmsm/remotelab/bin/python2
# -*- coding: utf-8 -*-
import re
import sys
from weblab.admin.script import weblab
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(weblab())
