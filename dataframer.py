# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 15:25:27 2017

@author: Syht
"""

import pandas as pd, os, numpy as np

#def dataframer(gazedata, balldata, paddledata):

datadir, tag, subject = 'datadir', '2017-06-26_111238', 'thys'    

gazefile = open(os.path.join(datadir, tag + '_gaze_' + subject + '.txt'), "r")
ballfile = open(os.path.join(datadir, tag + '_ball_' + subject + '.txt'), "r")
paddlefile = open(os.path.join(datadir, tag + '_paddle_' + subject + '.txt'), "r")

glines = gazefile.readlines()
blines = ballfile.readlines()
plines = paddlefile.readlines()

gazefile.close()
ballfile.close()
paddlefile.close()

Tgaze = []
Xgaze = []
Ygaze = []
GazeState = []
Tball = []
Xball = []
Yball = []
Tpaddle = []
Xpaddle = []
Ypaddle = []

for x in glines:
    Tgaze.append(x.split(';')[2])
    GazeState.append(x.split(';')[4])
    Xgaze.append(x.split(';')[5])
    Ygaze.append(x.split(';')[6])

for x in blines:
    Tball.append(x.split(';')[0])
    Xball.append(x.split(';')[1])
    Yball.append(x.split(';')[2].replace('\n',''))

for x in plines:
    Tpaddle.append(x.split(';')[0])
    Xpaddle.append(x.split(';')[1])
    Ypaddle.append(x.split(';')[2].replace('\n',''))

if len(plines) > len(blines):
    Tball = np.hstack((np.zeros(len(Tpaddle)-len(Tball)) + np.nan, Tball))
    Xball = np.hstack((np.zeros(len(Xpaddle)-len(Xball)) + np.nan, Xball))
    Yball = np.hstack((np.zeros(len(Ypaddle)-len(Yball)) + np.nan, Yball))

datasheet = pd.DataFrame(
        {'Tgaze' : Tgaze, 'Xgaze' : Xgaze, 'Ygaze' : Ygaze, 'GazeState' : GazeState,
         'Tball' : Tball, 'Xball' : Xball, 'Yball' : Yball,
         'Tpaddle' : Tpaddle, 'Xpaddle' : Xpaddle, 'Ypaddle' : Ypaddle})

pd.set_option('display.width', 160)
pd.set_option('display.max_rows', len(datasheet))
with open(os.path.join('datadir', tag + '_dataframe_' + subject + '.df'), 'w') as data:
    data.write('%s' %datasheet)