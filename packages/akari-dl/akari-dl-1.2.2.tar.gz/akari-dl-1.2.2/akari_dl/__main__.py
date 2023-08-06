from . import conf_parser, arg_parser, logger
from .src.website import Website

def main():
  args = arg_parser.parse_args()

  if args.debug or conf_parser["debug"]:
    logger.basicConfig(level=logger.NOTSET)

  website = Website(anime=args.anime, episodes=args.episodes, specials=args.specials)

  if not args.website:
    if conf_parser["default_website"]:
      website.name = conf_parser["default_website"]
    else:
      print("Expected website at position 1 or default_website in user configuration.\nHELP: https://github.com/keisanng/akari-dl#usage")
      exit()
  else:
    website.name = args.website

  if not args.output:
    if conf_parser["default_output"]:
      website.output_path = conf_parser["default_output"]
    else:
      print("Expected website at position 1 or default_website in user configuration.\nHELP: https://github.com/keisanng/akari-dl#usage")
      exit()
  else:
    website.output_path = args.output

  if args.debug:
    conf_parser["debug"] = True

  match website.name.lower():
    case "tokyoinsider":
      website.domains = ("tokyoinsider.net", "tokyoinsider.org", "tokyoinsider.com")
      website.search = "anime/search/?k="
      website.anchors = ("tbody > tr > .c_h2 > a", ".episode > div > a", ".c_h2 > div > a")
    case "chauthanh":
      website.domains = "chauthanh.info"
      website.search = "search/?s="
      website.anchors = (".boxcontent > p > span > a", "tbody > tr > td > a", ".bd-blue > p > a")
    case _:
      print(f"\033[91m\"{args.website}\" not supported.\033[0m")

  # pylint: disable=no-member
  website.resolve_website()
  website.resolve_anime()
  website.download_anime()

  if args.debug:
    conf_parser["debug"] = False

  print("Downloading Complete.")

if __name__ == "__main__":
  main()
