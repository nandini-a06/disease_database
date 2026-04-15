import requests
import xml.etree.ElementTree as ET
import re


def clean_html(raw_html):
    # Remove all HTML tags
    clean = re.sub('<.*?>', '', raw_html)
    return clean


def fetch_medlineplus_data(disease):
    url = f"https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term={disease}"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return None

        root = ET.fromstring(response.content)

        for doc in root.iter('document'):
            title = doc.find("./content[@name='title']")
            summary = doc.find("./content[@name='FullSummary']")

            return {
                "title": clean_html(title.text) if title is not None else "N/A",
                "summary": clean_html(summary.text) if summary is not None else "No summary available"
            }

    except Exception as e:
        print("Error:", e)

    return None