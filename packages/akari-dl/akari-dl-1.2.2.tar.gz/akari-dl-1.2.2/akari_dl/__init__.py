"""
akari-dl
--------
A lightweight and open-source anime downloading CLI.

https://github.com/keisanng/akari-dl
"""

import os
import json
import argparse
import logging
from sys import version_info

if not version_info[0] >= 3 and not version_info[1] >= 10:
  print("You must use Python 3.10 or above.")
  exit()

CONFIG = {
  "debug": False,
  "default_website": "",
  "default_output": ""
}

for i in range(2):
  CONFIG_POINTER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "CONFIG_POINTER")

  try:
    with open(CONFIG_POINTER, "r", encoding="utf-8") as f:
      config_path = f.read()

      if not len(config_path):
        config_path = input("Config not found... supply desired folder path to save config file (.akari.json) or press enter to create it where akari-dl is installed:\n")

        if not len(config_path):
          config_path = os.path.dirname(os.path.realpath(__file__))

        config_path = os.path.join(config_path, ".akari.json")

        open(CONFIG_POINTER, "w", encoding="utf-8").write(config_path)

        with open(config_path, "w", encoding="utf-8") as f:
          json.dump(CONFIG, f, ensure_ascii=False, indent=2)

      with open(config_path, "r", encoding="utf-8") as f:
        conf_parser = json.load(f)
  except FileNotFoundError:
    try:
      open(CONFIG_POINTER, "x", encoding="utf-8").close()
      continue
    except FileExistsError:
      # Invalid config path supplied
      open(CONFIG_POINTER, "w", encoding="utf-8").close()
      continue

arg_parser = argparse.ArgumentParser(prog="akari_dl")

arg_parser.add_argument("website", type=str, help="Specify the name of what website to direct-download anime from (see supported websites: https://github.com/keisanng/akari-dl#supported-websites.)", nargs="?")
arg_parser.add_argument("anime", type=str, help="Specify what anime to download by title (in Romaji {https://en.wikipedia.org/wiki/Romanization_of_Japanese}.)")
arg_parser.add_argument("output", type=str, help="Specify path to output downloaded video files to.", nargs="?")
arg_parser.add_argument("-e", "--episodes", type=int, help="Specify the amount of episodes to download (downloads all if not specified) [NOT YET IMPLEMENTED.]")
arg_parser.add_argument("-s", "--specials", action="store_true", help="Enable downloading of special episodes (only works with websites that list the specials on the same page as the episodes.)")
arg_parser.add_argument("-d", "--debug", action="store_true", help="Run akari-dl in debug mode; log each connections html body and http headers and prints logging messages.")
arg_parser.add_argument("-v", "--version", action="version", version="1.2.2", help="Print the current version of akari-dl.")

logger = logging
