# Multi_GPU_Runner
Helps to run Multiple processes on Multiple GPUs, each process correspond to only one GPU. Only **Python** language is supported here.

[中文说明请跳转至本人博客](https://www.cnblogs.com/acm-icpcer/p/13679508.html)

## Usage

### 1. All GPUs are occupied, you have to wait one of them to be released. And you want all tasks running one by one.

first, prepare all the python command line in a .sh file, and provide it as the input file of the source code ./src/keep_looking_gpu.py. The python source code will automatically pick command line which contains string 'python' in the .sh file to generate mission queue.

example:

```
bash ./keep_looking_gpu.sh
```

### 2. You have some GPU tasks to run parallelly on a multi-GPU server.

same as Usage.1

However, this code running all the missions in the mission queue parallelly.

example:

```
bash ./keep_looking_gpu_missions_queue.sh
```

## Pay Attention

Only GPU-memory-usage information was used to judge if a GPU is available.

## Reference
1. [tf_gpu_manager](https://github.com/QuantumLiu/tf_gpu_manager)
2. [Basenji_source_code](https://github.com/calico/basenji/blob/master/basenji/util.py)
