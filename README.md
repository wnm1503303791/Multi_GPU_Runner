# Multi_GPU_Runner
Helps to run Multiple processes on Multiple GPUs, each process correspond to only one GPU.

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
