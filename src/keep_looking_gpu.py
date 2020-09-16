'''
	> File Name: test.py
	> Author: tuzhuo
	> Mail: xmb028@163.com 
	> Created Time: Tue 15 Sep 2020 10:07:25 AM CST
'''

import time
import subprocess
import numpy as np
import tensorflow as tf
from manager import GPUManager
# from keras.layers import LSTM
gm=GPUManager()

'''
with gm.auto_choice(mode=0):
    # x = tf.placeholder(tf.float32, shape=(None, 20, 64))
    # y = LSTM(32)(x)
    # print(gm.auto_choice(mode=1))
    x=0
'''

while(1):
    localtime = time.asctime( time.localtime(time.time()) )
    gpu_index = gm.choose_no_task_gpu()
    if gpu_index >= 0 :
        print('Mission Start Running @ %s'%(localtime));

        # gpu_index = 0

        cmd_1 = 'CUDA_VISIBLE_DEVICES=' + str(gpu_index) + ' ' + 'python /public/home/ztu/projects/basenji-old/bin/basenji_sat_bed2.py -f /public/home/WBXie/tuzhuo/tzhuo/genome/NIPP.fasta -l 400 --rc -t /public/home/ztu/projects/nxiepo/2/yuanjian/bw54-list.txt -o /public/home/ztu/projects/nxiepo/lwh_predict/lbd/h5_result -n lbd /public/home/ztu/projects/nxiepo/2/training/ZS97_params.txt /public/home/ztu/projects/nxiepo/2/training/r-zs-54/model_best.tf /public/home/ztu/projects/nxiepo/lwh_predict/lbd/lbd.bed'

        # cmd_ = 'python ./test_code.py'
        subprocess.call(cmd_1, shell=True)

        cmd_2 = 'python /public/home/ztu/projects/nxiepo/lwh_predict/lbd/plot_sat_bed_h5_lots_seqs_Parallel.py -p 20 -i /public/home/ztu/projects/nxiepo/lwh_predict/lbd/h5_result/lbd.scores.h5 -o /public/home/ztu/projects/nxiepo/lwh_predict/lbd/motif_plot/n_54_samples -t /public/home/ztu/projects/nxiepo/2/yuanjian/bw54-list.txt -l 20 -r 50'
        subprocess.call(cmd_2, shell=True)

        break;
    else:
        print('Keep Looking @ %s'%(localtime),end = '\r')
        continue;

print('Mission Complete ! Checking GPU Process Over ! ')

