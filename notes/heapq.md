# heapq

Python built-in heap implementation.

## Functions

Suppose there is a stack `stk = [1, 2, 3, ...]`.

### heapq.heappush(stk, ele)

Put the `ele` into heap and maintain the heap property.

### heapq.heappop(stk)

Pop and return the minimum element.
Make sure the `stk` is not empty, otherwise there will be an `IndexError`.

### heapq.heapify(stk)

Make the `stk` become a heap, this operation can be done in O(n) time and will not allocate extra memory.

### heapq.nlargest(n, stk)

Return the first `n` largest elements in an array.
For first `n smallest elements, use `heapq.nsmallest(n, stk)`.

## Max Heap

The original version of this library is min heap.
To maintain a max heap, one can multiply all elements by `-1` so that the smallest element `-x` is actually the largest element `x`, and so on. 
