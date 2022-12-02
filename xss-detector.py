#!/usr/bin/python3

import requests
import sys
import re

url = sys.argv[1]
t = []
o = []
gg = []

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

print(bcolors.OKCYAN + "ParamÃ¨tres trouvÃ©s:" + bcolors.ENDC)

resp = requests.get(url)
path = resp.url

with open("content.txt", "w") as content:
	content.write(resp.text)


with open("content.txt", "r") as content:
	for line in content:
		if ("name=" in line and "input" in line) or ("name=" in line and "select" in line) or ("name=" in line and "option" in line) or ("name=" in line and "textarea" in line) or ("name=" in line and "button" in line):
			for word in line.split():
				if 'name="' in word:
					try:
						laver = re.search('name="(.*)"', word).group(1)
					except AttributeError:
						laver = re.search('name="(.*)"', word)
					t.append(laver)
					print(laver)
				if "name='" in word:
					try:
						laver = re.search("name='(.*)'", word).group(1)
					except AttributeError:
						laver = re.search("name='(.*)'", word)
					t.append(laver)
					print(laver)


print(bcolors.OKCYAN + "\nTest des paramÃ¨tres avec GET:" + bcolors.ENDC)

while i < len(t):
	get = requests.get(url, params={t[int(i)]: '<h1>f11a2gfa4erg1</h1>'})

	if '<h1>f11a2gfa4erg1</h1>' in get.text:
		if t[int(i)] is not None:
			print(bcolors.OKGREEN + "ParamÃ¨tre '" + t[int(i)] + "' vulnÃ©rable avec la mÃ©thode GET" + bcolors.ENDC)
			gg.append(bcolors.OKGREEN + "ParamÃ¨tre '" + t[int(i)] + "' vulnÃ©rable avec la mÃ©thode GET" + bcolors.ENDC)
	else:
		if t[int(i)] is not None:
			print(bcolors.FAIL + "ParamÃ¨tre '" + t[int(i)] + "' non vulnÃ©rable avec la mÃ©thode GET" + bcolors.ENDC)
	i = i + 1


print(bcolors.OKCYAN + "\nTest des paramÃ¨tres avec POST:" + bcolors.ENDC)

while j < len(t):
	post = requests.post(url, data={t[int(j)]: '<h1>f11a2gfa4erg1</h1>'})

	if '<h1>f11a2gfa4erg1</h1>' in post.text:
		if t[int(j)] is not None:
			print(bcolors.OKGREEN + "ParamÃ¨tre '" + t[int(j)] + "' vulnÃ©rable avec la mÃ©thode POST" + bcolors.ENDC)
			gg.append(bcolors.OKGREEN + "ParamÃ¨tre '" + t[int(j)] + "' vulnÃ©rable avec la mÃ©thode POST" + bcolors.ENDC)
	else:
		if t[int(j)] is not None:
			print(bcolors.FAIL + "ParamÃ¨tre '" + t[int(j)] + "' non vulnÃ©rable avec la mÃ©thode POST" + bcolors.ENDC)

	j = j + 1


print(bcolors.OKCYAN + "\nAutres pages trouvÃ©es:" + bcolors.ENDC)

with open("content.txt", "r") as content:
	for line in content:
		for word in line.split():
			if ".png" in word or ".jpg" in word or ".svg" in word or ".jpeg" in word or ".ico" in word or ".css" in word or ".js" in word or ".zip" in word or ".pdf" in word or ".txt" in word or ".gif" in word:
				pass
			else:
				if 'href="' in word:
					try:
						new_url = re.search('href="(.*)"', word).group(1)
					except AttributeError:
						new_url = re.search('href="(.*)"', word)
					o.append(new_url)
					print(bcolors.WARNING + "find: " + new_url + bcolors.ENDC)
				if "href='" in word:
					try:
						new_url = re.search("href='(.*)'", word).group(1)
					except AttributeError:
						new_url = re.search("href='(.*)'", word)
					o.append(new_url)
					print(bcolors.WARNING + "find: " + new_url + bcolors.ENDC)
				if "src='" in word:
					try:
						new_url = re.search("src='(.*)'", word).group(1)
					except AttributeError:
						new_url = re.search("src='(.*)'", word)
					o.append(new_url)
					print(bcolors.WARNING + "find: " + new_url + bcolors.ENDC)
				if 'src="' in word:
					try:
						new_url = re.search('src="(.*)"', word).group(1)
					except AttributeError:
						new_url = re.search('src="(.*)"', word)
					o.append(new_url)
					print(bcolors.WARNING + "find: " + new_url + bcolors.ENDC)
				if "action='" in word:
					try:
						new_url = re.search("action='(.*)'", word).group(1)
					except AttributeError:
						new_url = re.search("action='(.*)'", word)
					o.append(new_url)
					print(bcolors.WARNING + "find: " + new_url + bcolors.ENDC)
				if 'action="' in word:
					try:
						new_url = re.search('action="(.*)"', word).group(1)
					except AttributeError:
						new_url = re.search('action="(.*)"', word)
					o.append(new_url)
					print(bcolors.WARNING + "find: " + new_url + bcolors.ENDC)
				if "iframe='" in word:
					try:
						new_url = re.search("iframe='(.*)'", word).group(1)
					except AttributeError:
						new_url = re.search("iframe='(.*)'", word)
					o.append(new_url)
					print(bcolors.WARNING + "find: " + new_url + bcolors.ENDC)
				if 'iframe="' in word:
					try:
						new_url = re.search('iframe="(.*)"', word).group(1)
					except AttributeError:
						new_url = re.search('iframe="(.*)"', word)
					o.append(new_url)
					print(bcolors.WARNING + "find: " + new_url + bcolors.ENDC)
x=0

while x < len(o):
	print("\n---------------------------------------------------------------------")
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

	print(bcolors.OKCYAN + "\nParamÃ¨tres trouvÃ©s sur la page", o[x] + bcolors.ENDC)

	with open("content.txt", "r") as content:
		for line in content:
			if ("name=" in line and "input" in line) or ("name=" in line and "select" in line) or ("name=" in line and "option" in line) or ("name=" in line and "textarea" in line) or ("name=" in line and "button" in line):
				for word in line.split():
					if 'name="' in word:
						try:
							laver = re.search('name="(.*)"', word).group(1)
						except AttributeError:
							laver = re.search('name="(.*)"', word)
						t.append(laver)
						print(laver)
					if "name='" in word:
						try:
							laver = re.search("name='(.*)'", word).group(1)
						except AttributeError:
							laver = re.search("name='(.*)'", word)
						t.append(laver)
						print(laver)

	print(bcolors.OKCYAN + "\nTest des paramÃ¨tres avec GET sur la page:", o[x] + bcolors.ENDC)

	while i < len(t):
		get = requests.get(new_url, params={t[int(i)]: '<h1>f11a2gfa4erg1</h1>'})

		if '<h1>f11a2gfa4erg1</h1>' in get.text:
			if t[int(i)] is not None:
				print(bcolors.OKGREEN + "ParamÃ¨tre '" + t[int(i)] + "' vulnÃ©rable avec la mÃ©thode GET" + bcolors.ENDC)
				gg.append(bcolors.OKGREEN + "ParamÃ¨tre '" + t[int(j)] + "' vulnÃ©rable avec la mÃ©thode POST sur la page " + o[x] + bcolors.ENDC)

		else:
			if t[int(i)] is not None:
				print(bcolors.FAIL + "ParamÃ¨tre '" + t[int(i)] + "' non vulnÃ©rable avec la mÃ©thode GET" + bcolors.ENDC)

		i = i + 1


	print(bcolors.OKCYAN + "\nTest des paramÃ¨tres avec POST sur la page:", o[x] + bcolors.ENDC)

	while j < len(t):
		post = requests.post(new_url, data={t[int(j)]: '<h1>f11a2gfa4erg1</h1>'})

		if '<h1>f11a2gfa4erg1</h1>' in post.text:
			if t[int(j)] is not None:
				print(bcolors.OKGREEN + "ParamÃ¨tre '" + t[int(j)] + "' vulnÃ©rable avec la mÃ©thode POST" + bcolors.ENDC)
				gg.append(bcolors.OKGREEN + "ParamÃ¨tre '" + t[int(j)] + "' vulnÃ©rable avec la mÃ©thode POST sur la page " + o[x] + bcolors.ENDC)
		else:
			if t[int(j)] is not None:
				print(bcolors.FAIL + "ParamÃ¨tre '" + t[int(j)] + "' non vulnÃ©rable avec la mÃ©thode POST" + bcolors.ENDC)

		j = j + 1
	x = x + 1

print("\n---------------------------------------------------------------------")
print(bcolors.OKCYAN + "\nRESUME DES FAILLES XSS TROUVEES:" + bcolors.ENDC)
y=0
while y < len(gg):
	print(gg[y])
	y = y + 1















