# Algorithms

A collection of essential algorithms and coding patterns implemented in Python.

### Sorting & Selection
- [Bubble Sort](./01_bubble_sort.py) - Simple comparison-based sorting.
- [Selection Sort](./02_selection_sort.py) - In-place comparison sorting.
- [Insertion Sort](./03_insertion_sort.py) - Builds the sorted array one item at a time.
- [Merge Sort](./04_merge_sort.py) - Divide and conquer sorting algorithm.
- [Quick Sort](./05_quick_sort.py) - Efficient partitioning-based sorting.
- [Heap Sort](./06_heap_sort.py) - Comparison-based sorting using a binary heap.
- [Quickselect](./29_quickselect.py) - Finds the kth smallest/largest element in an unordered list in average O(n).
- [Cyclic Sort](./30_cyclic_sort.py) - Sorts an array in O(n) when numbers are in a known range (1 to n).
- [Rotate Array](./46_rotate_array.py) - Rotates an array in O(n) time and O(1) space using reversal.
- [Dutch National Flag](./47_dutch_national_flag.py) - Three-way partitioning of an array with three distinct values.

### Tree & Graph Algorithms
- [Breadth-First Search (BFS)](./08_bfs.py) - Level-order graph traversal.
- [Depth-First Search (DFS)](./09_dfs.py) - Branch-by-branch graph traversal.
- [Dijkstra's Algorithm](./19_dijkstra.py) - Single-source shortest path.
- [Topological Sort](./20_topological_sort.py) - Linear ordering of directed acyclic graphs.
- [Floyd-Warshall Algorithm](./21_floyd_warshall.py) - All-pairs shortest path.
- [Bellman-Ford Algorithm](./22_bellman_ford.py) - Shortest path with negative weights.
- [Tree Level Order Traversal](./34_tree_level_order_traversal.py) - Traverses a tree level by level using a queue.
- [Tree Inorder Traversal](./35_tree_inorder_traversal.py) - Left-Root-Right traversal (iterative/recursive).
- [Tree Preorder Traversal](./36_tree_preorder_traversal.py) - Root-Left-Right traversal (iterative/recursive).
- [Tree Postorder Traversal](./37_tree_postorder_traversal.py) - Left-Right-Root traversal (iterative/recursive).
- [Prim's Algorithm](./40_prims_algorithm.py) - Finds the Minimum Spanning Tree of a graph starting from a node.
- [Kruskal's Algorithm](./41_kruskals_algorithm.py) - Finds the Minimum Spanning Tree using the Union-Find data structure.
- [Tarjan's SCC](./42_tarjans_scc.py) - Finds strongly connected components in a directed graph.
- [Bridges in Graph](./43_bridges_in_graph.py) - Identifies edges whose removal increases the number of connected components.
- [LCA Binary Tree](./44_lca_binary_tree.py) - Finds the lowest common ancestor of two nodes in a binary tree.
- [LCA Binary Search Tree](./45_lca_binary_search_tree.py) - Finds the lowest common ancestor in a BST using value properties.

### Dynamic Programming & Greedy
- [Greedy Algorithm](./12_greedy.py) - Locally optimal choices for global optimization.
- [Backtracking](./13_backtracking.py) - Incremental solution building with pruning.
- [Dynamic Programming](./14_dynamic_programming.py) - Solving complex problems via subproblems.
- [Kadane's Algorithm](./23_kadanes_algorithm.py) - Maximum subarray sum.

### Advanced Data Structure Patterns (Stack, Queue, Heap)
- [Two Pointers](./10_two_pointers.py) - Efficiently searching pairs in sorted data.
- [Sliding Window](./11_sliding_window.py) - Finding subarrays with specific properties.
- [Fast & Slow Pointers](./15_fast_and_slow_pointers.py) - Cycle detection and related problems.
- [Merge Intervals](./16_merge_intervals.py) - Combining overlapping ranges.
- [Monotonic Stack](./26_monotonic_stack.py) - Maintains elements in increasing/decreasing order to solve next-greater-element problems.
- [Monotonic Queue](./27_monotonic_queue.py) - Maintains elements in a sliding window to find the maximum/minimum in O(1).
- [K-way Merge](./31_k_way_merge.py) - Merges k sorted lists into a single sorted list.
- [Two Heaps](./32_two_heaps.py) - Uses a min-heap and a max-heap to find the median of a data stream.
- [Top K Elements](./33_top_k_elements.py) - Uses a heap to find the k most frequent or largest elements.

### Specialized & Named Algorithms
- [Binary Search](./07_binary_search.py) - Efficiently find elements in sorted arrays.
- [Boyer-Moore Voting](./17_boyer_moore_voting.py) - Majority element detection.
- [KMP Matching](./18_kmp_matching.py) - Efficient string pattern matching.
- [Binary Exponentiation](./24_binary_exponentiation.py) - Fast power calculation.
- [Union-Find Algorithm](./25_union_find_algorithm.py) - Disjoint set operations.
- [Prefix Sum](./28_prefix_sum.py) - Precomputes cumulative sums to answer range sum queries in O(1).
- [Bit Manipulation Basics](./38_bit_manipulation_basics.py) - Common tricks for setting, clearing, and toggling bits.
- [Counting Bits](./39_counting_bits.py) - Using Brian Kernighan's algorithm to count set bits.
- [Reservoir Sampling](./48_reservoir_sampling.py) - Randomly choosing k samples from a stream of unknown size.
- [Manacher's Algorithm](./49_manachers_algorithm.py) - Finds the longest palindromic substring in linear time.
- [Rolling Hash](./50_rolling_hash.py) - Efficiently calculates hash values for sliding windows (Rabin-Karp).
