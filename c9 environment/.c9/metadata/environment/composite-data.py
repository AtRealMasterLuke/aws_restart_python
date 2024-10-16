{"filter":false,"title":"composite-data.py","tooltip":"/composite-data.py","undoManager":{"mark":32,"position":32,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":3},"action":"remove","lines":["\"\"\"","Your module description","\"\"\""],"id":55}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":11},"action":"insert","lines":["import csv","import copy"],"id":56}],[{"start":{"row":1,"column":11},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":57}],[{"start":{"row":2,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["myVehicle = {","    \"vin\" : \"<empty>\",","    \"make\" : \"<empty>\" ,","    \"model\" : \"<empty>\" ,","    \"year\" : 0,","    \"range\" : 0,","    \"topSpeed\" : 0,","    \"zeroSixty\" : 0.0,","    \"mileage\" : 0","}"],"id":58}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":36},"action":"insert","lines":["for key, value in myVehicle.items():"],"id":59}],[{"start":{"row":12,"column":36},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":60},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":38},"action":"insert","lines":["print(\"{} : {}\".format(key,value))"],"id":61}],[{"start":{"row":13,"column":38},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":62},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":63}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":64}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["",""],"id":65},{"start":{"row":13,"column":38},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":38},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":66},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "],"id":67},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":68},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "],"id":69},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"remove","lines":["",""]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":13,"column":38},"end":{"row":14,"column":0},"action":"remove","lines":["",""],"id":70}],[{"start":{"row":13,"column":38},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":71},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "],"id":72}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":20},"action":"insert","lines":["myInventoryList = []"],"id":73}],[{"start":{"row":15,"column":20},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":74}],[{"start":{"row":16,"column":0},"end":{"row":36,"column":42},"action":"insert","lines":["with open('car_fleet.csv') as csvFile:","    csvReader = csv.reader(csvFile, delimiter=',')  ","    lineCount = 0  ","    for row in csvReader:","        if lineCount == 0:","            print(f'Column names are: {\", \".join(row)}')  ","            lineCount += 1  ","        else:  ","            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  ","            currentVehicle = copy.deepcopy(myVehicle)  ","            currentVehicle[\"vin\"] = row[0]  ","            currentVehicle[\"make\"] = row[1]  ","            currentVehicle[\"model\"] = row[2]  ","            currentVehicle[\"year\"] = row[3]  ","            currentVehicle[\"range\"] = row[4]  ","            currentVehicle[\"topSpeed\"] = row[5]  ","            currentVehicle[\"zeroSixty\"] = row[6]  ","            currentVehicle[\"mileage\"] = row[7]  ","            myInventoryList.append(currentVehicle)  ","            lineCount += 1  ","    print(f'Processed {lineCount} lines.')"],"id":75}],[{"start":{"row":15,"column":20},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":76}],[{"start":{"row":37,"column":42},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":77},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]},{"start":{"row":38,"column":4},"end":{"row":39,"column":0},"action":"insert","lines":["",""]},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":45},"action":"insert","lines":["currentVehicle = copy.deepcopy(myVehicle)"],"id":78}],[{"start":{"row":39,"column":45},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":79},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]},{"start":{"row":40,"column":4},"end":{"row":41,"column":0},"action":"insert","lines":["",""]},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":41,"column":4},"end":{"row":44,"column":22},"action":"insert","lines":["for myCarProperties in myInventoryList:","    for key, value in myCarProperties.items():","        print(\"{} : {}\".format(key,value))","        print(\"-----\")"],"id":80}],[{"start":{"row":41,"column":43},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":81},{"start":{"row":42,"column":0},"end":{"row":42,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":42,"column":8},"end":{"row":43,"column":0},"action":"remove","lines":["",""],"id":82},{"start":{"row":42,"column":8},"end":{"row":42,"column":12},"action":"remove","lines":["    "]},{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"remove","lines":["f"]}],[{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"insert","lines":["f"],"id":83}],[{"start":{"row":42,"column":50},"end":{"row":43,"column":0},"action":"insert","lines":["",""],"id":84},{"start":{"row":43,"column":0},"end":{"row":43,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":43,"column":12},"end":{"row":44,"column":0},"action":"remove","lines":["",""],"id":85},{"start":{"row":43,"column":12},"end":{"row":43,"column":16},"action":"remove","lines":["    "]},{"start":{"row":43,"column":12},"end":{"row":43,"column":16},"action":"remove","lines":["    "]}],[{"start":{"row":43,"column":46},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":86},{"start":{"row":44,"column":0},"end":{"row":44,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":44,"column":12},"end":{"row":45,"column":0},"action":"remove","lines":["",""],"id":87},{"start":{"row":44,"column":12},"end":{"row":44,"column":16},"action":"remove","lines":["    "]},{"start":{"row":44,"column":12},"end":{"row":44,"column":16},"action":"remove","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":44,"column":12},"end":{"row":44,"column":12},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1728763352415,"hash":"01807d0e84e48ce023ae41f256be839254b263f6"}