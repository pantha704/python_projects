from bs4 import BeautifulSoup
import requests, lxml

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url="https://www.amazon.in/Instant-Pressure-Steamer-Sterilizer-Stainless/dp/B08PQ2KWHS/ref%22"
                            "%22=pd_lpo_sccl_3/258-7661168-7865154?pd_rd_w=Rc0wx&content-id=amzn1.sym.c3daf87c-2802"
                            "-47b7%22%22-8fa4-23dc91a4fca7&pf_rd_p=c3daf87c-2802-47b7-8fa4-23dc91a4fca7&pf_rd_r%22%22"
                            "=BFPG75S0QGD1VSJKMA9H&pd_rd_wg=djizU&pd_rd_r=f0233c9d-17ac-4b47-a90d-699e6df5bbdc%22%22"
                            "&pd_rd_i=B08PQ2KWHS&psc=1%22", headers=HEADERS)

data = response.text
print(data)
soup = BeautifulSoup(data, 'lxml')
price = soup.find(class_="a-offscreen")
price_without_currency = price.split("₹")[1]
print(price_without_currency)

