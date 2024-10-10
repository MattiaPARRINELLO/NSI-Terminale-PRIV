from file import File
from client import Client
class Caisse:
    def __init__(self, fileClient):
        self.fileClient = fileClient
        self.nbArticles = 0
    
    def nouveau_client(self, nbArticles):
            print('Nouveau client avec '+str(nbArticles)+' articles')
            self.fileClient.enfiler(Client(nbArticles))

    def pas(self):
        if self.nbArticles > 0:
            self.nbArticles -= 1
        else:
            self.fileClient.defiler()
            self.nbArticles = self.fileClient.premier().nombre_articles
            

        


