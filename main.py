import pprint
import re
import time

import html2text
# import spacy
from textblob import TextBlob
import requests
import os

# data_path="files/"
# files=[i.name for i in os.scandir(data_path)]
beds = "https://www.covidbedmbmc.in/HospitalInfo/show"  # "https://coronabeds.jantasamvad.org/beds.html"
icu_beds = "https://coronabeds.jantasamvad.org/all-covid-icu-beds.html"


def bed_availability(beds):
    data = html2text.html2text(requests.get(beds).text)
    time.sleep(2)
    blob = TextBlob(data)
    # print(blob)
    x = blob.split("####")
    # print(x)
    j = [i for i in x if i.startswith(" **")]
    extract_out = []
    for hospital in j:
        try:
            contact = re.findall("[0-9]{10}", hospital)[0]
        except IndexError:
            contact = None
        hospital_name = hospital.split("\n")[0].replace('*', '')
        vacant_index = hospital.split("\n").index('Vacant')
        icu_vacant_index = hospital.split("\n").index('ICU Vacant')
        non_icu_vacant_index = hospital.split("\n").index('Non ICU Vacant')
        # print(vacant_index,icu_vacant_index,non_icu_vacant_index)

        vacant = hospital.split("\n")[vacant_index - 2].replace('*', '').replace(' ', '').replace('_', '')
        icu_vacant = hospital.split("\n")[icu_vacant_index - 2].replace('*', '').replace(' ', '').replace('_', '')
        non_icu_vacant = hospital.split("\n")[non_icu_vacant_index - 2].replace('*', '').replace(' ', '').replace('_',
                                                                                                                  '')
        # print(vacant,icu_vacant,non_icu_vacant)

        extract_out.append((hospital_name, contact, int(vacant), int(icu_vacant), int(non_icu_vacant)))
    return extract_out


if __name__ == "__main__":
    extract_out = bed_availability(beds)
    pprint.pprint(extract_out)
    for i in extract_out:
        if i[1] is not None:
            print('''Hospital: {}
Contact: {}
Total Vacant: {}
ICU Vacant: {}
Non ICU Vacant: {}'''.format(i[0], i[1], i[2], i[3], i[4]))

            print("*" * 50)
# for i in files[:100]:
#     data=html2text.html2text(open(data_path+i).read())
#     # print(data)
#     blob = TextBlob(data)
#     # print(blob.detect_language())
#     out=blob.translate(to='en')#.split('\n')
#     # print(out.split('\n'))
#     # out[6],out[13]=out[13],out[6]
#     # # print(out[22:29])
#     #
#     # for line in out:
#     #     if line.startswith("(4)"):
#     #         address1=out[out.index(line):out.index(line)+7]
#     #         address=address1.copy()
#     #         for check in address1:
#     #             if check.startswith("---") or check.startswith("(5)") or check.startswith("(6)") or check.startswith("(7)"):
#     #                 address.pop(address.index(check))
#     #         else:
#     #             print(address,len(address))
#     #
#     #
#     #         out[out.index(line):out.index(line)+len(address)]=address
#     #
#     #         out='\n'.join(out)
#     with open("data/"+i.split('.')[0]+".txt",'w') as file:
#         file.write(str(out))

# https://www.covidbedmbmc.in/
# https://vasaicoronaresources.net/dashboard/
