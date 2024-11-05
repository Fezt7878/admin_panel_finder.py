import requests
from bs4 import BeautifulSoup

def find_admin_panel(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                if href and 'admin' in href.lower():
                    return href
        return None
    except:
        return None

# Example usage
url = 'https://example.com'  # Replace with the URL of the website you want to scan
admin_panel_url = find_admin_panel(url)
if admin_panel_url:
    print(f"Admin panel found at: {admin_panel_url}")
else:
    print("Admin panel not found.")
