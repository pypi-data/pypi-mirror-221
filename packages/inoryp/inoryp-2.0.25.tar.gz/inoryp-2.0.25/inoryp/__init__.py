# Autor: R0htg0r
# Versão: 2.0.16
# Atualização de: 16/09/2022 até...

import requests
import Raney

def getIP(Proxy=None, Type=None):
    if Proxy != None:
        if(Type == "http"):
            try:
                ZFsiYDmRYWgVPtg4MDTm = requests.get("https://sinkable-coils.000webhostapp.com/py.php", proxies={"http": "http://" + Proxy, "https": "https://" + Proxy}).text
            except:
                ZFsiYDmRYWgVPtg4MDTm = "0.0.0.0" 
            return ZFsiYDmRYWgVPtg4MDTm
        elif(Type == "socks5"):
            try:
                ZFsiYDmRYWgVPtg4MDTm = requests.get("https://sinkable-coils.000webhostapp.com/py.php", proxies={"http": "socks5://" + str(Proxy),"https": "socks5://" + str(Proxy)}).text
            except Exception as e:
                print(e)
                ZFsiYDmRYWgVPtg4MDTm = "0.0.0.0"
            return ZFsiYDmRYWgVPtg4MDTm
        elif(Type == "socks4"):
            try:
                ZFsiYDmRYWgVPtg4MDTm = requests.get("https://sinkable-coils.000webhostapp.com/py.php", proxies={"http": "socks4://" + Proxy, "https": "socks4://" + Proxy}).text
            except:
                ZFsiYDmRYWgVPtg4MDTm = "0.0.0.0"
            return ZFsiYDmRYWgVPtg4MDTm
        else:
            return "Você precisa informar qual método deseja utilizar: http, https, socks4 ou socks5socks4 ou socks5"
    else:
        ZFsiYDmRYWgVPtg4MDTm = requests.get("https://sinkable-coils.000webhostapp.com/py.php").text
        return ZFsiYDmRYWgVPtg4MDTm

def getCode(Proxy=None, Type=None):
    if Proxy != None:
        if(Type == "http"):
            try:
                ZFsiYDmRYWgVPtg4MDTm = requests.get("https://sinkable-coils.000webhostapp.com/py.php", proxies={"http": "http://" + Proxy, "https": "https://" + Proxy}).status_code
            except:
                ZFsiYDmRYWgVPtg4MDTm = "-1" 
            return ZFsiYDmRYWgVPtg4MDTm
        elif(Type == "socks5"):
            try:
                ZFsiYDmRYWgVPtg4MDTm = requests.get("https://sinkable-coils.000webhostapp.com/py.php", proxies={"http": "socks5://" + Proxy, "https": "socks5://" + Proxy}).status_code
            except:
                ZFsiYDmRYWgVPtg4MDTm = "-1"
            return ZFsiYDmRYWgVPtg4MDTm
        elif(Type == "socks4"):
            try:
                ZFsiYDmRYWgVPtg4MDTm = requests.get("https://sinkable-coils.000webhostapp.com/py.php", proxies={"http": "socks4://" + Proxy, "https": "socks4://" + Proxy}).status_code
            except:
                ZFsiYDmRYWgVPtg4MDTm = "-1"
            return ZFsiYDmRYWgVPtg4MDTm
        else:
            return "Você precisa informar qual método deseja utilizar: http, https, socks4 ou socks5socks4 ou socks5"
    else:
        ZFsiYDmRYWgVPtg4MDTm = requests.get("https://sinkable-coils.000webhostapp.com/py.php").status_code
        return ZFsiYDmRYWgVPtg4MDTm

def getJSON(Proxy=None, Type=None):
    if Proxy != None:
        if(Type == "http"):
            try:
                ZFsiYDmRYWgVPtg4MDTm = requests.get("https://sinkable-coils.000webhostapp.com/py.php", proxies={"http": "http://" + Proxy,"https": "https://" + Proxy})
                YaVHqQTJFnxpzVzQFNWo = {"IP": ZFsiYDmRYWgVPtg4MDTm.text,"Codigo": ZFsiYDmRYWgVPtg4MDTm.status_code, "Sessao": Raney.criar(0, "C", 20)}
            except:
                YaVHqQTJFnxpzVzQFNWo = {"IP": "0.0.0.0", "Codigo": "-1", "Sessao": Raney.criar(0, "C", 20)}
            
            return YaVHqQTJFnxpzVzQFNWo

        elif(Type == "socks5"):
            try:
                ZFsiYDmRYWgVPtg4MDTm = requests.get("https://sinkable-coils.000webhostapp.com/py.php", proxies={"http": "socks5://" + Proxy,"https": "socks5://" + Proxy})
                YaVHqQTJFnxpzVzQFNWo = {"IP": ZFsiYDmRYWgVPtg4MDTm.text,"Codigo": ZFsiYDmRYWgVPtg4MDTm.status_code,"Sessao": Raney.criar(0, "C", 20)}
            except:
                YaVHqQTJFnxpzVzQFNWo = {"IP": "0.0.0.0","Codigo": "-1","Sessao": Raney.criar(0, "C", 20)}
            
            return YaVHqQTJFnxpzVzQFNWo

        elif(Type == "socks4"):
            try:
                ZFsiYDmRYWgVPtg4MDTm = requests.get("https://sinkable-coils.000webhostapp.com/py.php", proxies={"http": "socks4://" + Proxy,"https": "socks4://" + Proxy})
                YaVHqQTJFnxpzVzQFNWo = {"IP": ZFsiYDmRYWgVPtg4MDTm.text,"Codigo": ZFsiYDmRYWgVPtg4MDTm.status_code,"Sessao": Raney.criar(0, "C", 20)}
            except:
                YaVHqQTJFnxpzVzQFNWo = {"IP": "0.0.0.0","Codigo": "-1","Sessao": Raney.criar(0, "C", 20)}
            
            return YaVHqQTJFnxpzVzQFNWo

        else:
            return "Você precisa informar qual método deseja utilizar: http, https, socks4 ou socks5socks4 ou socks5"

    else:
        ZFsiYDmRYWgVPtg4MDTm = requests.get("https://sinkable-coils.000webhostapp.com/py.php")
        YaVHqQTJFnxpzVzQFNWo = {"IP": ZFsiYDmRYWgVPtg4MDTm.text,"Codigo": ZFsiYDmRYWgVPtg4MDTm.status_code,"Sessao": Raney.criar(0, "C", 20)}
        return YaVHqQTJFnxpzVzQFNWo

def RetornarIP(Procurador=None, Metodo=None):
    if (Procurador != None):
        return getIP(Procurador, Metodo)
    else:
        return getIP()

def RetornarCodigo(Procurador=None, Metodo=None):
    if (Procurador != None):
        return getCode(Procurador, Metodo)
    else:
        return getCode()
    
def RetornarJSON(Procurador=None, Metodo=None):
    if (Procurador != None):
        return getJSON(Procurador, Metodo)
    else:
        return

# Versão clássica
def classico(Conteudo=None, Proxy=None, Type=None):
    if (Conteudo == 0):
        if (Proxy != None):
            return getIP(Proxy, Type)
        else:
            return getIP()
    
    elif (Conteudo == 1):
        if (Proxy != None):
            return getCode(Proxy, Type)
        else:
            return getCode()

    elif (Conteudo == 2):
        if (Proxy != None):
            return getJSON(Proxy, Type)
        else:
            return getJSON()