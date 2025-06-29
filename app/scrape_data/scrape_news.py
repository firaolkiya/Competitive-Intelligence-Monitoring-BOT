from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

walmart_news="https://corporate.walmart.com/newsroom"
ebay_news="https://www.ebayinc.com/stories/news/	"
bestbuy_news="https://corporate.bestbuy.com/news/"
async def scrape_walmart_news(driver):
    
    driver.get(walmart_news)
    try:
        WebDriverWait(driver,50).until(
            EC.presence_of_element_located((By.CLASS_NAME,"in-page__title"))
    )
    except:
        return await scrape_walmart_news(driver)
    wrapper = driver.find_element(By.XPATH,"//*[@id=\"inpage-search-list\"]/li[1]/div/a")
    link=wrapper.get_attribute("href")
    
    titles=driver.find_element(By.CLASS_NAME,"in-page__title").text
    driver.get(link if link else walmart_news)
    
    time.sleep(5)
    description = driver.find_elements(By.TAG_NAME,"p")
    news1=[]
    for p in description:
        descr=p.text.strip()
        if descr!="":
            news1.append(descr)
    recent_news="\n".join(news1)
    return recent_news


async def scrape_ebay_news(driver):
    
    driver.get(ebay_news)
    try:
        WebDriverWait(driver,50).until(
            EC.presence_of_element_located((By.CLASS_NAME,"article-content"))
    )
    except:
        return await scrape_ebay_news(driver)
    wrapper = driver.find_element(By.XPATH,"//*[@id=\"main-content\"]/div[3]/div/div[2]/div[1]/a")
    link=wrapper.get_attribute("href")
    
    # titles=driver.find_element(By.CLASS_NAME,"in-page__title").text
    driver.get(link if link else ebay_news)
    
    time.sleep(5)
    description = driver.find_elements(By.TAG_NAME,"p")
    news1=[]
    for p in description:
        descr=p.text.strip()
        if descr!="":
            news1.append(descr)
    recent_news="\n".join(news1)
    return recent_news

async def scrape_bestbuy_news(driver):
    
    driver.get(bestbuy_news)
    try:
        WebDriverWait(driver,50).until(
            EC.presence_of_element_located((By.CLASS_NAME,"article-content"))
    )
    except:
        return await scrape_ebay_news(driver)
    wrapper = driver.find_element(By.XPATH,"//*[@id=\"main-content\"]/div[3]/div/div[2]/div[1]/a")
    link=wrapper.get_attribute("href")
    
    # titles=driver.find_element(By.CLASS_NAME,"in-page__title").text
    driver.get(link if link else ebay_news)
    
    time.sleep(5)
    description = driver.find_elements(By.TAG_NAME,"p")
    news1=[]
    for p in description:
        descr=p.text.strip()
        if descr!="":
            news1.append(descr)
    recent_news="\n".join(news1)
    return recent_news


