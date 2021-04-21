import mercury
import json
from datetime import datetime
import time

configuracoes = {}
file = open("Configuracao.json")
configuracoes = json.load(file)
leitor = mercury.Reader(configuracoes.get('porta serial'),configuracoes.get('taxa em baud'))
leitor.set_region(configuracoes.get('regiao'))
leitor.set_read_plan([configuracoes.get('antena')],configuracoes.get('protocolo'), None, [], configuracoes.get("potencia do sinal"))
listaTagsNaoFiltradas=[]
def countdown(t):    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
        leitor.stop_reading()
t = 10
def classificacao():
    leitor.start_reading(listaTagsNaoFiltradas.append,1000,0)
    countdown(int(t))
classificacao()
informacoesTAGs = {}
def armazenarTAGs():
    with open("informacoesTAGS.json","w") as informacoes: 
        for tag in listaTagsNaoFiltradas:
            informacoesTAGs['epc'] = tag.epc.decode()
            informacoesTAGs['tempo'] = datetime.fromtimestamp(tag.timestamp).strftime('%H:%M:%S.%f')[:-3]           
            json.dump(informacoesTAGs, informacoes)
            informacoes.write("\n")
armazenarTAGs()