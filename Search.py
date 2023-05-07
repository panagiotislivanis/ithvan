import urllib.parse
import webbrowser


def search_query(query):
    base_url = "https://www.google.com/search?q="
    url = base_url + urllib.parse.quote(query)
    webbrowser.open(url)
