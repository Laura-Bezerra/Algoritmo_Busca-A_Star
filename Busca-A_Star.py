import math

class vetorPadrao:
    def __init__(self, X,Y,Anterior, Distancia):
        self.X = X
        self.Y = Y
        self.Anterior = Anterior
        self.Distancia = Distancia

class buscar_labirinto:
    
    def verificarDistanciaXY(self,x0,y0,x,y):
        #Calcula a distancia euclidiana entre duas coordenadas,
        #utilizando a formula de pitagoras.
        dist = math.sqrt(
                math.fabs(math.pow(x-x0,2)) + 
            math.fabs(math.pow(y-y0,2))
            )
        return round(dist,3)
    
    def verificarExistenciaVetorAberto(self,x,y):
        #Roda o vetor aberto conferindo se o x,y esta la
        for i in self.vetorAberto:
            if((i.X == x) and (i.Y == y)):
                return True
        return False
    
    def verificarExistenciaVetorFechado(self,x,y):
        #Roda o vetor fechado conferindo se o x,y esta la
        for i in self.vetorFechado:
            if((i.X == x) and (i.Y == y)):
                return True
        return False 
    
    def verNovosVizinhos(self, x, y):
        saida = []
        #O algoritmo abaixo verifica todos os 8 vizinhos 
    
        #x+1,y-1
        if ((y-1 >= 0) and (x+1 <= self.tamanhoX)):
            if(self.corpo[x+1][y-1] == 1):               
                if (self.verificarExistenciaVetorAberto(x+1, y-1) == False):
                    if(self.verificarExistenciaVetorFechado(x+1, y-1) == False):
                        saida.append([x+1,y-1])                     
        #x+1,y
        if ((x+1 <= self.tamanhoX)):
            if(self.corpo[x+1][y] == 1):
                if (self.verificarExistenciaVetorAberto(x+1, y) == False):
                    if(self.verificarExistenciaVetorFechado(x+1, y) == False):
                        saida.append([x+1,y])
        #x+1,y+1
        if ((y+1 <=self.tamanhoY) and (x+1 <= self.tamanhoX)):
            if(self.corpo[x+1][y+1] == 1):
                if (self.verificarExistenciaVetorAberto(x+1, y+1) == False):
                    if(self.verificarExistenciaVetorFechado(x+1, y+1) == False):
                        saida.append([x+1,y+1])       
        #x,y+1
        if ((y+1 <=self.tamanhoY)):
            if(self.corpo[x][y+1] == 1):
                if (self.verificarExistenciaVetorAberto(x, y+1) == False):
                    if(self.verificarExistenciaVetorFechado(x, y+1) == False):
                        saida.append([x,y+1])
        #x,y-1
        if ((y-1 >=0)):
            if(self.corpo[x][y-1] == 1):
                if (self.verificarExistenciaVetorAberto(x, y-1) == False):
                    if(self.verificarExistenciaVetorFechado(x, y-1) == False):
                        saida.append([x,y-1])       
        #x-1,y-1
        if ((y-1 >= 0) and (x-1 >= 0)):
            if(self.corpo[x-1][y-1] == 1):
                if (self.verificarExistenciaVetorAberto(x-1, y-1) == False):
                    if(self.verificarExistenciaVetorFechado(x-1, y-1) == False):
                        saida.append([x-1,y-1])
        #x-1,y
        if ((x-1 >= 0)):
            if(self.corpo[x-1][y] == 1):
                if (self.verificarExistenciaVetorAberto(x-1, y) == False):
                    if(self.verificarExistenciaVetorFechado(x-1, y) == False):
                        saida.append([x-1,y])
        #x-1,y+1
        if ((y+1 <= self.tamanhoY) and (x-1 >= 0)):
            if(self.corpo[x-1][y+1] == 1):
                if (self.verificarExistenciaVetorAberto(x-1, y+1) == False):
                    if(self.verificarExistenciaVetorFechado(x-1, y+1) == False):
                        saida.append([x-1,y+1])
                      
        return saida
    
    def avaliarVizinhosEVetorAbarto(self, vizinhos, posisaoVetorFechado):
        Controle = 999999
        semVizinho = False
        vetorControle = []
        posControle = 0
        
        #verificar se vizinhos e vetorAberto estão vazios, indicando algo sem solução
        if((len(vizinhos) == 0) and (len(self.vetorAberto) == 0)):
            print("SEM SOLUÇÃO")
            return False
        
        #Rodar todos os vizinhos enviados, adicionar no vetorControle 
        #validando a distanca.        
        c=0
        for i in vizinhos:
            tempDistancia = self.verificarDistanciaXY(i[0],i[1],self.fimx,self.fimy)
            vetorControle.append(vetorPadrao(i[0],i[1],posisaoVetorFechado,tempDistancia))
            
            if (c == 0):
               Controle = tempDistancia
            else:
                if(tempDistancia<Controle):
                    Controle = tempDistancia
                    posControle = c
            c = c + 1
        #Validando o vetorAberto, buscando o mais proximo deles
        c=0
        for i in self.vetorAberto:
            if (i.Distancia < Controle):
                semVizinho = True
                Controle = i.Distancia
                posControle = c
            c = c + 1 
        
        #redefinição dos vetores aberto e fechado
        addVetorFechado = []
        if(semVizinho == True):
            addVetorFechado.append(self.vetorAberto[posControle])
            del self.vetorAberto[posControle]
        else:
            addVetorFechado.append(vetorControle[posControle])
            del vetorControle[posControle]
            
        self.vetorFechado.append(addVetorFechado[0])
        for i in vetorControle:
            self.vetorAberto.append(i)
        
        return True