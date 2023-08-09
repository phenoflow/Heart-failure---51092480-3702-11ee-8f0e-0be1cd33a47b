# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"14A6.00","system":"readv2"},{"code":"G58..00","system":"readv2"},{"code":"10079.0","system":"med"},{"code":"10154.0","system":"med"},{"code":"104275.0","system":"med"},{"code":"11424.0","system":"med"},{"code":"1223.0","system":"med"},{"code":"12550.0","system":"med"},{"code":"13189.0","system":"med"},{"code":"17278.0","system":"med"},{"code":"18853.0","system":"med"},{"code":"19066.0","system":"med"},{"code":"2062.0","system":"med"},{"code":"21837.0","system":"med"},{"code":"22262.0","system":"med"},{"code":"23481.0","system":"med"},{"code":"23707.0","system":"med"},{"code":"24503.0","system":"med"},{"code":"26242.0","system":"med"},{"code":"27884.0","system":"med"},{"code":"27964.0","system":"med"},{"code":"2906.0","system":"med"},{"code":"32671.0","system":"med"},{"code":"398.0","system":"med"},{"code":"4024.0","system":"med"},{"code":"46672.0","system":"med"},{"code":"51214.0","system":"med"},{"code":"5141.0","system":"med"},{"code":"52127.0","system":"med"},{"code":"5255.0","system":"med"},{"code":"5695.0","system":"med"},{"code":"57987.0","system":"med"},{"code":"5942.0","system":"med"},{"code":"62718.0","system":"med"},{"code":"68766.0","system":"med"},{"code":"72668.0","system":"med"},{"code":"8464.0","system":"med"},{"code":"884.0","system":"med"},{"code":"8966.0","system":"med"},{"code":"94870.0","system":"med"},{"code":"9524.0","system":"med"},{"code":"9913.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('heart-failure-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["heart---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["heart---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["heart---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
