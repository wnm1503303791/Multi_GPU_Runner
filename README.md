# Multi_GPU_Runner
Helps to run Multiple processes on Multiple GPUs, each process correspond to only one GPU.

[中文说明请跳转至本人博客](https://www.cnblogs.com/acm-icpcer/p/13679508.html)

## usage

### 1. All GPUs are occupied and you have to wait one of them to be released

first, edit the **cmd_** variable in the source code ./src/keep_looking_gpu.py  to change its content to your own GPU python command line.

then

```
python ./src/keep_looking_gpu.py
```

### 2. some of the GPUs on the server are free and you have some GPU task to run parallelly on them

first, edit the **mission_queue** variable in the source code ./src/keep_looking_gpu_missions_queue.py  to change its content to all of your GPU python command lines.

then

```
python ./src/keep_looking_gpu_missions_queue.py
```

## Pay Attention

Only GPU-memory-usage information was used to judge if a GPU is available.

## Reference
1. [tf_gpu_manager](https://github.com/QuantumLiu/tf_gpu_manager)
2. [Basenji_source_code](https://github.com/calico/basenji/blob/master/basenji/util.py)
