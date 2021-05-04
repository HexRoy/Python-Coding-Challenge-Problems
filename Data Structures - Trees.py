# Simple Tree Implementation
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, print_type):
        data = self.data.split(" ", 1)
        if print_type == "name":
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + data[0])
            if self.children:
                for child in self.children:
                    child.print_tree(print_type)

        elif print_type == "designation":
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + data[1])
            if self.children:
                for child in self.children:
                    child.print_tree(print_type)
        elif print_type == "both":
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if self.children:
                for child in self.children:
                    child.print_tree(print_type)
        else:
            print("Invalid print type")
            return


    def print_tree_location(self, depth):
        if depth < 0:
            print("illegal depth")
        level = self.get_level()
        if level <= depth:
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if self.children:
                for child in self.children:
                    child.print_tree_location(depth)



    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()




# Data structures exercise: General Tree
# Below is the management hierarchy of a company.
#
# ss
#
# Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class.
# Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree.
# As shown below,
#
#
#
# Here is how your main function should will look like,
#
# if __name__ == '__main__':
#     root_node = build_management_tree()
#     root_node.print_tree("name") # prints only name hierarchy
#     root_node.print_tree("designation") # prints only designation hierarchy
#     root_node.print_tree("both") # prints both (name and designation) hierarchy
# Solution
#
# Build below location tree using TreeNode class
#
#
#
# Now modify print_tree method to take tree level as input.
# And that should print tree only upto that level as shown below,

def build_management_tree(type):
    root = TreeNode("Nilupul (CEO)")

    cto = TreeNode("Chinmay (CTO)")
    cto.add_child(TreeNode("AAmir (Application Head)"))
    root.add_child(cto)

    infrastructure_head = TreeNode("Vishwa (Infrastructure Head)")
    infrastructure_head.add_child(TreeNode("Dhaval (Cloud Manager)"))
    infrastructure_head.add_child(TreeNode("Abhijit (App Manager)"))
    cto.add_child(infrastructure_head)

    hr_head = TreeNode("Gels (HR Head)")
    hr_head.add_child(TreeNode("Peter (Recruitment Manager)"))
    hr_head.add_child(TreeNode("Waqas (Policy Manager)"))
    root.add_child(hr_head)

    root.print_tree(type)


def print_managemnt_tree():
    print("Designation")
    tree = build_management_tree("designation")
    print("\nName")
    tree = build_management_tree("name")
    print('\nBoth')
    tree = build_management_tree("both")
    print("\nIllegal input")
    tree = build_management_tree("bad")


def build_location_tree(level):
    root = TreeNode("Global")

    india = TreeNode("India")
    root.add_child(india)

    gajarat = TreeNode("Gajarat")
    gajarat.add_child(TreeNode("Ahmedabad"))
    gajarat.add_child(TreeNode("Baroda"))
    india.add_child(gajarat)

    karnataka = TreeNode('Karnataka')
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))
    india.add_child(karnataka)

    usa = TreeNode("USA")
    root.add_child(usa)

    new_jersey = TreeNode("New Jersey")
    new_jersey.add_child(TreeNode("Princeton"))
    new_jersey.add_child(TreeNode("Trenton"))
    usa.add_child(new_jersey)

    california = TreeNode('California')
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))
    usa.add_child(california)

    root.print_tree_location(level)


def print_managemnt_tree():
    build_location_tree(0)
    build_location_tree(1)
    build_location_tree(2)
    build_location_tree(3)

if __name__ == '__main__':
    #print_managemnt_tree()
    print_managemnt_tree()
