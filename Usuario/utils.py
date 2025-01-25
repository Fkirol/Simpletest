import requests
from bs4 import BeautifulSoup
import re

def scrape_pinterest_board(board_url):
   
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
             'Accept-Language': 'en-US,en;q=0.9',
         }
        images = []

        response = requests.get(board_url, headers=headers)
        response.raise_for_status()  
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            links = soup.find_all('div')
            for link in links:
                asd = link.find('div')         
                if asd:
                   dsa = asd.find('img')
                   if dsa:
                       image = dsa.get('src')
                       images.append({
                          'image': image 
                       })
        seen_urls = set()
        unique_data = []

        for item in images:
            if 'image' in item and item['image'] not in seen_urls:
                seen_urls.add(item['image'])
                unique_data.append(item)               
                       
        
        return unique_data
    

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión o HTTP: {e}")
        return None
    except Exception as e:
        print(f"Error al parsear la página: {e}")
        return None