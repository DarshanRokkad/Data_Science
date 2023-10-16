# Web and Image Scraping
1. Web Scrapping.
    - Libraries.
        - import requests 
        - from bs4 import BeautifulSoup as bs
        - from urllib.request import urlopen
    - url_client = urlopen(url) -> we will get the http response.
    - raw_page = url_client.read() -> We will get a raw html page.
    - html_page = bs(raw_page,'html.parser') -> We will get the actual html page.
    - from this html page we can extract the data -> page.find_all(element,{'class':'class name'})
    - response = requests.get(href_link) -> to enter into inner page response we can request for page html after getting the response we can use page by converting into text.  
        
2. Image Scrapping.
    - headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"} -> Have to add to avoid the blocking from google for scrapping.
    - with open(os.path.join(save_directory, f"{query}_{image_tags.index(image_tag)}.jpg"),"wb") as f: -> have write image data in the binary form inside dictionary format so that we can store in mongodb.
    - pip install -r requirements.txt -> before deployment.  
