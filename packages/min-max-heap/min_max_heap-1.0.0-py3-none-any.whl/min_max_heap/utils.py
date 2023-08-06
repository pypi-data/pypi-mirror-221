

def heaplify(heap):
    size = len(heap)
    for i in range((size - 3)>>1, -1, -1):
        siftdown(heap, i)

def siftdown(heap, k):
    if (k & 1) == 0:
        siftdown_min(heap, k)
    else:
        siftdown_max(heap, k)

def sift_up(heap, k):
    if (k & 1) == 0:
        sibling = k - 1 if (k & 3) == 0 else k >> 1
        if sibling > 0 and heap[sibling] < heap[k]:
            heap[sibling], heap[k] = heap[k], heap[sibling]
            siftup_max(heap, sibling)
        else:
            siftup_min(heap, k)
    else:
        if heap[k-1] > heap[k]:
            heap[k-1], heap[k] = heap[k], heap[k-1]
            siftup_min(heap, k-1)
        else:
            siftup_max(heap, k)


def peek_min(heap):
    return heap[0]

def peek_max(heap):
    return heap[1] if len(heap) > 1 else heap[0]

def pop_min(heap):
    val = heap[0]
    last = heap.pop()
    if len(heap) > 0:
        heap[0] = last
        siftdown(heap, 0)
    return val

def pop_max(heap):
    size = len(heap)
    if size < 2:
        return pop_min(heap)
    val = heap[1]
    last = heap.pop()
    if size > 2:
        heap[1] = last
        siftdown(heap, 1)
    return val


def push(heap, value):
    index = len(heap)
    heap.append(value)
    sift_up(heap, index)


def replace_min(heap, value):
    val = heap[0]
    heap[0] = value
    siftdown(heap, 0)
    return val

def replace_max(heap, value):
    size = len(heap)
    if size < 2:
        return replace_min(heap, value)
    val = heap[1]
    heap[1] = value
    siftdown(heap, 1)
    return val

def siftdown_min(heap, k):
    size = len(heap)
    if k + 1 < size and heap[k] > heap[k+1]:
        heap[k], heap[k+1] = heap[k+1], heap[k]

    candidate, end = (k + 1) << 1, min(size, (k + 3) << 1)
    if candidate >= size:
        return

    for i in range(candidate+1, end):
        if heap[i] < heap[candidate]:
            candidate = i

    if heap[candidate] < heap[k]:
        heap[k], heap[candidate] = heap[candidate], heap[k]
        siftdown(heap, candidate)


def siftdown_max(heap, k):
    size = len(heap)
    if heap[k-1] > heap[k]:
        heap[k-1], heap[k] = heap[k], heap[k-1]

    candidate, end = k << 1, min(size, (k + 2) << 1)
    if candidate >= size:
        return
    
    for i in range(candidate+1, end):
        if heap[i] > heap[candidate]:
            candidate = i

    if heap[candidate] > heap[k]:
        heap[k], heap[candidate] = heap[candidate], heap[k]
        siftdown(heap, candidate)

def siftup_min(heap, k):
    val = heap[k]
    while k > 0:
        parent = (k >> 1) - 2 if (k & 3) == 0 else (k >> 1) - 1
        if heap[parent] <= val:
            break
        heap[k] = heap[parent]
        k = parent
    heap[k] = val


def siftup_max(heap, k):
    val = heap[k]
    while k > 1:
        parent = k >> 1 if (k & 3) == 3 else (k >> 1) - 1
        if heap[parent] >= val:
            break
        heap[k] = heap[parent]
        k = parent
    heap[k] = val
