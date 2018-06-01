# Data Structures in Python

A collection of fundamental and advanced data structures implemented in Python, illustrating various ways of organizing and storing data.

## Linear Data Structures
Basic structures where data elements are arranged sequentially.

- [Array/List](./01_array.py) - Basic contiguous memory collection.
- [Linked List](./02_linked_list.py) - Linear collection of nodes where each points to the next.
- [Doubly Linked List](./03_doubly_linked_list.py) - Nodes point to both next and previous elements.
- [Stack](./04_stack.py) - LIFO (Last-In, First-Out) data structure.
- [Queue](./05_queue.py) - FIFO (First-In, First-Out) data structure.
- [Circular Queue](./06_circular_queue.py) - Queue where the last position is connected back to the first.
- [Priority Queue](./07_priority_queue.py) - Elements are served based on priority (often implemented with a heap).
- [Hash Table](./08_hash_table.py) - Maps keys to values using a hash function.

## Non-Linear Data Structures
Hierarchical and network-based data structures.

- [Binary Tree](./09_binary_tree.py) - Hierarchical structure where each node has at most two children.
- [Binary Search Tree](./10_binary_search_tree.py) - Binary tree where left < parent < right.
- [AVL Tree](./11_avl_tree.py) - Self-balancing binary search tree.
- [Trie](./12_trie.py) - Prefix tree used for efficient string retrieval.
- [Graph (Adj List)](./13_graph_adjacency_list.py) - Collection of nodes with edges stored as lists.
- [Graph (Adj Matrix)](./14_graph_adjacency_matrix.py) - Collection of nodes with edges stored in a 2D array.
- [Segment Tree](./16_segment_tree.py) - Tree used for storing information about intervals or segments.
- [Fenwick Tree](./17_fenwick_tree.py) - Efficiently updates elements and calculates prefix sums.

## Advanced Data Structures
Specialized data structures for specific use cases.

- [Disjoint Set](./15_disjoint_set.py) - Keeps track of elements partitioned into disjoint sets (Union-Find).
- [LRU Cache](./18_lru_cache.py) - Least Recently Used cache implementation.
- [Bloom Filter](./19_bloom_filter.py) - Space-efficient probabilistic data structure.
- [Skip List](./20_skip_list.py) - Probabilistic data structure that allows fast search within an ordered sequence.

## Python Collections
High-performance container datatypes from the `collections` module.

- [Deque](./21_deque.py) - Double-ended queue for fast appends and pops from both ends.
- [Namedtuple](./22_namedtuple.py) - Factory function for creating tuple subclasses with named fields.
- [OrderedDict](./23_ordereddict.py) - Dictionary subclass that remembers the order entries were added.
- [Defaultdict](./24_defaultdict.py) - Dictionary subclass that calls a factory function to supply missing values.
- [Counter](./25_counter.py) - Dictionary subclass for counting hashable objects.
- [ChainMap](./26_chainmap.py) - Class for creating a single view of multiple mappings.
