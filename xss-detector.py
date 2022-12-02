import requests
import sys
import re

url = sys.argv[1]
t = []
o = []

i = 0
j = 0

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKCYAN + "Paramètres trouvés:" + bcolors.ENDC)

resp = requests.get(url)
path = resp.url

with open("content.txt", "w") as content:
	content.write(resp.text)


with open("content.txt", "r") as content:
	for line in content:
		for word in line.split():
			if 'name="' in word:
				laver = re.search('name="(.*)"', word).group(1)
				t.append(laver)
				print(laver)
			if "name='" in word:
				laver = re.search("name='(.*)'", word).group(1)
				t.append(laver)
				print(laver)


print(bcolors.OKCYAN + "\nTest des paramètres avec GET:" + bcolors.ENDC)

while i < len(t):
	get = requests.get(url, params={t[int(i)]: '<h1>f11a2gfa4erg1</h1>'})

	if '<h1>f11a2gfa4erg1</h1>' in get.text:
		print(bcolors.OKGREEN + "Paramètre '" + t[int(i)] + "' vulnérable avec la méthode GET" + bcolors.ENDC)
	else:
		print(bcolors.FAIL + "Paramètre '" + t[int(i)] + "' non vulnérable avec la méthode GET" + bcolors.ENDC)

	i = i + 1


print(bcolors.OKCYAN + "\nTest des paramètres avec POST:" + bcolors.ENDC)

while j < len(t):
	post = requests.post(url, data={t[int(j)]: '<h1>f11a2gfa4erg1</h1>'})

	if '<h1>f11a2gfa4erg1</h1>' in post.text:
		print(bcolors.OKGREEN + "Paramètre '" + t[int(j)] + "' vulnérable avec la méthode POST" + bcolors.ENDC)
	else:
		print(bcolors.FAIL + "Paramètre '" + t[int(j)] + "' non vulnérable avec la méthode POST" + bcolors.ENDC)

	j = j + 1


print(bcolors.OKCYAN + "\nAutres pages trouvées:" + bcolors.ENDC)

with open("content.txt", "r") as content:
	for line in content:
		for word in line.split():
			if 'href="' in word:
				new_url = re.search('href="(.*)"', word).group(1)
				o.append(new_url)
				print(new_url)
			if "href='" in word:
				new_url = re.search("href='(.*)'", word).group(1)
				o.append(new_url)
				print(new_url)
			if "src='" in word:
				new_url = re.search("src='(.*)'", word).group(1)
				o.append(new_url)
				print(new_url)
			if 'src="' in word:
				new_url = re.search('src="(.*)"', word).group(1)
				o.append(new_url)
				print(new_url)
			if "action='" in word:
				new_url = re.search("action='(.*)'", word).group(1)
				o.append(new_url)
				print(new_url)
			if 'action="' in word:
				new_url = re.search('action="(.*)"', word).group(1)
				o.append(new_url)
				print(new_url)
			if "iframe='" in word:
				new_url = re.search("iframe='(.*)'", word).group(1)
				o.append(new_url)
				print(new_url)
			if 'iframe="' in word:
				new_url = re.search('iframe="(.*)"', word).group(1)
				o.append(new_url)
				print(new_url)
			if "load('" in word:
				new_url = re.search("load('(.*)'", word).group(1)
				o.append(new_url)
				print(new_url)
			if 'load("' in word:
				new_url = re.search('load("(.*)"', word).group(1)
				o.append(new_url)
				print(new_url)


x=0

while x < len(o):
	print("---------------------------------------------------------------------")
	t = []
	i = 0
	j = 0
	
	new_url = o[x]
	if "http" in new_url:
		new_url = o[x]
	else:
		new_url = path + o[x]

	resp = requests.get(new_url)

	with open("content.txt", "w") as content:
		content.write(resp.text)

	print(bcolors.OKCYAN + "\nParamètres trouvés sur la page", o[x] + bcolors.ENDC)

	with open("content.txt", "r") as content:
		for line in content:
			for word in line.split():
				if 'name="' in word:
					laver = re.search('name="(.*)"', word).group(1)
					t.append(laver)
					print(laver)
				if "name='" in word:
					laver = re.search("name='(.*)'", word).group(1)
					t.append(laver)
					print(laver)

	print(bcolors.OKCYAN + "\nTest des paramètres avec GET sur la page:", o[x] + bcolors.ENDC)

	while i < len(t):
		get = requests.get(new_url, params={t[int(i)]: '<h1>f11a2gfa4erg1</h1>'})

		if '<h1>f11a2gfa4erg1</h1>' in get.text:
			print(bcolors.OKGREEN + "Paramètre '" + t[int(i)] + "' vulnérable avec la méthode GET" + bcolors.ENDC)
		else:
			print(bcolors.FAIL + "Paramètre '" + t[int(i)] + "' non vulnérable avec la méthode GET" + bcolors.ENDC)

		i = i + 1


	print(bcolors.OKCYAN + "\nTest des paramètres avec POST sur la page:", o[x] + bcolors.ENDC)

	while j < len(t):
		post = requests.post(new_url, data={t[int(j)]: '<h1>f11a2gfa4erg1</h1>'})

		if '<h1>f11a2gfa4erg1</h1>' in post.text:
			print(bcolors.OKGREEN + "Paramètre '" + t[int(j)] + "' vulnérable avec la méthode POST" + bcolors.ENDC)
		else:
			print(bcolors.FAIL + "Paramètre '" + t[int(j)] + "' non vulnérable avec la méthode POST" + bcolors.ENDC)

		j = j + 1
	x = x + 1


















