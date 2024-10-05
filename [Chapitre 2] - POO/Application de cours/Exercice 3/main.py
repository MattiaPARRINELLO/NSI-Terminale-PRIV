class Tranche():
    def __init__(self, tableau, start, end):
        self.tableau = tableau[start:end]
    
    def __getItem__(self, index):
        return self.tableau[index]
    
    def __setItem__(self, index, valeur):
        self.tableau[index] = valeur

    def __len__(self):
        return len(self.tableau)
    
    
