from akari_dl import conf_parser
from akari_dl.src.log_response import log_response

def resolve_anime(self):
  """
    Verify user-specified anime exists on user-specified website via resolved url
    and return the link of the first entry of the anime's name on the website.
  """
  print(f"Searching for \"{self.anime}\"...")

  self.response = self.session.get(f"{self.url}/{self.search}{self.anime}", timeout=30)
  if conf_parser["debug"]:
    log_response(self.response)

  try:
    anchors = self.response.html.find(self.anchors[0])
    if self.name == "tokyoinsider":
      anchors += self.response.html.find("table > tr > .c_h2b > a")
  except Exception:
    print("Anime not found.")
    exit()

  for i, anchor in enumerate(anchors):
    if self.name == "tokyoinsider":
      print(f"{i+1}. {anchor.attrs['href']}")
    else:
      print(f"{i+1}. {anchor.text}")

  while True:
    try:
      desired = int(input("Select anime by index: "))
      break
    except ValueError:
      print("Please input an integer.")

  return anchors[desired-1].attrs["href"]
