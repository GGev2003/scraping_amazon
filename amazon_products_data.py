from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
from time import sleep

url = "https://www.amazon.com/s?k=gaming+headsets"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
wait = WebDriverWait(driver,10)

try:
    for i in range(1,21):
        pages = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".s-list-item-margin-right-adjustment")))
        pages[-1].click()
        sleep(3)
        page_content = driver.page_source
        sleep(2)
        try:
            with open(f"datas/first_page{i}.html","w",encoding="utf-8") as f:
                f.write(page_content)

        except Exception as e:
            print(f"file didnt created {e}")

        try:
            with open(f"datas/first_page{i}.html","r",encoding="utf-8") as f:
                html = f.read()
                
        except Exception as e:
            print(f"file didnt found {e}")

        soup = BeautifulSoup(html,"html.parser")

        products = soup.find_all(class_="puis-card-container")
        print(len(products))

        prod_datas = {}
        prod_datas["first_page_prod"]={}
        index = 0

        for each_product in products:
            try:
                prod_name = each_product.find(class_="a-size-medium a-spacing-none a-color-base a-text-normal").text.strip()
            except:
                prod_name = "N/A"

            try:
                prod_review = each_product.find(class_="a-size-base s-underline-text").text.strip()
            except:
                prod_review = "N/A"

            try:
                prod_price = each_product.find("span",class_="a-price-whole").text.replace(".","").strip()
            except:
                prod_price = "N/A"

            try:
                prod_delivery = each_product.find("div",class_="a-row a-size-base a-color-secondary s-align-children-center").find("span").get("aria-label").strip()
            except:
                prod_delivery = "N/A"
            
            index+=1
            prod_datas["first_page_prod"][f"product_{index}"] = {
                "name": prod_name,
                "review": prod_review,
                "price": f"{prod_price}$",
                "delivery": prod_delivery
            }


        try:
            with open(f"datas/infos{i}.json","w",encoding="utf-8") as f:
                json.dump(prod_datas,f,indent=4)
        except Exception as e:
            print(f"error occurred while saving the file {e}")

except:
    print("something went wrong in pages")
finally:
    driver.quit()



