#!/usr/bin/env python3
import os
import re
import json
import urllib.request

USERNAME = "Pratyaksh0x1"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

def get_contributions():
    if not TOKEN:
        print("No GITHUB_TOKEN found, skipping GraphQL API fetch.")
        return None
    
    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
          }
        }
      }
    }
    """
    data = json.dumps({"query": query, "variables": {"login": USERNAME}}).encode('utf-8')
    req = urllib.request.Request("https://api.github.com/graphql", data=data, headers={
        "Authorization": f"Bearer {TOKEN}",
        "User-Agent": "Contribution-Sync"
    })
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            return res["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]
    except Exception as e:
        print("Error fetching GraphQL contributions:", e)
        return None

def update_svg_files(total):
    if not total:
        return
    
    pattern = re.compile(r'(\d+)\s+CONTRIBUTIONS\s+\((\d+)\s+COMMITS\)')
    status_pattern = re.compile(r'(\d+)\s*/\s*YEAR\s*✓')

    for fname in ["assets/animated-contributions-dark.svg", "assets/animated-contributions-light.svg"]:
        if not os.path.exists(fname):
            continue
        with open(fname, "r", encoding="utf-8") as f:
            content = f.read()

        # Update total contributions in header
        new_content = pattern.sub(f"{total} CONTRIBUTIONS (\\2 COMMITS)", content)
        # Update total in bottom status bar
        new_content = status_pattern.sub(f"{total} / YEAR ✓", new_content)

        if new_content != content:
            with open(fname, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {fname} with {total} contributions.")
        else:
            print(f"{fname} already up to date ({total} contributions).")

if __name__ == "__main__":
    count = get_contributions()
    if count:
        print(f"Live total contributions for {USERNAME}: {count}")
        update_svg_files(count)
    else:
        print("Could not retrieve live count, keeping existing data.")
