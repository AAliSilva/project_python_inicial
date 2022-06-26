import socket 
import smtplib
from datetime import datetime
import time
import nmap3
from ping3 import ping, verbose_ping


def __init__(self, dominios):
        self.dominios = dominios
  
def testar_com_socket(self, porta=0):
    testconnect = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
    try:
      testconnect.connect((self.dominios, porta))
      testconnect.close()
    except:
      mensagem = "Ocorreu um erro as " + str(datetime.today()) + " no IP/dominio " + self.dominios
      enviar_email("<alice.alves@aluno.faculdadeimpacta.com.br>", "<alice.alves@aluno.faculdadeimpacta.com.br>", mensagem, "Erro durante a execução")
      testconnect.close()

def verificar_portas(domain):
    scanner = nmap.PortScanner()
    try:
        ip_add = sc.gethostbyname(domain)
        for i in range(75, 80 + 1):
            res = scanner.scan(domain, str(i))
            res = res['scan'][ip_add]['tcp'][i]['state']
            generate_csv(res, domain, i, "Check_Ports")
    except:
        generate_csv("Failed", domain, "-", "Check_Ports")
def testar_com_ping(self, tempo=2, qtd=1):
    for i in range(qtd):
      results = ping(self.servidor)
      print("Gravando arquivo Ping")
      self.gravar_arquivo (datetime.now(), str(results) , "ArquivoPing.csv")
      if results == False:
         mensagem = "Ocorreu um erro as " + str(datetime.now().strftime("%d/%m/%Y %H:%M")) + " no IP/dominio " + self.servidor
         msg = EnviarMensagem(mensagem)
         msg.enviarEmail(self.tituloEmail, self.enderecoRemetente, self.enderecoDestino) 
      else:
        time.sleep(tempo)
       
def gerar_csv(ip_domain, nome_arquivo, tempo=2, qtd=1, ):
  resultado_ping = []
  for n in range(qtd):
    resultado = ping(ip_domain)
    resultado_ping.append(resultado)
    time.sleep(tempo)
  df_ping = pd.DataFrame(resultado_ping)
  df_ping.to_csv(nome_arquivo)
