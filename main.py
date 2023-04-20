import bs4
import requests
import smtplib

url = "https://www.amazon.sa/-/en/HP-Laptop-15s-eq3002nx-RyzenTM-Windows/dp/B0BGXGL91F/ref=sr_1_1?keywords=15s-eq3002nx&qid=1681768792&s=electronics&sr=1-1&th=1"
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3' }

old_price = 1299

soup = bs4.BeautifulSoup(requests.get(url, headers = headers).text, "lxml")
soup = soup.find("span", class_ = "a-price-whole").getText().split(",")
new_price = float(soup[0] + soup [1].split(".")[0])

if new_price != old_price:
    a = smtplib.SMTP("smtp.gmail.com", 587)
    a.starttls()
    a.login("obadahpy@gmail.com", "sohgdzfdmxagagkv")
    a.sendmail("obadahpy@gmail.com", "obadah2109@gmail.com", f"Subject:Amazon\n\nnew price = {new_price} SAR")
