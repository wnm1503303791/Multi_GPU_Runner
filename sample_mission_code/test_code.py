'''
	> File Name: test_code.py
	> Author: tuzhuo
	> Mail: xmb028@163.com 
	> Created Time: Tue 15 Sep 2020 11:30:01 AM CST
'''

import numpy as np
import tensorflow as tf
a=tf.test.is_built_with_cuda()
b=tf.test.is_gpu_available(cuda_only=False,min_cuda_compute_capability=None)
print(a)
print(b)

