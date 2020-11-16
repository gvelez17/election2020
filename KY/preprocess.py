"""
Process the raw text files

find and separate presidential and senate races  (could add other races)

convert to tab-delimited
"""
import os
import re

RAW_DIR = '/edata/KY/raw'
DATA_DIR = '/edata/KY'
# data is output to /edata/KY/pres and /edata/KY/sen

# we are interested in the second and third sections of the file
# which are the presidential and senate races
# the first section is a summary
sections = ['summary', 'pres', 'sen']

for filename in os.listdir(RAW_DIR):
    if re.search(r'\.txt$', filename):
        print("Processing {}".format(filename))
        m = re.match(r'(.+)\.txt', filename)
        county = m.group(1)
        line_num = 0
        with open("{}/{}".format(RAW_DIR, filename), 'r') as rawfile:
            section_num = 0
            section_text = ''
            next_line = rawfile.readline()
            line_num += 1
            while next_line:
                if re.search('Totals?:', next_line):
                    section_name = sections[section_num]
                    if section_name in ('pres', 'sen'):
                        outfile = open("{}/{}/{}.txt".format(DATA_DIR, section_name, county), "w")
                        outfile.write(section_text)
                    section_num += 1
                    section_text = ''

                    # if this was the senate we just wrote, we are done
                    if section_name == 'sen':
                        print("Finished with {}".format(filename))
                        break

                    # now consume 2 blank lines and a header
                    rawfile.readline()
                    rawfile.readline()
                    races = rawfile.readline()
                    header = rawfile.readline()
                    line_num += 4

                    # confirm the rep is first then the dem, then lib
                    if not re.search('.*Rep.*Dem.*Lib', races):
                        print("Unexpected candidate order: {}".format(filename))

                    # replace more than one space with a tab
                    header = re.sub(r'  +', '\t', header) 
                    section_text = header

                elif section_num > 0:
                    # now we need to convert the line to be tab-delimited
                    # but the first field might contain spaces and digits
                    # usually the separation is at least 2 spaces but not always
                    # examples:
                    # Miller-Eldridge L Miller Elem 3455 
                    # Chamblee 2      3137
                    # 01 Bethlehem Community Center 3359
                    # Grovetown Public Safety Station 23696  (special case - the 2 is part of the name)
                    try:

                        # anything non-greedy with no more than 2 trailing digits  followed by the first two spaces and then a digit
                        m = re.match(r'^(.+?)  (\d.*)$', next_line)
                        precinct = m.group(1).strip()
                        if re.search(r' \d+\d$', precinct):
                            raise("Too many trailing digits to be a precinct name")
                    except:
                        try:
                            m = re.match(r'^(Grovetown Public Safety Station 2)(.+)$', next_line)
                            if not m:
                                # accept possibly digits followed by non-digits followed by one space then digit 
                                m = re.match(r'^([\d-]*[^\d]+) (\d.*)$', next_line)
                            precinct = m.group(1).strip()
                        except:
                            print("Cannot parse: {}".format(next_line))
                            print("Line number: {}".format(line_num))
                            raise
                    fields = re.sub(r' +', '\t', m.group(2)).strip()
                    section_text += "{}\t{}\n".format(precinct,fields)
                next_line = rawfile.readline()
                line_num += 1

