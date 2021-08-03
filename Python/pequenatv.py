class televisao:
    def __init__ (self):
        self.ligada = False
        self.canal = 5

#Make turn on or off the television!
    def power(self):
        #variavel booliana não precisa de True
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
#Make a change the channel
    def aumenta_canal(self):
        #if the chanel is on, change the channel!
        if self.ligada:
            self.canal +=1
#Make a change the previous channel
    def diminui_canal(self):
        #If the channel is off, not change the channel!
        if self.ligada:
            self.canal -=1


#estanciamos a classe televisao!
televisao = televisao()
#printar o status da televisão!
print(televisao.ligada)
#Informa o status depois de apertar o botão de on!
televisao.power()
print(televisao.ligada)
#Informa o status depois de apertar o botão de off!
televisao.power()
print(televisao.ligada)
#aumenta o canal!
print(f"televisão canal: {televisao.canal}")
televisao.aumenta_canal()
televisao.aumenta_canal()
print(f"Canal: {televisao.canal}")
#Mostra a troca para oitro canal (canal anterior!)
televisao.diminui_canal()
print(f"Canal diminuido: {televisao.canal}")
