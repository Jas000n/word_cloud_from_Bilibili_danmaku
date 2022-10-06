import os
import re
def _getfiles(dirPath):
    # open directory 
    files = os.listdir(dirPath)
    # re match *.xls/xlsx，you can change 'xlsx' to 'doc' or other file types.
    ptn = re.compile('.*\.xml')
    for f in files:
        res = ptn.match(f)
        if(res):
            return f


_getfiles(".")