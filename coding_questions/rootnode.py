class Treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
        
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
        
        
    def print_data(self):
        spaces= " "*self.get_level() *2
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + self.data)
        if len(self.children):
            for child in self.children:
                child.print_data()
                

def build_electronics():
    root= Treenode("electronics")

    laptop=Treenode("laptop")
    laptop.add_child(Treenode("Mac"))
    laptop.add_child(Treenode("acer"))

    cell_phone=Treenode("cellphone")
    cell_phone.add_child(Treenode("iphone"))
    cell_phone.add_child(Treenode("samsung"))
    
    root.add_child(laptop)
    root.add_child(cell_phone)
    
    print(cell_phone.get_level())
    return root 

if __name__=='__main__':
    root=build_electronics()
    root.print_data()
    print(root.get_level())
    pass