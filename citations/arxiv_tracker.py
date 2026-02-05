import requests
import xml.etree.ElementTree as ET
import json

ARXIV_AUTHOR = "Saxena_T"

def fetch_arxiv():
    url = f"http://export.arxiv.org/api/query?search_query=au:{ARXIV_AUTHOR}"
    response = requests.get(url)

    root = ET.fromstring(response.text)

    papers = []
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        title = entry.find("{http://www.w3.org/2005/Atom}title").text
        papers.append(title)

    return papers

if __name__ == "__main__":
    papers = fetch_arxiv()

    with open("citations/citation_data.json", "w") as f:
        json.dump(papers, f, indent=2)
