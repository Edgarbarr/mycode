#!/usr/bin/env python3
import requests as r
response = r.get("http://api.open-notify.org/astros.json").json()

print(f"People in space: {response['number']}")
for astro in response["people"]:
    print(f"{astro['name']} on the {astro['craft']}")

