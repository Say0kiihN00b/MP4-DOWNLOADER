import os
import pytube

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print('''\033[1;32m
Bem vindo ao MP4 Downloader

\033[1;36m[\033[1;32m1\033[1;36m] \033[1;32mBaixar video do Youtube
\033[1;36m[\033[1;32m2\033[1;36m] \033[1;32mCredito/sair
\033[1;36m[\033[1;32m3\033[1;36m] \033[1;32mSe inscrever no meu canal
''')

	r = input("\033[1;33m>\033[1;36m>\033[1;32m>\033[1;34m ")

	if r == '1':
		os.system('cls' if os.name == 'nt' else 'clear')
		url = input("\033[1;32mDigite o link do video que deseja baixar:\033[1;34m ")

		if 'https://www.youtube.com/' not in url:
			print("\n\033[1;31mApenas links de videos do Youtube\n")
			exit()

		os.system('cls' if os.name == 'nt' else 'clear')
		yt = pytube.YouTube(url)
		video =  yt.streams.first()
		video.download()

		print(f"\033[1;95mvideo \033[;1m{yt.title} \033[1;95mbaixado")
		pt = input("""
\033[;1m1 \033[1;96mSair
\033[;1m2 \033[1;96mVoltar ao menu

\033[1;33m>\033[1;36m>\033[1;32m>\033[1;34m """)
		if pt == '1':
			exit()
		if pt == '2':
			main()
		else:
			print("\n\033[1;31mOpção invalida\n")
			exit()

	if r == '2':
		os.system('cls' if os.name == 'nt' else 'clear')
		print('''\033[1;107m\033[1;30m
+-------------------------------------+
|Criador: Near Shelby                 |
|Libs usadas: OS e Pytube             |
|Editor de texto: Nano                |
+-------------------------------------+\n''')

	if r == '3':
		os.system("am start -a android.intent.action.VIEW https://www.youtube.com/channel/UCYx02EM3e2h2Nbn2OwJ9voQ")
		os.system('cls' if os.name == 'nt' else 'clear')
		print("\n\033[1;32mCanal: https://www.youtube.com/channel/UCYx02EM3e2h2Nbn2OwJ9voQ\033[0;0mm\n")

main()
