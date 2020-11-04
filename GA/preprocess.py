"""
Process the raw text files

find and separate presidential and senate races  (could add other races)

convert to tab-delimited
"""
import os
import re

RAW_DIR = '/edata/GA/raw'
DATA_DIR = '/edata/GA'
# data is output to /edata/GA/pres and /edata/GA/sen

# we are interested in the second and third sections of the file
# which are the presidential and senate races
# the first section is a summary
sections = ['summary', 'pres', 'sen']

for filename in os.listdir(RAW_DIR):
    if re.search(r'\.txt$', filename):
        m = re.match(r'(.+)\.txt', filename)
        county = m.group(1)
        with open("{}/{}".format(RAW_DIR, filename), 'r') as rawfile:
            section_num = 0
            section_text = ''
            next_line = rawfile.readline()
            while next_line:
                if re.search('Totals:', next_line):
                    section_name = sections[section_num]
                    if section_name in ('pres', 'sen'):
                        outfile = open("{}/{}/{}.txt".format(DATA_DIR, section_name, county), "w")
                        outfile.write(section_text)
                    section_num += 1
                    section_text = ''

                    # now consume 2 blank lines and a header
                    rawfile.readline()
                    rawfile.readline()
                    header = rawfile.readline()

                    # confirm the rep is first then the dem, then lib
                    if not re.search('.*Rep.*Dem.*Lib', header):
                        raise("Unexpected candidate order: {}".format(filename))

                    # if this was the senate we just wrote, we are done
                    if section_name == 'sen':
                        print("Finished with {}".format(filename))
                        break

                else:
                    # now we need to convert the line to be tab-delimited
                    # but the first field might contain spaces
                    m = re.match(r'^([^\d]+)(.*)$', next_line)
                    precinct = m.group(1).strip()
                    fields = re.sub(r' +', '\t', m.group(2))
                    section_text += "{}\t{}\n".format(precinct,fields)
                next_line = rawfile.readline()

