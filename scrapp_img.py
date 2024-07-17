from time import sleep, time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import openpyxl

story = 'https://lacotedesmontres.com/list-ad-folio-1-newCote.htm'

def get_data(data, element):

    for montre in element:
        img = montre.find_element(By.CSS_SELECTOR, 'div.coteimg>img.pictoGalerie').get_attribute('src')

        watch = montre.text.split('\n')
        if len(watch) > 3:
            brand = watch[0]
            ref = watch[1]
            model = watch[2]
            # price = watch[3]

            # data.append({'brand': brand, 'model': model, 'ref': ref, 'price': price})
            data.append([brand, model, ref, img])

            print(f'Brand: {brand},ref: {ref} Model: {model}, img: {img}')
    return
def gecko_test(site=story):
    data = []
    # set the driver
    driver = webdriver.Firefox()
    # load this article
    driver.get(site)

    while True:
        sleep(1)
        # Trouver un élément sur la page en utilisant son sélecteur CSS
        element = driver.find_elements(By.CSS_SELECTOR, 'li.listeNews.cote')
        # img = driver.find_elements(By.CSS_SELECTOR, 'div.coteimg>img.pictoGalerie').get_attribute('src')

        # Extraire le contenu de l'élément
        with ThreadPoolExecutor(max_workers=100) as executor:
            executor.submit(get_data, data, element)
            # data.append(executor.submit(get_data, data, element))

        # passage a la page suivante
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, 'li#next.listeNews')
            next_button.click()
        except NoSuchElementException:
            print('Plus de page suivante')
            break

    driver.close()

    # Create un pandas dataframe
    df = pd.DataFrame(data, columns = ['Brand', 'Model', 'Ref', 'Price'])
    print(df)

    # Save to csv
    df.to_csv(f"/Users/hugo/PycharmProjects/project_watches/watches_pictures.csv", index=False)

    # Save to excel
    df.to_excel(f"/Users/hugo/PycharmProjects/project_watches/watches_pictures.xlsx", index=False)

# make runable
if __name__ == '__main__':
    # here we go
    start = time()
    gecko_test()
    end = time()

    print(f'Elapsed time: {end - start}')