import mercury
import json
from datetime import datetime
import time
from threading import *  
configuracoes = {}
file = open("Configuracao.json")
configuracoes = json.load(file)
leitor = mercury.Reader(configuracoes.get('porta serial'),configuracoes.get('taxa em baud'))
leitor.set_region(configuracoes.get('regiao'))
leitor.set_read_plan([configuracoes.get('antena')],configuracoes.get('protocolo'), None, [], configuracoes.get("potencia do sinal"))
listaTagsNaoFiltradas=[]
globalIsOver = False
listAuxiliar = []
listaTagsFiltradas = []
now = datetime.now()
ultimaLeitura = now.strftime("%Y-%m-%d %H:%M:%S")
tempoMinimo = configuracoes.get('tempo minimo de volta')
t = (configuracoes.get('tempo de classificacao')
informacoesTAGs = {}
semaforo = Semaphore(1)

class Tag:
    def __init__(self, tag, ultimaLeitura):
        self.Tag = tag
        self.ultimaLeitura = ultimaLeitura
        
def lerTAG():
    leitor.start_reading(listaTagsNaoFiltradas.append) 
    time.sleep(0.5) 
    
def armazenarTAGs():
    if len(listaTagsFiltradas) != 0:
        for lista in listaTagsFiltradas:
            with open("informacoesTAGS.json","w") as informacoes:
                informacoes.write(0))
                informacoes.write("\n") 
                for tag in lista:
                    informacoesTAGs['epc'] = tag.epc.decode()
                    informacoesTAGs['tempo'] = datetime.fromtimestamp(tag.timestamp).strftime('%H:%M:%S.%f')[:-3]           
                    json.dump(informacoesTAGs, informacoes)
                    informacoes.write("\n")                
            informacoes = open("informacoesTAGS.json", "r")
            list_of_lines = informacoes.readlines()
            list_of_lines[0] = 1
            informacoes = open("informacoesTAGS.json", "w")
            informacoes.writelines(list_of_lines)
            informacoes.close()
        listaTagsFiltradas.pop(0)
    time.sleep(0.5)    

def filtrarTAG(listaTagsNaoFiltradas):
    semaforo.acquire()
    i = 0
    j = 0  
    y = len(listaTagsNaoFiltradas)
    z = len(listaTagsNaoFiltradas)
    while i < y:
        tag1 = listaTagsNaoFiltradas[i]
        j = (i + 1)
        while j < z:
            tag2 = listaTagsNaoFiltradas[j]
            if(tag1.epc.decode()  == tag2.epc.decode()):
                listaTagsNaoFiltradas.pop(j)
                z -= 1
                j -= 1
            j += 1
        y = z
        i += 1
    y = len(listaTagsNaoFiltradas)
    i = 0
    
    def buscarTAG(k, tag1):
        while x < a:
            if tag1.epc.decode() == listAuxiliar[x].Tag.epc.decode():
                return a
                x += 1
        return -1    
    
    while i < y:
        if len(listAuxiliar) == 0:
            tag1 = listaTagsNaoFiltradas[i]
            leituraAtual = datetime.fromtimestamp(tag1.timestamp).strftime("%Y-%m-%d %H:%M:%S")
            if leituraAtual - ultimaLeitura < tempoMinimo :
                listaTagsNaoFiltradas.pop(i)
                y -= 1
                i -= 1
            else:
                TAG = Tag(tag1, leituraAtual)
                listAuxiliar.append(TAG)
            i += 1
        tag1 = listaTagsNaoFiltradas[i]
        a = len(listAuxiliar)
        x = buscarTAG(a, tag1)
        if x == -1:
            tag1 = listaTagsNaoFiltradas[i]
            leituraAtual = datetime.fromtimestamp(tag1.timestamp).strftime("%Y-%m-%d %H:%M:%S")
            if leituraAtual - ultimaLeitura < tempoMinimo :
                listaTagsNaoFiltradas.pop(i)
                y -= 1
                i -= 1
            else:
                TAG = Tag(tag1, leituraAtual)
                listAuxiliar.append(TAG)
            i += 1
        else:            
            tag2 = listAuxiliar[x]
            leituraAtual = datetime.fromtimestamp(tag1.timestamp).strftime("%Y-%m-%d %H:%M:%S")
            if leituraAtual - tag2.ultimaLeitura < tempoMinimo:
                listaTagsNaoFiltradas.pop(i)
                y -= 1
                i -= 1
            else:
                TAG = Tag(tag1, leituraAtual)
                listAuxiliar.pop(x)
                listAuxiliar.append(TAG)
            i += 1
    listaTagsFiltradas.append(listaTagsNaoFiltradas)
    time.sleep(0.5)
    semaforo.release()    

def lerEArmazenar():
    semaforo.acquire()
    lerTAG()
    armazenarTAGs()
    semaforo.release()
    
leituraEArmazenamento = Thread(target= lerEArmazenar, args=())
filtrarTag = Thread(target= filtrarTAG, args=())    
    
def qualificacao(timeout):
    timer(timeout)
    i = 1
    while not over():
        leituraEArmazenamento.start()
        filtrarTag.start()

def timer(time):
    t = Timer(time, setOver)
    t.start()

def setOver():
    global globalIsOver
    globalIsOver = True

def over():
    global globalIsOver
    return globalIsOver    

qualificacao(t)
     


            
            





