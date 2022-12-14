#!/usr/bin/python3

import requests
import re
import sys
import ast
import urllib3
import random

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

def color(image):
	new_image = ""
	for char in image:
		if char == "═" or char == "║" or char == "╝" or char == "╚" or char == "╗" or char == "╔":
			new_image = new_image + bcolors.FAIL + char
		else:
			new_image = new_image + bcolors.WARNING + char
	return new_image

image = """\n\n
██╗  ██╗███████╗███████╗          ██████╗ ███████╗████████╗███████╗ ██████╗████████╗ ██████╗ ██████╗ 
╚██╗██╔╝██╔════╝██╔════╝          ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
 ╚███╔╝ ███████╗███████╗  █████╗  ██║  ██║█████╗     ██║   █████╗  ██║        ██║   ██║   ██║██████╔╝
 ██╔██╗ ╚════██║╚════██║  ╚════╝  ██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
██╔╝ ██╗███████║███████║          ██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═╝╚══════╝╚══════╝          ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝"""

print(color(image))


try:
	sys.argv[1]
except IndexError:
	print(bcolors.WARNING + "\nUsage: python3 web-enum.py <url_to_test> (Ex: python3 web-enum.py http://example.fr/ all)\n" + bcolors.ENDC)
	exit()

try:
	sys.argv[2]
	if sys.argv[2] == "all":
		all = 1
except IndexError:
	all = 0

cookie = input(bcolors.BOLD + bcolors.OKBLUE + "\nEnter cookies like this: {'PHPSESSID':'1841ed304c0911ed9609c', 'lang':'fr'} (press ENTER for nothing): " + bcolors.ENDC)
try:
	cookie
	cookie = ast.literal_eval(cookie)
except SyntaxError:
	cookie = {}

useragent = input(bcolors.BOLD + bcolors.OKBLUE + "\nEnter your custom User-Agent (press ENTER for default): " + bcolors.ENDC)
try:
	useragent
except SyntaxError:
	useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"


url = sys.argv[1]
o = []
gg = []

if str(url[-1]) == "/":
	url = url.rsplit("/", 1)[0]


try:
	test = requests.get(url, timeout=10, cookies=cookie, verify=False, headers = { "User-Agent": useragent})
except:
	print(bcolors.FAIL + "\nFailed to establish connection with ", url + bcolors.ENDC)
	exit()

def path(url, strict):
	if "http://" in url:
		url = url.replace('http://', '')
		pre = "http://"
	if "https://" in url:
		url = url.replace('https://', '')
		pre = "https://"
	if strict == 1:
		url = url.split("/", 1)[0]
		return url
	elif strict == 2:
		url = url.rsplit("/", 1)[0]
		return pre + url + "/"
	elif strict == 0:
		url = url.split("/", 1)[0]
		return pre + url + "/"


def xss(url):
	t = []
	resp = requests.get(url, cookies=cookie, headers = { 'User-Agent': useragent})

	for line in resp.text.splitlines():
		if ("name=" in line and "input" in line) or ("name=" in line and "select" in line) or ("name=" in line and "option" in line) or ("name=" in line and "textarea" in line) or ("name=" in line and "button" in line):
			for word in line.split():
				if 'name="' in word:
					try:
						laver = re.search('name="(.*)"', word).group(1)
					except AttributeError:
						laver = re.search('name="(.*)"', word)
					t.append(laver)
				if "name='" in word:
					try:
						laver = re.search("name='(.*)'", word).group(1)
					except AttributeError:
						laver = re.search("name='(.*)'", word)
					t.append(laver)
	if len(t) != 0:
		print(bcolors.OKCYAN + "\nParameters found on: " + url + bcolors.ENDC)
		for find in t:
			print(find)

	if len(t) != 0:
		print(bcolors.OKCYAN + "\nXSS attack with GET method (" + url + "):" + bcolors.ENDC)

	for param in t:
		get = requests.get(url, params={param: '<h1>f11a2gfa4erg1</h1>'}, cookies=cookie, headers = { 'User-Agent': useragent})

		if '<h1>f11a2gfa4erg1</h1>' in get.text:
			if param is not None:
				print(bcolors.OKGREEN + "Vulnerable '" + param + "' parameters with method GET" + bcolors.ENDC)
				gg.append(bcolors.OKGREEN + "Vulnerable '" + param + "' parameters with method GET on: " + url + bcolors.ENDC)
		else:
			if param is not None:
				print(bcolors.FAIL + "Vulnerable '" + param + "' parameters with method GET on: " + url + bcolors.ENDC)

	if len(t) != 0:
		print(bcolors.OKCYAN + "\nXSS attack with POST method (" + url + "):" + bcolors.ENDC)

	for param in t:
		post = requests.post(url, data={param: '<h1>f11a2gfa4erg1</h1>'}, cookies=cookie, headers = { 'User-Agent': useragent})

		if '<h1>f11a2gfa4erg1</h1>' in post.text:
			if param is not None:
				print(bcolors.OKGREEN + "Vulnerable '" + param + "' parameters with method POST" + bcolors.ENDC)
				gg.append(bcolors.OKGREEN + "Vulnerable '" + param + "' parameters with method POST on: " + url+ bcolors.ENDC)
		else:
			if param is not None:
				print(bcolors.FAIL + "Vulnerable '" + param + "' parameters with method POST on: " + url + bcolors.ENDC)


print(bcolors.OKCYAN + "\n----------------------------------------" + bcolors.ENDC)
print(bcolors.UNDERLINE + bcolors.BOLD + bcolors.FAIL + "\nURL found:" + bcolors.ENDC)


def add(balise, quote, word):
	if balise in word:
		try:
			new_url = re.search(balise + '(.*)' + quote, word).group(1)
		except AttributeError:
			new_url = re.search(balise + '(.*)' + quote, word)
		try:
			new_url = new_url.split("?", 1)[0]
			new_url = new_url.split("#",  1)[0]
		except:
			pass
		if 'http' not in new_url:
			try: 
				if new_url[0] == "." and new_url[1] == "/":
					new_url = path(url, 2) + new_url.replace('./', '')
				elif new_url[0] == "/":
					new_url = path(url, 0) + new_url
				else:
					new_url = path(url, 2) + new_url
			except:
				pass
		if new_url not in o and path(url, 1) == path(new_url, 1):
			o.append(new_url)
			print(bcolors.WARNING + "find: " + new_url.replace('//', '/') + bcolors.ENDC)
		elif path(url, 1) != path(new_url, 1):
			print(bcolors.FAIL + "Ignore: " + new_url.replace('//', '/') + " (not the same site)" + bcolors.ENDC)	
		elif new_url  in o:
			print(bcolors.FAIL + "Ignore: " + new_url.replace('//', '/') + " (alredy found)" + bcolors.ENDC)			



def discover(url, ):
	try:
		resp = requests.get(url, timeout=10, cookies=cookie, verify=False, headers = { "User-Agent": useragent})
		content = resp.text

		for line in content.split():
			for word in line.split():
				try:
					if all != 1 and ("@" in word or "mailto" in word or ".html" in word or ".7z" in word or "#" in word or ".png" in word or ".jpg" in word or ".svg" in word or ".jpeg" in word or ".ico" in word or ".css" in word or ".js" in word or ".zip" in word or ".pdf" in word or ".txt" in word or ".gif" in word or ".JPEG" in word or ".PNG" in word or ".JPG" in word):
						pass
					else:
						add('href="', '"', word)
						add("href='", "'", word)
						add("src='", "'", word)
						add('src="', '"', word)
						add("action='", "'", word)
						add('action="', '"', word)
						add("iframe='", "'", word)
						add('iframe="', '"', word)
				except TypeError:
					pass
	except requests.exceptions.ConnectTimeout:
		pass


discover(url)
xss(url)

y=0
for url in o:
	discover(url)
	xss(url)

if len(gg) != 0:
	print(bcolors.OKCYAN + "\n----------------------------------------\n" + bcolors.ENDC)
	print(bcolors.UNDERLINE + bcolors.BOLD + bcolors.FAIL + "XSS flaws founds:" + bcolors.ENDC)
	for url in gg:
		print(url.replace('//', '/'))
