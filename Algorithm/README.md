Algorithm
=========

* [Sorting Algorithms](#sorting-algorithms)


## Sorting Algorithms

Sorting comparison:

| Name | Best | Average | Worst | Memory | Stable | Comment |
|------|------|---------|-------|--------|--------|---------|
| Insertion sort | &Omega;(N) | &Theta;(N<sup>2</sup>) | O(N<sup>2</sup>) | 1 | Yes | [diagram](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif) |
| Shell sort | &Omega;(N*log(N)) | Depends on gap sequence | Depends on gap sequence; best known is O(N<sup>4/3</sup>) | 1 | No | [diagram](https://upload.wikimedia.org/wikipedia/commons/d/d8/Sorting_shellsort_anim.gif) |
| Heapsort | &Omega;(N*log(N)) (N if all keys are not distinct) | &Theta;(N*log(N)) | O(N*log(N)) | 1 | No | [diagram](https://upload.wikimedia.org/wikipedia/commons/4/4d/Heapsort-example.gif) |
| Mergesort | &Omega;(N*log(N)) | &Theta;(N*log(N)) | O(N*log(N)) | n | Yes | [diagram](https://upload.wikimedia.org/wikipedia/commons/e/e6/Merge_sort_algorithm_diagram.svg) |
| Quicksort | &Omega;(N*log(N)) | &Theta;(N*log(N)) | O(N<sup>2</sup>) | log(N) | Both | [diagram](https://upload.wikimedia.org/wikipedia/commons/a/af/Quicksort-diagram.svg) |
| Bucket Sort | &Omega;(N+M) | &Theta;(N+M) | O(N<sup>2</sup>) | N+M | Yes | Use other sorting algorithms to sort buckets |
| Bubble Sort | &Omega;(N) | &Theta;(N<sup>2</sup>) | O(N<sup>2</sup>) | 1 | Yes | [diagram](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif) |
| Selection Sort | &Omega;(N<sup>2</sup>) | &Theta;(N<sup>2</sup>) | O(N<sup>2</sup>) | 1 | No | [diagram](https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif) |


