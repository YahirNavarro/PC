#!/usr/bin/env python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse
import subprocess
import os
import logging
import socket
import sys
import traceback
try:
    from googlesearch import search
except ImportError:
    os.system('pip install -r requirements.txt')
    print('\nInstalando  "requirements.txt"...')
    print('Ejecuta el script de nuevo.')
    exit()

# Funciones de modulos locales
from metadata_img import printMeta
from nmap_Scripting import nmapRun
from env_correo import Correo
from script_Hash import HashTool


def main(firewallOpc):
    # Condicion que valida si el usuario quiso usar la herramienta FirewallRed
    if(firewallOpc!="Nada"):
        # Llamado a la funcion interna de Firewall
        FirewallRed(firewallOpc)
def mail():
    # Creacion de un objeto de mensaje SMTP
    msg = MIMEMultipart()
    mensaje = input('Ingresa el mesaje: ')

# Parametros del mensaje
    password = input('Ingresa tu contraseña: ')
    msg['From'] = input('Ingresa tu correo electronico: ')
    msg['To'] = input('Ingresa el correo electronico del destinatario: ')
    msg['Subject'] = input('Descripción: ')

    msg.attach(MIMEText(mensaje, 'plain'))

# Crear el Servidor
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()

# Ingresamos las credencial para envio del mensaje
    servidor.login(msg['From'], password)

# Enviamos el mensaje con el servidor
    servidor.sendmail(msg['From'], msg['To'], msg.as_string())
    servidor.quit()

    print('Mensaje Enviado correctamente a el correo', msg['To'])

def FirewallRed(opc):
    print("\n\n--- Corriendo el programa FirewallRed... ---")
    # Validamos que sea una opcion correcta
    if(opc == "Status" or opc == "Public" or opc == "Private"):
        # Llamado a la aplicacion Powershell externa de FirewallRed 
        psExe = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                                  '-ExecutionPolicy',
                                  'Unrestricted',
                                  './scriptPS/Scrip_PwShelll.ps1', #Checar esto
                                  opc], cwd=os.getcwd())
        psExe.wait()
        print("\n")
    else:
        print("ERROR. Corra de nuevo este script con una opcion firewall correcta.")


def SocketInfo(hostname):
    print("=== Inicio de la aplicacion SocketInfo... ===\n")
    try:
        info = socket.gethostbyname_ex(hostname)
        print("Info del dominio: " + str(info))
        print("\nResultados de buscar este dominio en Google: ")
        query = info[0]
        for enlace in search(query, tld="com", num=10, stop=10, pause=2):
            print(enlace)
        print("\n=== Fin de la busqueda ===")
    except:
        traceback.print_exc(file=sys.stdout)
        print("\nLINK INVALIDO. No se pudo analizar ningun host.")

if len(sys.argv) == 0:
    print("\n Escribe un argumento u opcion a elegir.")


if __name__ == '__main__':

    
    
    parser = argparse.ArgumentParser(description='Herramientas de ciberseguridad')
    
    parser.add_argument('--hash', '-H', 
                        help='Ruta completa del archivo que deseamos "hashear".')
    
    parser.add_argument('--metadata', '-M', type=str, 
                        help='Ver metadatos de las imagenes \
                            de la carpeta indicada.')
    
    parser.add_argument('--nmap', '-N', 
                        help='Escanear puertos IP (no olvides \
                        ingresar el argumento --gatewayip).', 
                        action='store_true')
    
    parser.add_argument('--gatewayip', '-GWI', type=str, 
                        help='Ingresar su puerta de enlace(Gateway Ip).')
    
    parser.add_argument('--firewall', '-F', type=str, 
                        help='La opcion que desea \
                        realizar con el tipo de red (checar documentacion).', 
                        default='Nada')
    
    parser.add_argument('--hostname', '-H2', type=str, 
                        help='Link del host que quiere analizar.')
    parser.add_argument('--mail', '-Z', type=str, 
                        help='MAIL.')
    args = parser.parse_args()
    
    # Chequeo de argumentos para hash
    if args.hash:
        logging.info("Hash_Script")
        HashTool(args.hash)
    
    # Chequeo de argumentos para metadata
    if args.metadata:
        logging.info("Metadata_Script")
        printMeta(args.metadata)
    
    # Chequeo de argumentos para nmap
    if args.nmap:
        if args.gatewayip:
            logging.info("nmap_Scripting")
            nmapRun(args.gatewayip)
        else:
            logging.warning("Falta el argumento --gatewayip")
            parser.error("--nmap requires --gatewayip.")
    
    # Chequeo de argumentos para SocketInfo
    if args.hostname:
        logging.info("SocketInfo")
        SocketInfo(args.hostname)
    if args.mail:
        mail()

    main(args.firewall)
