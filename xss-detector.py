#!/usr/bin/python3

import requests
import sys
import re
import ast

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

try:
	sys.argv[1]
except IndexError:
	print(bcolors.WARNING + "\nUsage: python3 xss-detector.py <url_to_test> (Ex: python3 xss-detector.py http://example.fr/)\n" + bcolors.ENDC)
	exit()


cookie = input("Enter cookies like this: {'PHPSESSID':'1841ed304c0911ed9609c'} (press ENTER for nothing): ")
try:
	cookie
	cookie = ast.literal_eval(cookie)
except SyntaxError:
	cookie = {}

url = sys.argv[1]
t = []
o = []
gg = []

i = 0
j = 0

print(bcolors.OKCYAN + "Parameters found:" + bcolors.ENDC)

resp = requests.get(url, cookies=cookie, headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'})
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


print(bcolors.OKCYAN + "\nParameter test with GET:" + bcolors.ENDC)

while i < len(t):
	get = requests.get(url, params={t[int(i)]: '<h1>f11a2gfa4erg1</h1>'}, cookies=cookie, headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'})

	if '<h1>f11a2gfa4erg1</h1>' in get.text:
		if t[int(i)] is not None:
			print(bcolors.OKGREEN + "Vulnerable '" + t[int(i)] + "' parameters with method GET" + bcolors.ENDC)
			gg.append(bcolors.OKGREEN + "Vulnerable '" + t[int(i)] + "' parameters with method GET" + bcolors.ENDC)
	else:
		if t[int(i)] is not None:
			print(bcolors.FAIL + "Vulnerable '" + t[int(i)] + "' parameters with method GET" + bcolors.ENDC)
	i = i + 1


print(bcolors.OKCYAN + "\nParameter test with POST:" + bcolors.ENDC)

while j < len(t):
	post = requests.post(url, data={t[int(j)]: '<h1>f11a2gfa4erg1</h1>'}, cookies=cookie, headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'})

	if '<h1>f11a2gfa4erg1</h1>' in post.text:
		if t[int(j)] is not None:
			print(bcolors.OKGREEN + "Vulnerable '" + t[int(j)] + "' parameters with method POST" + bcolors.ENDC)
			gg.append(bcolors.OKGREEN + "Vulnerable '" + t[int(j)] + "' parameters with method POST" + bcolors.ENDC)
	else:
		if t[int(j)] is not None:
			print(bcolors.FAIL + "Vulnerable '" + t[int(j)] + "' parameters with method POST" + bcolors.ENDC)

	j = j + 1


print(bcolors.OKCYAN + "\nAutres pages trouvÃ©es:" + bcolors.ENDC)

with open("content.txt", "r") as content:
	for line in content:
		for word in line.split():
			if ".html" in word or ".7z" in word or "#" in word or ".png" in word or ".jpg" in word or ".svg" in word or ".jpeg" in word or ".ico" in word or ".css" in word or ".js" in word or ".zip" in word or ".pdf" in word or ".txt" in word or ".gif" in word or ".JPEG" in word or ".PNG" in word or ".JPG" in word:
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

	resp = requests.get(new_url, cookies=cookie, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'})

	with open("content.txt", "w") as content:
		content.write(resp.text)

	print(bcolors.OKCYAN + "\nParameters found on", new_url + bcolors.ENDC)

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

	print(bcolors.OKCYAN + "\nParameter test with GET on:", new_url + bcolors.ENDC)

	while i < len(t):
		get = requests.get(new_url, params={t[int(i)]: '<h1>f11a2gfa4erg1</h1>'}, cookies=cookie, headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'})

		if '<h1>f11a2gfa4erg1</h1>' in get.text:
			if t[int(i)] is not None:
				print(bcolors.OKGREEN + "Vulnerable '" + t[int(i)] + "' parameters with method GET" + bcolors.ENDC)
				gg.append(bcolors.OKGREEN + "Vulnerable '" + t[int(j)] + "' parameters with method POST on " + new_url + bcolors.ENDC)

		else:
			if t[int(i)] is not None:
				print(bcolors.FAIL + "Vulnerable '" + t[int(i)] + "' parameters with method GET" + bcolors.ENDC)

		i = i + 1


	print(bcolors.OKCYAN + "\nParameter test with POST on: " + new_url + bcolors.ENDC)

	while j < len(t):
		post = requests.post(new_url, data={t[int(j)]: '<h1>f11a2gfa4erg1</h1>'}, cookies=cookie, headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'})

		if '<h1>f11a2gfa4erg1</h1>' in post.text:
			if t[int(j)] is not None:
				print(bcolors.OKGREEN + "Vulnerable '" + t[int(j)] + "' parameters with method POST" + bcolors.ENDC)
				gg.append(bcolors.OKGREEN + "Vulnerable '" + t[int(j)] + "' parameters with method POST on " + new_url + bcolors.ENDC)
		else:
			if t[int(j)] is not None:
				print(bcolors.FAIL + "Vunerable '" + t[int(j)] + "' parameters with method POST" + bcolors.ENDC)

		j = j + 1
	x = x + 1

print("\n---------------------------------------------------------------------")
print(bcolors.OKCYAN + "\nSummary of faults found:" + bcolors.ENDC)
y=0
while y < len(gg):
	print(gg[y])
	y = y + 1

if y == 0:
	print(bcolors.FAIL + "\nNo XSS flaws found :(" + bcolors.ENDC)















