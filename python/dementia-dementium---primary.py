# Siobhan Reilly, Ivan Olier, Claire Planner, Tim Doran, David Reeves, Darren M Ashcroft, Linda Gask, Evangelos Kontopantelis, 2024.

import sys, csv, re

codes = [{"code":"Eu02300","system":"readv2"},{"code":"Eu02200","system":"readv2"},{"code":"Eu02100","system":"readv2"},{"code":"Eu02500","system":"readv2"},{"code":"Eu01100","system":"readv2"},{"code":"Eu02400","system":"readv2"},{"code":"E004.11","system":"readv2"},{"code":"299 B","system":"readv2"},{"code":"2901D","system":"readv2"},{"code":"299 G","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('dementia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["dementia-dementium---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["dementia-dementium---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["dementia-dementium---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
