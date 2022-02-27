####### METHOD 1 ##############

class Node:
    def __init__(self, value):
        self.children = []
        self.value = value

    def add_child(self, value):
        self.children.append(Node(value))

    def __repr__(self):
        return f'{self.value}'


class CategoryTree:
    def __init__(self):
        self.roots = {} 

    def add_category(self, category, parent=None):
        if not parent:
            root = category
            self.roots[root] = Node(root)
        else:
            root = self.roots.get(parent, None)
            if not root:
                raise KeyError(f'No parent named {parent} exists')
            root.add_child(category)

    def get_children(self, parent):
        parent_obj = self.roots.get(parent, None)
        if not parent_obj:
            raise KeyError(f'No parent named {parent} exists')
        return parent_obj.children
    
c = CategoryTree()
c.add_category('A', None)
c.add_category('B', 'A')
c.add_category('C', 'A')
c.add_category('E', 'A')
c.add_category('D', None)
c.add_category('F', 'D')
c.add_category('Q', 'D')
print(c.get_children('A'))



###### METHOD 2

class CategoryTree:
    def __init__(self):
        self.parents = dict()

    def add_category(self, category, parent=None):
        if not parent:
            self.parents[category] = []
        elif parent not in self.parents:
            raise KeyError(f'No parent named {parent} exists')
        else:
            self.parents[parent] = self.parents[parent] + [category]

    def get_children(self, parent):
        if parent not in self.parents:
            raise KeyError(f'No parent named {parent} exists')
        return self.parents[parent]

c = CategoryTree()
c.add_category('A', None)
c.add_category('B', 'A')
c.add_category('C', 'A')
c.add_category('D', None)
c.add_category('F', 'D')
c.add_category('Q', 'D')
print(','.join(c.get_children('A') or []))
