from config import SeleniumManager,Playwright


async def main():
    seleniumManager = SeleniumManager()
    driver = seleniumManager.get_driver()
    # news=await scrape_ebay_news(driver)
    # print(news)
    # playWrightManager=PlayWrightManager()
    # await playWrightManager.setup()
    # page = await playWrightManager.get_page()
    # producs=await scrape_ebay_products(page)
    # print(producs)
    # time.sleep(5)
    # # await human_hold(page)   
    # products = await scrape_walmart_products(page)
    # time.sleep(100)  
    # recent_news  = await fetchNews(driver)
    # await playWrightManager.close_browser()
    seleniumManager.close_driver()
    
    

# asyncio.run(main())
        
