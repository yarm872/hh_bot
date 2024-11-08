import selenium as sel
import PRE_SETTINGS as settings
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

#https://reutov.hh.ru/?hhtmFrom=account_login
base_url = "https://reutov.hh.ru/"

def setup_func(driver):
    for key, item in settings.settings.items():
        #time.sleep(1)
        print(key, item)
        if item[-1] is False or item[-1] is -1 or item[-1] is "":
            print("pass", item[-1])
        elif item[-1] is True:

            categories = driver.find_elements(By.CSS_SELECTOR, settings.category_css)
            for i in categories:
                if key == i.text.split('\n')[0]:
                    current_category = i
            current_item = current_category.find_element(By.CSS_SELECTOR, settings.item_css)
            current_button = current_item.find_element(By.CSS_SELECTOR, settings.button_of_item_css)
            
            driver.execute_script("arguments[0].click();", current_button)
            time.sleep(1)
        
        elif key == 'Опыт работы':

            categories = driver.find_elements(By.CSS_SELECTOR, settings.category_css)
            for i in categories:
                if key == i.text.split('\n')[0]:
                    current_category = i
                    

            items = current_category.find_elements(By.CSS_SELECTOR, settings.item_css)
            for i in items:
                print(i.text.split('\n')[0])
                if i.text.split('\n')[0] == item[-1]:
                    current_item = i
            print('\n', current_item.text)
            current_button = current_item.find_element(By.CSS_SELECTOR, 'input[class="magritte-radio-input___-IM3Y_3-0-21 magritte-radio-input-unchecked___J-rPE_3-0-21"]')
            # if not current_button.is_enabled:
            #     driver.execute_script("arguments[0].click();", current_button)
            try:
                current_button.click()
            except Exception as ex:
                time.sleep(0.5)
                current_button.click()
              
        elif key == 'Специализации':
            categories = driver.find_elements(By.CSS_SELECTOR, settings.category_css)
            for i in categories:
                if key == i.text.split('\n')[0]:
                    current_category = i
                
            choose_more = current_category.find_element(By.CSS_SELECTOR, 'div[data-qa="serp__novafilter-item-more"] button')#.find_element(By.CSS_SELECTOR, 'span[class="magritte-text___tkzIl_4-3-8"]')
            try:
                choose_more.click()
            except Exception as ex:
                time.sleep(1)
                choose_more.click()

            
            search = driver.find_element(By.CSS_SELECTOR,'[type="search"]')
            for i in item[1:]:
                search.clear()
                search.send_keys(i)
                name=driver.find_element(By.CSS_SELECTOR, 'div[class="bloko-tree-selector-item bloko-tree-selector-item_no-children"]')
                name = name.find_element(By.CSS_SELECTOR, '[class="bloko-tree-selector-content"]')
                try:
                    name.click()
                except Exception as ex:
                    time.sleep(1)
                    name.click()
                time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, 'button[class="bloko-button bloko-button_kind-primary"]').click()

        elif key == 'Ключевые слова':
            categories = driver.find_elements(By.CSS_SELECTOR, settings.category_css)
            for i in categories:
                if key == i.text.split('\n')[0]:
                    current_category = i
                
            x=item[0][1]
            y=item[1][1]
            z=item[2][1]
            
            
            items = current_category.find_elements(By.CSS_SELECTOR, settings.item_css)
            x_check= items[0].find_element(By.CSS_SELECTOR, 'div[class=magritte-item___h-S-Z_4-0-15]')
            if x==True and x_check.is_enabled()==False:
                current_button = x_check.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="search_field"]')
                try:
                    current_button.click()
                except Exception as ex:
                    time.sleep(0.5)
                    current_button.click()
            if x==False and x_check.is_enabled()==True:
                current_button = x_check.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="search_field"]')
                try:
                    current_button.click()
                except Exception as ex:
                    time.sleep(0.5)
                    current_button.click()


            y_check= items[1].find_element(By.CSS_SELECTOR, 'div[class=magritte-item___h-S-Z_4-0-15]')
            if y==True and y_check.is_enabled()==False:
                current_button = y_check.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="search_field"]')
                try:
                    current_button.click()
                except Exception as ex:
                    time.sleep(0.5)
                    current_button.click()
            if y==False and y_check.is_enabled()==True:
                current_button = y_check.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="search_field"]')
                try:
                    current_button.click()
                except Exception as ex:
                    time.sleep(0.5)
                    current_button.click()
  
            
            z_check= items[2].find_element(By.CSS_SELECTOR, 'div[class=magritte-item___h-S-Z_4-0-15]')
            if z==True and z_check.is_enabled()==False:
                current_button = z_check.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="search_field"]')
                try:
                    current_button.click()
                except Exception as ex:
                    time.sleep(0.5)
                    current_button.click()
            if z==False and z_check.is_enabled()==True:
                current_button = z_check.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="search_field"]')
                try:
                    current_button.click()
                except Exception as ex:
                    time.sleep(0.5)
                    current_button.click()         
            

        elif type(item[-1]) is int:

            categories = driver.find_elements(By.CSS_SELECTOR, settings.category_css)
            for i in categories:
                if key == i.text.split('\n')[0]:
                    current_category = i
                    
            for i in item[1:]:
                current_item = current_category.find_elements(By.CSS_SELECTOR, settings.item_css)
                current_item = current_item[i]
                print(current_item.text)
                current_button = current_item.find_element(By.CSS_SELECTOR, settings.button_of_item_css)
                if not current_button.is_enabled:
                    driver.execute_script("arguments[0].click();", current_button)
        
        elif type(item[-1]) is str:
            categories = driver.find_elements(By.CSS_SELECTOR, settings.category_css)
            for i in categories:
                if key == i.text.split('\n')[0]:
                    current_category = i
            current_item = current_category.find_element(By.CSS_SELECTOR, settings.item_css)
            current_button = current_item.find_element(By.CSS_SELECTOR, 'input[data-qa]')
            current_button.send_keys(item[-1])
    return driver

def exp(driver):
    for key, item in settings.settings.items():
        if key == 'Опыт работы':

            categories = driver.find_elements(By.CSS_SELECTOR, settings.category_css)
            for i in categories:
                if key == i.text.split('\n')[0]:
                    current_category = i
                    

            items = current_category.find_elements(By.CSS_SELECTOR, settings.item_css)
            for i in items:
                print(i.text.split('\n')[0])
                if i.text.split('\n')[0] == item[-1]:
                    current_item = i
            print('\n', current_item.text)
            current_button = current_item.find_element(By.CSS_SELECTOR, 'input[class="magritte-radio-input___-IM3Y_3-0-21 magritte-radio-input-unchecked___J-rPE_3-0-21"]')
            # if not current_button.is_enabled:
            #     driver.execute_script("arguments[0].click();", current_button)
            try:
                current_button.click()
            except Exception as ex:
                time.sleep(0.5)
                current_button.click()

def set_key_words(driver):
    for key, item in settings.settings.items():
        if key == 'Ключевые слова':
            categories = driver.find_elements(By.CSS_SELECTOR, settings.category_css)
            for i in categories:
                if key == i.text.split('\n')[0]:
                    current_category = i
                
            x=item[0][1]
            y=item[1][1]
            z=item[2][1]
            
            
            items = current_category.find_elements(By.CSS_SELECTOR, settings.item_css)
            x_check= items[0].find_element(By.CSS_SELECTOR, 'div[class=magritte-item___h-S-Z_4-0-15]')
            if x==True and x_check.is_enabled()==False:
                current_button = x_check.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="search_field"]')
                try:
                    current_button.click()
                except Exception as ex:
                    time.sleep(0.5)
                    current_button.click()
            if x==False and x_check.is_enabled()==True:
                current_button = x_check.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="search_field"]')
                try:
                    current_button.click()
                except Exception as ex:
                    time.sleep(0.5)
                    current_button.click()


            y_check= items[1].find_element(By.CSS_SELECTOR, 'div[class=magritte-item___h-S-Z_4-0-15]')
            if y==True and y_check.is_enabled()==False:
                current_button = y_check.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="search_field"]')
                try:
                    current_button.click()
                except Exception as ex:
                    time.sleep(0.5)
                    current_button.click()
            if y==False and y_check.is_enabled()==True:
                current_button = y_check.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="search_field"]')
                try:
                    current_button.click()
                except Exception as ex:
                    time.sleep(0.5)
                    current_button.click()

            
            z_check= items[2].find_element(By.CSS_SELECTOR, 'div[class=magritte-item___h-S-Z_4-0-15]')
            if z==True and z_check.is_enabled()==False:
                current_button = z_check.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="search_field"]')
                try:
                    current_button.click()
                except Exception as ex:
                    time.sleep(0.5)
                    current_button.click()
            if z==False and z_check.is_enabled()==True:
                current_button = z_check.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="search_field"]')
                try:
                    current_button.click()
                except Exception as ex:
                    time.sleep(0.5)
                    current_button.click()
                
def parse(driver): 
    
    try:
        vacancies = driver.find_elements(By.CSS_SELECTOR, 'div[data-sentry-element="Element"]')

        for i in range(len(vacancies)):
            time.sleep(1)
            
            # Re-find the vacancies in each loop iteration
            vacancies = driver.find_elements(By.CSS_SELECTOR, 'div[data-sentry-element="Element"]')
            
            try:
                response_button = vacancies[i].find_element(By.CSS_SELECTOR, 'a[class="magritte-button___Pubhr_5-2-1 magritte-button_mode-primary___wU8PN_5-2-1 magritte-button_size-medium___WvUsb_5-2-1 magritte-button_style-accent___TE21J_5-2-1"]')
                
                url1 = driver.current_url
                try:
                    response_button.click()
                    time.sleep(1)
                except Exception as ex:
                    time.sleep(0.5)
                    response_button.click()
                    time.sleep(1)
                
                url2 = driver.current_url
                
                if url1 != url2:
                    driver.back()
                    time.sleep(1)  # Add a short delay to allow the page to fully load

            except Exception as ex:
                print("Element not found:", ex)

        next_button = driver.find_element(By.CSS_SELECTOR, 'a[data-qa="number-pages-next"]')
        next_button.click()
        time.sleep(1)
        return parse(driver)
    except NoSuchElementException:
        return driver

   
def main():
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    profile_path=r"C:\Users\yarm\AppData\Local\Google\Chrome\User Data"
    options.add_argument(f"user-data-dir={profile_path}")
    options.add_argument("--profile-directory=Profile 1")
    driver = webdriver.Chrome(options=options)
    
    #Заход на страницу
    driver.get(base_url)
    find_button=driver.find_element(By.CSS_SELECTOR,'span[class="magritte-button__label___zplmt_5-2-1"]')
    #find_button.is_enabled
    try:
        find_button.click()
    except Exception as ex:
        time.sleep(0.5)
        find_button.click()
    
    # Поиск по запросу
    for tag in settings.search_query:
        search_line = driver.find_element(By.CSS_SELECTOR, settings.search_line_css)

        try:
            clear_button=driver.find_element(By.CSS_SELECTOR, 'button[data-qa="input-clearable-button"]')
            clear_button.click()
        except NoSuchElementException:
            pass

        search_line.send_keys(tag)
        time.sleep(0.5)
        find_button=driver.find_element(By.CSS_SELECTOR,'span[class="magritte-button__label___zplmt_5-2-1"]')
        #!find_button.isE
        try:
            find_button.click()
        except Exception as ex:
            time.sleep(0.5)
            find_button.click()
        
        setup_func(driver)
        # Поиск и выгрузка результатов
        parse(driver)
    
    time.sleep(100)
    
    # Закрытие драйвера
    driver.quit()
    
if __name__ == '__main__':
    main()
    