# min-max-heap
A implementation of MinMaxHeap with Python language.


### Usage

```python
from min_max_heap import MinMaxHeap

heap = MinMaxHeap()

for i in range(100):
    heap.push(i)

for i in range(50):
    assert heap.pop_min() == i
    assert heap.pop_max() == 99 - i

assert heap.is_empty()
```