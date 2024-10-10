class File:
    def __init__(self):
        self.listFile = []
    
    def enfiler(self, element):
        self.listFile.append(element)

    def defiler(self):
        if not self.est_vide():
            return self.listFile.pop(0)
        return None
    
    def est_vide(self):
        return len(self.listFile) == 0
    
    def premier(self):
        print(self.est_vide())
        if not self.est_vide():
            return self.listFile[0]
        return None
    
    def __len__(self):
        return len(self.listFile)
    
    def __str__(self):
        return str(self.listFile)
    
    

