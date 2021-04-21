import mercury
import json
from datetime import datetime
import time
from threading import Thread

configuracoes = {}
file = open("Configuracao.json")
configuracoes = json.load(file)
leitor = mercury.Reader(configuracoes.get('porta serial'),configuracoes.get('taxa em baud'))
leitor.set_region(configuracoes.get('regiao'))
leitor.set_read_plan([configuracoes.get('antena')],configuracoes.get('protocolo'), None, [], configuracoes.get("potencia do sinal"))
tempoMinimo = configuracoes.get('tempo minimo de volta')
listaTagsNaoFiltradas=[]
def countdown(t):    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
        leitor.stop_reading()
t = configuracoes.get('tempo minimo de volta')

def lerTAG():
    leitor.start_reading(listaTagsNaoFiltradas.append,1000,0)
    countdown(int(t))

lerTAG()
listaTagsFiltradas = []
now = datetime.now()
ultimaLeitura = now.strftime("%Y-%m-%d %H:%M:%S")

def filtrarTAG(listaTagsNaoFiltradas):
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
    return listaTagsNaoFiltradas    

informacoesTAGs = {}
listaTagsFiltradas = filtrarTAG(listaTagsNaoFiltradas)
print(listaTagsNaoFiltradas)

def armazenarTAGs():
    with open("informacoesTAGS.json","w") as informacoes: 
        for tag in listaTagsFiltradas:
            informacoesTAGs['epc'] = tag.epc.decode()
            informacoesTAGs['tempo'] = datetime.fromtimestamp(tag.timestamp).strftime('%H:%M:%S.%f')[:-3]           
            json.dump(informacoesTAGs, informacoes)
            informacoes.write("\n")

armazenarTAGs()