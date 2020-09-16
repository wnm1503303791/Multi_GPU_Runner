'''
	> File Name: test.py
	> Author: tuzhuo
	> Mail: xmb028@163.com 
	> Created Time: Tue 15 Sep 2020 10:07:25 AM CST
'''

import sys
import time
import subprocess
import numpy as np
import tensorflow as tf
from manager import GPUManager
import random
from optparse import OptionParser
# from keras.layers import LSTM
gm=GPUManager()

parser = OptionParser()
parser.add_option('-i', dest='cmd_file', default=None)
(options, args) = parser.parse_args()

mission_queue = []
if (options.cmd_file != None):
    cmds =  open(options.cmd_file)
    line = cmds.readline()
    while(line):
        line = line.strip()
        if ('python' in line):#仅支持python语言的GPU计算任务
            mission_queue.append(line)
        line = cmds.readline()
    cmds.close()

if (len(mission_queue) <= 0):
    sys.exit(0)

while(1):
    gpu_av = gm.choose_no_task_gpu()
    if len(gpu_av) >= 0 :
        gpu_index = random.sample(gpu_av, 1)[0]

        while(len(mission_queue) > 0):
            localtime = time.asctime( time.localtime(time.time()) )
            cmd_ = 'CUDA_VISIBLE_DEVICES=' + str(gpu_index) + ' ' + mission_queue.pop(0)
            print('Mission : %s\nRUN ON GPU : %d\nStarted @ %s\n'%(cmd_, gpu_index, localtime))
            subprocess.call(cmd_, shell=True)

        break
    else:
        print('Keep Looking @ %s'%(localtime),end = '\r')
        continue;

print('Mission Complete ! Checking GPU Process Over ! ')

