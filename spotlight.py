#!/usr/bin/python

import os, sys, subprocess, fnmatch

from rofi import Rofi


class Spotlight:
	def __init__(self):
		self.rofi = Rofi()

	def multifuncitonal(self, argument):
		def reformat_whitespaces(self, search):
			search = search.split(" ")
			while "" in search:
				search.remove("")
			del search[0]
			return search

		try:
			argument
		except:
			search = self.rofi.text_entry("function")
		else:
			search = argument + " " + self.rofi.text_entry("function")

		selector = search[0]
		if selector == "w":
			search = reformat_whitespaces(self, search)
			search = " ".join(search)
			self.websearch(search)
		elif selector == "s":
			search = reformat_whitespaces(self, search)
			search = " ".join(search)
			print(search)
			self.search(search)
		elif selector == "e":
			self.exit()
		elif selector == "x":
			search = reformat_whitespaces(self, search)
			self.execute(search)
		else:
			self.rofi.error(
				'Not a valid command. Type "s" for search, "!" for websearch, "e" for exit or "x" for executing a command.'
			)

	def websearch(self, search):
		subprocess.Popen(["firefox", "-search", search], stdout=subprocess.PIPE)

	def search(self, search):
		def find(self, pattern, path):
			result = []
			for root, dirs, files in os.walk(path):
				for name in files:
					if fnmatch.fnmatch(name, pattern):
						result.append(os.path.join(root, name))
			return result

		output = find(self, search, os.path.expanduser("~"))
		index, key = self.rofi.select("out", output)
		self.open(output[index])

	def open(self, file):
		subprocess.Popen(["xdg-open", file], stdout=subprocess.PIPE)

	def exit(self):
		options = ["lock", "exit", "suspend", "hibernate", "reboot", "shutdown"]
		index, key = self.rofi.select("exit", options)
		command = ""
		if index == 0:
			command = "sh i3exit.sh lock"
		elif index == 1:
			command = "sh i3exit.sh logout"
		elif index == 2:
			command = "sh i3exit.sh suspend"
		elif index == 3:
			command = "sh i3exit.sh hibernate"
		elif index == 4:
			command = "sh i3exit.sh reboot"
		elif index == 5:
			command = "sh i3exit.sh poweroff"
		subprocess.Popen(command.split(" "), stdout=subprocess.PIPE)

	def execute(self, command):
		proc = subprocess.Popen(command, stdout=subprocess.PIPE)
		output, errors = proc.communicate()
		output = output.decode("utf-8").split("\n")
		self.rofi.select("out", output)

sp = Spotlight()
sp.multifuncitonal(sys.argv[1][1])
