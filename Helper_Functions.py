import json
import numpy as np
import pandas as pd
import os

###########################################################
#Input: Filename (either full path or simply file name)

#Output: positional data, associated event data, associated event keys
def Load_Data(fname):
    if fname.find('open-data') == -1:
        path = 'open-data/data/three-sixty/' + fname #path to positional data
        epath = 'open-data/data/events/' + fname  #path to associated event data
    else:
        path= fname
        epath ='open-data/data/events/' + fname[fname.find('s/') + 2:]
        
    
    
    with open(path,'r') as f:
        data = f.read()
    try:
        pdata = json.loads(data)
    except:
        try:
            data = data.replace('\x00lse','')
            data = data.replace('\x00','')
            pdata = json.loads(data)
        except:
            ##### Cleaning up errors in 360 data #####
            
            try:
                with open(path,'r') as f:
                    data = f.read()
                data = data.replace('\x00 0.0, 80.0 ],\n  "freeze_frame" : [','0.0, 80.0 ]},')
                data = data.replace('\x00','')
                pdata = json.loads(data)
            except:
                with open(path,'r') as f:
                    data = f.read()
                    
                    
                    
                d = data.replace('\x00r" : false,\n    "keeper" : false,\n    "location" : [ 89.65213668295611, 43.49361697801779 ]\n  },','"freeze_frame":[')
                d = d.replace(' "visible_area" : [ 61.0396536912917, 80.0, 58.7798520016688, 11.5724945829715, 82.5839064198706, 0.0, 83.8\x00',' "visible_area" : [ 61.0396536912917, 80.0, 58.7798520016688, 11.5724945829715, 82.5839064198706, 0.0, 83.8],')
                d = d.replace('\x00','')
                pdata = json.loads(d)
    with open(epath,'r') as f:
        data = f.read()
    edata = json.loads(data)
    event_keys = {datum['id']  : n for n,datum in enumerate(edata)}
    
    return pdata,edata,event_keys


##########################################################

# Input: datum from 360 data

# Outputs: vectors of positions, whether they are teammates with the actor, whether the player was a goalkeeper and whether the player was the actor

def Get_Positions(datum):
    locs = []
    teams= []
    actor = []
    keepers = []
    ff = datum['freeze_frame']
    for f in ff:
        locs.append(f['location'])
        teams.append(f['teammate'])
        keepers.append(f['keeper'])
        actor.append(f['actor'])
    return np.array(locs),np.array(teams),np.array(keepers),np.array(actor)

########################################################

# Input: datum from 360 data, event data, event keys

# Outputs: associated event

def Get_Associated_Event(datum,edata,event_keys):
    return edata[event_keys[datum['event_uuid']]]


############################################################
def Load_Test_Data(file, half=1):
    data = pd.read_csv(file).to_numpy()[3:]
    data_output = np.zeros((len(data),22))
    ball_pos = np.zeros((len(data),2))
    count = 0
    cball = np.array([0.5,0.5])
    n = 0
    for nn,datum in enumerate(data):
        if datum[0] == 3-half:
            continue
        count+=1
        n+=1
        curr = 0
        for m in range(3,len(datum)-2):
            if datum[m] == datum[m]:
                data_output[n,curr] = datum[m]
                curr+=1
                if curr == 22:
                    break

        for m in range(len(datum)-2,len(datum)):
            if datum[m] == datum[m]:
                ball_pos[n,m-(len(datum)-2)] = datum[m]
                cball[m-(len(datum)-2)] = datum[m]
            else:
                ball_pos[n,m-(len(datum)-2)] = cball[m-(len(datum)-2)] 

    data_output[:,np.arange(22)%2 == 0]*=120
    data_output[:,np.arange(22)%2 == 1]*=80

    ball_pos[:,0]*=120
    ball_pos[:,1]*=80
    data_output = data_output[:count]
    ball_pos = ball_pos[:count]



    a_outfielders = data_output[:,np.abs(np.arange(22) -0.5) > 1]
    a_gk = data_output[:,np.abs(np.arange(22) -0.5) < 1]
    
    return a_outfielders,a_gk,ball_pos


##########################################################################


