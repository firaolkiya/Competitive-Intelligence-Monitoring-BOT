from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from playwright.async_api import async_playwright,Page,Browser,Playwright

driver=None
class SeleniumManager():
    def __init__(self) -> None:
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        # options.add_argument("window-size=1920x1080")

        # Launch Chrome using WebDriver Manager
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
    def get_driver(self):
        return self.driver # type: ignore
    
    def close_driver(self):
        self.driver.close()

class PlayWrightManager():
    def __init__(self) -> None:
        self._playwright_instance: Playwright = None # type: ignore
        self.browser: Browser = None # type: ignore
        self.page: Page = None # type: ignore
    
    async def setup(self):
        self._playwright_instance = await async_playwright().start()
        self.browser = await self._playwright_instance.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )
        self.page = await self.browser.new_page()
    
    async def get_page(self) -> Page:
        if not self.page:
            raise RuntimeError("PlaywrightManager.setup() must be called before accessing the page.")
        return self.page

    async def close_browser(self):
        if self.browser:
            await self.browser.close()
        if self._playwright_instance:
            await self._playwright_instance.stop()
        
