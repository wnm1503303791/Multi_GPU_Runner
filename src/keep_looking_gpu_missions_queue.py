'''
	> File Name: test.py
	> Author: tuzhuo
	> Mail: xmb028@163.com 
	> Created Time: Tue 15 Sep 2020 10:07:25 AM CST
'''

'''
这个代码能做到多进程并行
'''

import time
import subprocess
import numpy as np
import tensorflow as tf
from manager import GPUManager
import random
# from keras.layers import LSTM
gm=GPUManager()

'''
cmd_1 = 'CUDA_VISIBLE_DEVICES=' + str(gpu_index) + ' ' + 'python /public/home/ztu/projects/basenji-old/bin/basenji_sat_bed2.py -f /public/home/WBXie/tuzhuo/tzhuo/genome/NIPP.fasta -l 400 --rc -t /public/home/ztu/projects/nxiepo/2/yuanjian/bw54-list.txt -o /public/home/ztu/projects/nxiepo/lwh_predict/lbd/h5_result -n lbd /public/home/ztu/projects/nxiepo/2/training/ZS97_params.txt /public/home/ztu/projects/nxiepo/2/training/r-zs-54/model_best.tf /public/home/ztu/projects/nxiepo/lwh_predict/lbd/lbd.bed'
'''

mission_queue = []
#for i in range(3):
if(1):
    #以下的cmd_用于测试目的，真正使用的时候将cmd换成自己需要执行的GPU任务命令即可
    cmd_ = 'python ./fizzbuzz.py > fizzbuzz_1'
    mission_queue.append(cmd_)
    cmd_ = 'python fizzbuzz.py > fizzbuzz_2'
    mission_queue.append(cmd_)
    cmd_ = 'python ./fizzbuzz.py > fizzbuzz_3'
    mission_queue.append(cmd_)
    cmd_ = 'python fizzbuzz.py > fizzbuzz_4'
    mission_queue.append(cmd_)
    cmd_ = 'python ./fizzbuzz.py > fizzbuzz_5'
    mission_queue.append(cmd_)

p = []
total = len(mission_queue)
finished = 0
running = 0

while(finished + running < total):
    '''
    if len(mission_queue) <= 0 :
        break;
    '''
    localtime = time.asctime( time.localtime(time.time()) )
    gpu_av = gm.choose_no_task_gpu()
    # 在每轮epoch当中仅提交1个GPU计算任务
    if len(gpu_av) > 0 :
        gpu_index = random.sample(gpu_av, 1)[0]#为了保证服务器上所有GPU负载均衡，从所有空闲GPU当中随机选择一个执行本轮次的计算任务
        cmd_ = 'CUDA_VISIBLE_DEVICES=' + str(gpu_index) + ' ' + mission_queue.pop(0)#mission_queue当中的任务采用先进先出优先级策略
        print('Mission : %s\nRUN ON GPU : %d\nStarted @ %s\n'%(cmd_, gpu_index, localtime))
        # subprocess.call(cmd_, shell=True)
        p.append(subprocess.Popen(cmd_, shell=True))
        running += 1
        time.sleep(10)#等待NVIDIA CUDA代码库初始化并启动

    else:#如果服务器上所有GPU都已经满载则不提交GPU计算任务
        print('Keep Looking @ %s'%(localtime), end = '\r')

    new_p = []#用来存储已经提交到GPU但是还没结束计算的进程
    for i in range(len(p)):
        if p[i].poll() != None:
            running -= 1
            finished += 1
        else:
            new_p.append(p[i])

    if len(new_p) == len(p):#此时说明已提交GPU的进程队列当中没有进程被执行完
        time.sleep(1)
    p = new_p

for i in range(len(p)):#mission_queue队列当中的所有GPU计算任务均已提交，等待GPU计算完毕结束主进程
    p[i].wait()

print('Mission Complete ! Checking GPU Process Over ! ')

