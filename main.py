import sys
import os
def error(message):
  print(message)
  exit()
try:
  link = sys.argv[1]
except:
  error("Git link not provided. Aborting...")
