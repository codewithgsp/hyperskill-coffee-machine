class River:
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        River.all_rivers.append(self)

    def get_info(self):
        print('The length of  {river} is {length}'.format(river=self.name,
                                                          length=self.length))


volga = River('volga', 3530)
seine = River('Seine', 776)
nile = River('Nile', 6852)

for river in River.all_rivers:
    print(river.name, river.length)

volga.get_info()
River.get_info(volga)
