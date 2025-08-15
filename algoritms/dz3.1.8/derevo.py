from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left:
                self._insert(current.left, key)
            else:
                current.left = Node(key)
        else:
            if current.right:
                self._insert(current.right, key)
            else:
                current.right = Node(key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current, key):
        if not current:
            return False
        if key == current.key:
            return True
        elif key < current.key:
            return self._search(current.left, key)
        else:
            return self._search(current.right, key)

    def bfs(self):
        result = []
        if not self.root:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def preorder(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return []
        result = [node.key]
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        return result #[node.key] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return []
        result = []
        result += self.inorder(node.left)
        result.append(node.key)
        result += self.inorder(node.right)
        return result

    def postorder(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return []
        result = []
        result += self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.key)
        return result

class AVLTree(BinaryTree):
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        self._update_height(node)
        return self.rebalance(node)

    def _update_height(self, node):
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))

    def _get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right)

    def rebalance(self, node):
        balance = self.get_balance(node)

        # Left heavy
        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right heavy
        if balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self._update_height(z)
        self._update_height(y)
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        self._update_height(z)
        self._update_height(y)
        return y

    def preorder(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return []
        result = [node.key]
        if node.left:
            result += self.preorder(node.left)
        if node.right:
            result += self.preorder(node.right)
        return result

    def inorder(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return []
        result = []
        if node.left:
            result += self.inorder(node.left)
        result.append(node.key)
        if node.right:
            result += self.inorder(node.right)
        return result

    def postorder(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return []
        result = []
        if node.left:
            result += self.postorder(node.left)
        if node.right:
            result += self.postorder(node.right)
        result.append(node.key)
        return result

# Создаем AVL-дерево
avl = AVLTree()
bnr = BinaryTree

# Вставляем элементы
avl.insert(10)
avl.insert(20)
avl.insert(30)
avl.insert(40)
avl.insert(50)
avl.insert(25)

# Проверяем обходы
print("Preorder:", avl.preorder())
print("Inorder:", avl.inorder())
print("Postorder:", avl.postorder())

# Проверка поиска
print("Поиск 25:", avl.search(25))  # True
print("Поиск 60:", avl.search(60))  # False

# Проверка балансировки: высота и структура
print("Высота корня:", avl.root.height)
print("Обход BFS (по уровням):", avl.bfs())
