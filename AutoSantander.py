import os
import pyautogui
import time
import logging
import shutil
from datetime import date

pyautogui.PAUSE=2

#lista de diretórios
dir_client = r'c:\Clientes\teste\PRD\Entrada'
dir_input = r'c:\Clientes\teste\arquivo\Entrada'
dir_output = r'c:\Clientes\teste\arquivo\Saida'

#organiza datas
data_atual = date.today()
data_em_texto = data_atual.strftime('/%d-%m-%Y/')
data_dir_client = dir_client + data_em_texto

#copiar somente arquivos de produção, igorando os de homologação e o bastao
for filename in os.listdir(data_dir_client):
    arq_prod = filename.find("P")
    if arq_prod == 2:
        shutil.copy(data_dir_client + filename, dir_input)

#criação de log
log_format = '%(asctime)s: %(message)s'
logging.basicConfig(filename='log_dec_san.log', format=log_format)
logging.Logger = logging.getLogger('root')

pyautogui.doubleClick(117, 23) # executa vmware
pyautogui.press('enter')
pyautogui.write('senhateste123$') # insere senha
pyautogui.press('enter')
pyautogui.write('senhateste1234$') # insere senha
pyautogui.press('enter')
time.sleep(3)

# descobrir a quantidade de arquivos nos diretório
qtde_arqs_input = len([item for item in os.listdir(dir_input)
    if os.path.isfile(os.path.join(dir_input, item))])

pyautogui.doubleClick(228, 314) # executando a aplicação de dec
pyautogui.click(478, 370) # escolher a opção decriptografar

for dec in range(0, qtde_arqs_input):
    pyautogui.click(505, 244) # entrada
    pyautogui.doubleClick(776, 199) # escolher arquivo
    pyautogui.click(510, 288) # saida
    pyautogui.doubleClick(776, 199) # escolher arquivo
    pyautogui.doubleClick(664, 283) # mudar a palavra de entrada para saida
    pyautogui.write('\Saida') # escrever palavra
    pyautogui.click(859, 588) # botao ok
    pyautogui.click(544, 431) # clicar campo senha
    pyautogui.write('senhateste12345') # digitar senha
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.click(505, 244) # entrada
    pyautogui.click(776, 199) # escolher arquivo
    pyautogui.press('del')
    pyautogui.press('enter')
    pyautogui.click(1158, 83) # fechar diretorio

pyautogui.click(916, 208) # fechar dec
pyautogui.click(177, 41) # crtl+alt+del
pyautogui.click(728, 413) # bloquaar pc
pyautogui.click(716, 640) # trocar usuario
pyautogui.click(177, 41) # crtl+alt+del
pyautogui.click(505, 507) # seleciona usuario
pyautogui.click(1180, 16) # fechar vmware

qtde_arqs_output = len([item for item in os.listdir(dir_output)
    if os.path.isfile(os.path.join(dir_output, item))])

if qtde_arqs_output == qtde_arqs_input:
    logging.warning(f'{qtde_arqs_output} arquivos decriptados com sucesso!' )
else:
    logging.error(f'Processo incorreto pois a quantidade de entrada é {qtde_arqs_input} e o de saida é {qtde_arqs_output} e deveriam ser iguais')
