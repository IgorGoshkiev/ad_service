from typing import Dict, List
import csv


def load_ad_platforms(file_content: str) -> Dict[str, List[str]]:
    ad_platforms = {}
    reader = csv.reader(file_content.splitlines())
    for row in reader:
        if len(row) < 2:
            continue
        platform, locations = row[0], row[1].split(',')
        for loc in locations:
            if loc not in ad_platforms:
                ad_platforms[loc] = []
            ad_platforms[loc].append(platform)
    return ad_platforms


def search_ad_platforms(ad_platforms: Dict[str, List[str]], location: str) -> List[str]:
    platforms = set()
    for loc in ad_platforms:
        if location.startswith(loc):
            platforms.update(ad_platforms[loc])
    return list(platforms)
