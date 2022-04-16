import urllib.request
import sys
import os
from lib.scanner import *

def error(message):
  print(f"{message} Aborting...")
  exit()
try:
  link = sys.argv[1]
except:
  error("GitHub link not provided.")

parts = link.split("/")
username, repo = urlscan(parts)
validation = urllib.request.urlopen(f"https://github.com/repos/{username}/{repo}")
if validation.getcode() !== 200:
  error("Invalid GitHub URL.")
print(validation.read())
