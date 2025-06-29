from playwright.async_api import async_playwright,Page
import random
import asyncio
walProductListing="https://www.walmart.com/search?q=keyword"
ebayProductListing="https://www.ebay.com/sch/i.html?_nkw=keyword"
bestbuyProductListing="https://www.bestbuy.com/site/searchpage.jsp?"


async def human_hold(page: Page, hold_sec: float = 4.0):
    try:
        outer = await page.wait_for_selector("#px-captcha iframe", timeout=10000)
        # 2️⃣ Wait until it gets a non‑empty src (PX just populated it)
        await outer.wait_for_element_state("stable")          # type: ignore
        await page.wait_for_timeout(500)                   
        outer_frame = outer.content_frame()                # type: ignore 

        # 3️⃣ Inside outer frame, wait for the *inner* widget frame
        inner = await outer_frame.wait_for_selector("iframe", timeout=10000) # type: ignore
        inner_frame = inner.content_frame()

        # 4️⃣ Now the “Press & Hold” button is inside inner_frame
        button = await inner_frame.wait_for_selector("div[role='button']", timeout=10000)

        # Centre mouse, press, jitter a bit, then release
        box = await button.bounding_box()
        x = box["x"] + box["width"] / 2
        y = box["y"] + box["height"] / 2
        await page.mouse.move(x, y)
        await page.mouse.down()
        for _ in range(int(hold_sec * 10)):
            await page.mouse.move(x + random.uniform(-2, 2), y + random.uniform(-2, 2))
            await asyncio.sleep(0.1)
        await page.mouse.up()

        # 5️⃣ Wait until the widget disappears (PX sets display:none)
        await outer_frame.wait_for_selector("div[role='button']", state="detached", timeout=10000) # type: ignore
        print("PX challenge passed")
    except:
        print("unable find challege")

async def scrape_walmart_products(page:Page):
        # Wait for product tiles to appear
        await page.goto(walProductListing) 
        await page.wait_for_selector('[data-automation-id="product-title"]')

        # Get all product containers
        products = await page.query_selector_all('[role="group"][data-item-id]')

        response=[]
            
        for product in products:
            try:
                # Title
                title_el = await product.query_selector('[data-automation-id="product-title"]')
                title = await title_el.inner_text() if title_el else "N/A"

                # Price
                price_el = await product.query_selector('[data-automation-id="product-price"]')
                price = await price_el.inner_text() if price_el else "N/A"

                # Image
                img_el = await product.query_selector('[data-testid="productTileImage"]')
                img_url = await img_el.get_attribute("src") if img_el else "N/A"

                # Product URL
                link_el = await product.query_selector('a[href*="/ip/"]')
                href = await link_el.get_attribute("href") if link_el else "N/A"
                full_url = f"https://www.walmart.com{href}" if href else "N/A"
                data=[title,price,img_url,full_url]
                response.append(data)
                return response
            except Exception as e:
                print("Error parsing product:", e)

async def scrape_ebay_products(page:Page):
        # Wait for product tiles to appear
        await page.goto(ebayProductListing) 
        await page.wait_for_selector('.s-item__info')

        # Get all product containers
        await page.wait_for_selector('li.s-item[data-view*="iid:"]')

        products = await page.query_selector_all('li.s-item[data-view*="iid:"]')
        print(f"Found {len(products)} products")
        response = []
        for item in products:
            title_el = await item.query_selector(".s-item__title")
            price_el = await item.query_selector(".s-item__price")
            link_el  = await item.query_selector("a.s-item__link")
            img_el   = await item.query_selector(".s-item__image img")

            title = await title_el.inner_text()  if title_el else "N/A"
            price = await price_el.inner_text()  if price_el else "N/A"
            href  = await link_el.get_attribute("href") if link_el else "N/A"
            img   = await img_el.get_attribute("src")   if img_el else "N/A"
            response.append([title,price,href,img])
        return response
            
