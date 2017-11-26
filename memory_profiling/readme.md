# Memory Profiling

Install the memory profiling module of python from [memory_profiler repo](https://github.com/pythonprofilers/memory_profiler).

Type in some python code. \
Run from cmd `python -m memory_profiler memory_profiling.py`

See Examples and get working.

## Source

[Memory Management in Python](http://deeplearning.net/software/theano/tutorial/python-memory-management.html)

Python design goals are radically different than, say, C design goals. While the latter is designed to give you good control on what you’re doing at the expense of more complex and explicit programming, the former is designed to let you code rapidly while hiding most (if not all) of the underlying implementation details. 

While this sounds nice, in a production environment ignoring the implementation inefficiencies of a language can bite you hard, and sometimes when it’s too late. I think that having a good feel of how inefficient Python is with memory management (by design!) will play an important role in whether or not your code meets production requirements, scales well, or, on the contrary, will be a burning hell of memory.

Do have a look at [Improving Python's Memory Allocator](http://www.evanjones.ca/memoryallocator/).