# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"103732.0","system":"med"},{"code":"105002.0","system":"med"},{"code":"105542.0","system":"med"},{"code":"106008.0","system":"med"},{"code":"106198.0","system":"med"},{"code":"11613.0","system":"med"},{"code":"12366.0","system":"med"},{"code":"15058.0","system":"med"},{"code":"17851.0","system":"med"},{"code":"18793.0","system":"med"},{"code":"19002.0","system":"med"},{"code":"19380.0","system":"med"},{"code":"28649.0","system":"med"},{"code":"30749.0","system":"med"},{"code":"30779.0","system":"med"},{"code":"32898.0","system":"med"},{"code":"32911.0","system":"med"},{"code":"32945.0","system":"med"},{"code":"34213.0","system":"med"},{"code":"46912.0","system":"med"},{"code":"60710.0","system":"med"},{"code":"60721.0","system":"med"},{"code":"64062.0","system":"med"},{"code":"69062.0","system":"med"},{"code":"70619.0","system":"med"},{"code":"71235.0","system":"med"},{"code":"72341.0","system":"med"},{"code":"72386.0","system":"med"},{"code":"72965.0","system":"med"},{"code":"83502.0","system":"med"},{"code":"89650.0","system":"med"},{"code":"90192.0","system":"med"},{"code":"90193.0","system":"med"},{"code":"90935.0","system":"med"},{"code":"92305.0","system":"med"},{"code":"95835.0","system":"med"},{"code":"96484.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('heart-failure-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["heart-failure-history---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["heart-failure-history---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["heart-failure-history---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
