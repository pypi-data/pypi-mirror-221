"""
  Download an anime based on user-configuration given desired anime is found on desired website.
"""

import os
import requests.exceptions

from akari_dl import conf_parser
from akari_dl.src.log_response import log_response

def download_episodes(self, folder_path=os.PathLike, episodes=list):
  """
    Download all (unless specified otherwise) episodes of an anime
    into a folder of the anime's name inside the user-provided output path.
  """
  ep_count = 0

  for episode in episodes:
    ep_count += 1

    self.endpoint = episode.attrs["href"]

    if self.name == "chauthanh":
      self.response = self.session.get(f"{self.url}/anime/{self.endpoint[3:]}", timeout=30)
    else:
      if self.endpoint.startswith("https"):
        self.response = self.session.get(self.endpoint, timeout=30)
      else:
        self.response = self.session.get(f"{self.url}{self.endpoint}", timeout=30)

    anchors = self.response.html.find(self.anchors[2])

    connected = False

    try:
      for anchor in anchors:
        try:
          while not connected:
            self.endpoint = anchor.attrs["href"]

            if self.name == "chauthanh":
              self.endpoint = f"{self.url}/anime/download/{self.endpoint[3:]}"

            print(f"Querying {self.endpoint}")

            file_format = self.endpoint[-3:]

            self.response = self.session.get(self.endpoint, timeout=30)

            if self.response.status_code == 200:
              connected = True
        except requests.exceptions.MissingSchema:
          print("Video file not found.")
    except Exception:
      print("Unable to find video file; skipping episode.")
      continue

    try:
      print(f"Downloading episode {ep_count} from {self.endpoint}")
      file_path = os.path.join(folder_path, f"Episode {ep_count}.{file_format}")
      with open(file_path, "wb") as video_file:
        for chunk in self.response.iter_content(1024):
          video_file.write(chunk)
      print(f"Episode {ep_count} downloaded to {file_path}")
    except Exception as error:
      print(f"Failed to download episode: {error}.")


def download_anime(self):
  """
    Download user specified anime by scraping links until reaching a video file source.
  """
  if self.endpoint.startswith("https"):
    self.response = self.session.get(self.endpoint)
  else:
    self.response = self.session.get(f"{self.url}{self.endpoint}")
  episodes = self.response.html.find(self.anchors[1]) # Episodes anchors

  if conf_parser["debug"]:
    log_response(self.response)

  episodes_regular, episodes_special = [], []

  if self.name != "enime":
    episodes.reverse()

  if self.name == "tokyoinsider":
    for episode in episodes:
      match episode.find("em", first=True).text:
        case "episode":
          episodes_regular.append(episode)
        case _:
          episodes_special.append(episode)
  else:
    episodes_regular = episodes

  anime_slug = self.anime
  for char in "/><\"\:|?*":
    anime_slug = anime_slug.replace(char, "")

  folder_path = os.path.join(self.output_path, anime_slug)

  if not os.path.exists(folder_path):
    os.makedirs(folder_path)

  download_episodes(self, folder_path, episodes_regular)

  if self.specials_enabled:
    folder_path = os.path.join(self.output_path, anime_slug, "Specials")

    if conf_parser["debug"]:
      download_episodes(self, folder_path, episodes_special)
    else:
      try:
        download_episodes(self, folder_path, episodes_special)
      except Exception as error:
        print(f"Download failed: {error}")
        exit()

  return f"Finished downloading {self.anime}."
