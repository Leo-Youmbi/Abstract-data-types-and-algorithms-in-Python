class BSTMap:
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    # Determines if the map contains the given key.
    def __contains__(self, key):
        return self._bstSearch(self._root, key) is not None

    # Returns the value associated with the key.
    def valueOf(self, key):
        node = self._bstSearch(self._root, key)
        assert node is not None, "Invalid map key."
        return node.value

    # Helper method that recursively searches the tree for a target key.
    def _bstSearch(self, subtree, target):
        if subtree is None:  # base case
            return None
        elif target < subtree.key:  # target is left of the subtree root.
            return self._bstSearch(subtree.left, target)
        elif target > subtree.key:  # target is right of the subtree root.
            return self._bstSearch(subtree.right, target)
        else:  # base case
            return subtree

    # Adds a new entry to the map or replaces the value of an existing key.
    def add(self, key, value):
        # Find the node containing the key, if it exists.
        node = self._bstSearch(self._root, key)
        # If the key is already in the tree, update its value
        if node is not None:
            node.value = value
            return False
        # Otherwise, add a new entry.
        else:
            self._root = self._bstInsert(self._root, key, value)
            self._size += 1
            return True

    # Helper method that inserts a new item, recursively.
    def _bstInsert(self, subtree, key, value):
        if subtree is None:
            subtree = _BSTMapNode(key, value)
        elif key < subtree.key:
            subtree.left = self._bstInsert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bstInsert(subtree.right, key, value)
        return subtree

    # Removes the map entry associated with the given key.
    def remove(self, key):
        assert self.__contains__(key), "Invalid map key."
        self._root = self._bstRemove(self._root, key)
        self._size -= 1

    # Helper method that removes an existing item recursively.
    def _bstRemove(self, subtree, target):
        # Search for the item in the tree
        if subtree is None:
            return subtree
        elif target < subtree.key:
            subtree.left = self._bstRemove(subtree.left, target)
            return subtree
        elif target > subtree.key:
            subtree.right = self._bstRemove(subtree.right, target)
            return subtree
        # We found the node containing the item.
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree is None:
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor = self._bstMinimum(subtree.right)
                subtree.key = successor.key
                subtree.value = successor.value
                subtree.right = self._bstRemove(subtree.right, successor.key)
                return subtree

    def _bstMinimum(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bstMinimum(subtree.left)


class _BSTMapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
