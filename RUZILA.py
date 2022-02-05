import os #importatnt libary
import json

def Location_Main():
    global main_l
    print("Your main location:", os.getcwd())
    main_l= os.getcwd()
    return main_l
Location_Main()



with open("your.json", "r") as jsonFile:
    data_data2 = json.load(jsonFile)

data1={"test":"tes2"}
#Create Json write=======================================================
birinci = {**data_data2, **data1}#merge 2 dictionary

with open("your.json", 'w', encoding='utf8') as f3:
  json.dump(birinci, f3, ensure_ascii=False, indent=1)


# learn_this = os.path.abspath('test.json')