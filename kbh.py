import webget
import pprint

urllist = ["http://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv"]
webget.download(urllist)

with open('befkbhalderstatkode.csv') as file_object:
    STATISTICS = {}

    # making a list of strings
    lines = file_object.readlines()

    # removing first string (the headers)
    lines.pop(0)

    # converting the list of strings to a list of intarrays
    listofintarrays = []
    for line in lines:
        strarr = line.split(",")
        strarr[-1] = strarr[-1].rstrip()
        for idx in range(len(strarr)):
            strarr[idx] = int(strarr[idx])
        listofintarrays.append(strarr)

    # using loops to fill the STATISTICS dictionary
    for item in listofintarrays:
        if item[0] in STATISTICS:
            continue
        else: STATISTICS[item[0]]={}
    
    for item in listofintarrays:
        if item[1] in STATISTICS[item[0]]:
            continue
        else: STATISTICS[item[0]][item[1]]={}
    
    for item in listofintarrays:
        if item[2] in STATISTICS[item[0]][item[1]]:
            continue
        else: STATISTICS[item[0]][item[1]][item[2]]={}

    for item in listofintarrays:
        STATISTICS[item[0]][item[1]][item[2]][item[3]] = item[4]

    pprint.pprint(STATISTICS[2015][1])


