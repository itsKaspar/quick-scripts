from glob import iglob
import shutil
import os

PATH = r'C:\Windows\System32'

destination = open('allfiles.dll', 'wb')
for filename in iglob(os.path.join(PATH, '*.dll')):
    shutil.copyfileobj(open(filename, 'rb'), destination)
destination.close()
