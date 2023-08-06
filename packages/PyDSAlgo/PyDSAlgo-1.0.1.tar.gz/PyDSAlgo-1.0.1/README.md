
# pyDSA: Your One-Stop Solution for Data Structures and Algorithms in Python

`pyDSA` is a Python library aiming to provide robust, easy-to-use implementations of a variety of data structures and algorithms. Whether you're studying for your next coding interview, teaching a computer science class, or working on a complex software project, `pyDSA` has got you covered!

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)
- [Contact](#contact)

## Features

`pyDSA` brings the power of the following data structures and algorithms to your Python projects:

- **Graph**: Connect and traverse nodes in complex networks. Implemented in `PyGraph.py` and `PyLinkedGraph.py`.
- **Heap**: Maximize or minimize data efficiently. Implemented in `PyMaxHeap.py` and `PyMinHeap.py`.
- **LinkedList**: Store and manipulate data flexibly. Implemented in `PyCircularLinkedList.py`, `PyDoublyCircularLinkedLIst.py`, `PyDoublyLinkedList.py`, `PyHeaderLinkedList.py`, `PyLinkedList.py`, and `PySkipLinkedList.py`.
- **Queue**: Manage data elements in a FIFO (First In First Out) manner. Implemented in `PyCircularQueue.py`, `PyDeque.py`, `PyPriorityQueue.py`, and `PyQueue.py`.
- **Stack**: Access your data in a LIFO (Last In First Out) fashion. Implemented in `PyStack.py` and `pyLinkedStack.py`.
- **Tree**: Model hierarchical data effectively. Implemented in `PyAVLTree.py`, `PyBTree.py`, `PyBinarySearchTree.py`, `PyBinaryTree.py`, and `PyGenericTree.py`.
- **Trie**: Execute fast retrieval operations for text. Implemented in `PyTrie.py`.

To ensure the correctness of our implementations, each data structure or algorithm has corresponding test files in the `tests` directory.

## Installation

Installing `pyDSA` is as simple as running the following command in your terminal:

```bash
pip install pyDSA
```

## Usage

Using `pyDSA` is as simple as importing the desired data structure or algorithm. Here's a basic example:

```python
from pyDSA.DS.Stack.PyStack import PyStack

# Create a new stack
stack = PyStack()

# Push elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Pop an element from the stack
element = stack.pop()
print(element)  # Output: 3
```

## Contributing

We welcome contributions of all kinds from the open-source community. Whether you'd like to fix a bug, add a feature, improve our documentation, or simply ask a question, we appreciate your help in making `pyDSA` better.

## Credits

This package was lovingly crafted by Sattyam Jain.

## License

`pyDSA` is licensed under the [MIT License](https://github.com/sattyamjjain/pyDSA/blob/main/LICENSE).

## Contact

If you have any questions or feedback, please feel free to [contact us](https://www.linkedin.com/in/sattyamjain/). We'd love to hear from you!
