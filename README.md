
# Data Structures Implementation

This Python script implements several fundamental data structures, including stacks, queues, and singly linked lists, using different underlying data structures such as arrays, singly linked lists, and doubly linked lists. Each data structure is designed to follow specific paradigms like LIFO (Last-In-First-Out) for stacks and FIFO (First-In-First-Out) for queues.

## Features

### 1. **Stack ADT (Abstract Data Type)**
   - **Array-based Stack**:
     - Implemented using a Python list.
     - Supports `push`, `pop`, `peek`, and `is_empty` operations.
   - **Singly Linked List-based Stack**:
     - Implemented using a singly linked list with sentinel nodes.
     - Supports `push`, `pop`, `peek`, and `is_empty` operations.
   - **Doubly Linked List-based Stack**:
     - Implemented using a doubly linked list with sentinel nodes.
     - Supports `push`, `pop`, `peek`, and `is_empty` operations.

### 2. **Queue ADT (Abstract Data Type)**
   - **Doubly Linked List-based Queue**:
     - Implemented using a doubly linked list with sentinel nodes.
     - Supports `queue` (enqueue), `dequeue`, `first`, and `is_empty` operations.
     - Also supports concatenation of two queues.

### 3. **Singly Linked List**
   - **Iterative Implementation**:
     - Supports `add`, `delete_first`, `delete_last`, and `is_empty` operations.
   - **Recursive Implementation**:
     - Supports `add_first`, `add_last`, `delete_first`, `delete_last`, and `is_empty` operations.
     - Uses recursive methods for adding and deleting elements.

## Usage

### Stack ADT (Array-based)

```python
stack = stack_ADT_array()
stack.push(10)
stack.push(20)
print(stack.peek())  # Output: 20
print(stack.pop())   # Output: 20
print(stack.is_empty())  # Output: False
```

### Stack ADT (Singly Linked List-based)

```python
stack = stack_ADT_singly_linked_list()
stack.push(10)
stack.push(20)
print(stack.peek())  # Output: 20
print(stack.pop())   # Output: 20
print(stack.is_empty())  # Output: False
```

### Stack ADT (Doubly Linked List-based)

```python
stack = stack_ADT_doublly_linked_list()
stack.push(10)
stack.push(20)
print(stack.peek())  # Output: 20
print(stack.pop())   # Output: 20
print(stack.is_empty())  # Output: False
```

### Queue ADT (Doubly Linked List-based)

```python
queue = queue_doublly_linked_list()
queue.queue(10)
queue.queue(20)
print(queue.first())  # Output: 10
print(queue.dequeue())  # Output: 10
print(queue.is_empty())  # Output: False
```

### Singly Linked List (Iterative)

```python
slist = singlly_recursive()
slist.add(10)
slist.add(20)
print(slist.delete_first())  # Output: 20
print(slist.delete_last())   # Output: 10
print(slist.is_empty())  # Output: True
```

### Singly Linked List (Recursive)

```python
slist = singlly_reccursive_methods()
slist.add_first(10)
slist.add_last(20)
print(slist.delete_first())  # Output: 10
print(slist.delete_last())   # Output: 20
print(slist.is_empty())  # Output: True
```

### Singly Linked List (Recursive with Tail)

```python
slist = singally_recursive()
slist.add_first(10)
slist.add_last(20)
print(slist.delete_first())  # Output: 10
print(slist.delete_last())   # Output: 20
print(slist.is_empty())  # Output: True
```

## Notes

- **Sentinel Nodes**: Some implementations use sentinel nodes to simplify boundary conditions.
- **Recursive Methods**: The recursive implementations of singly linked lists demonstrate how recursion can be used to manipulate linked lists.
- **Time Complexity**: 
  - Stack operations (`push`, `pop`, `peek`) are O(1) for all implementations.
  - Queue operations (`queue`, `dequeue`, `first`) are O(1) for the doubly linked list implementation.
  - Linked list operations (`add`, `delete`) are O(1) for adding/deleting at the head and O(n) for adding/deleting at the tail.

