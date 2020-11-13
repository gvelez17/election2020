import os

COUNTY_MAP = {
        'adair': 'https://results.enr.clarityelections.com//KY/Adair/106381/270022/reports/detailtxt.zip',

             }

RAW_DIR = '/edata/KY/raw'
os.chdir(RAW_DIR)
# loop thru links and put them in the dir
for (cty, url) in COUNTY_MAP.items():
    os.system('curl {} -o {}/{}.zip'.format(url, RAW_DIR, cty))
    cmd = 'unzip {}/{}.zip'.format(RAW_DIR, cty)
    print(cmd)
    os.system(cmd)
    cmd = 'mv detail.txt {}.txt'.format(cty)
    print(cmd)
    os.system(cmd) 

