#!/usr/bin/env python

__authors__ = ["Peter W. Njenga"]
__copyright__ = "Copyright © 2023 NNext, Co."

# Standard Libraries
import os
from pprint import pprint

# External Libraries
from playwright.async_api import async_playwright
import redis
from loguru import logger
from nnext.lib.core.main import Agent, Tool

# Internal Libraries
None

# Global Variables
BRIGHT_DATA_KEY = os.environ.get("BRIGHT_DATA_KEY")
browser_url = f'wss://{BRIGHT_DATA_KEY}@brd.superproxy.io:9222'

@Tool(
    name="browser",
    invoke_commands=["browse", "visit", "open"]
)
async def visit_url(url, *args, **kwargs):
    async with async_playwright() as pw:
        logger.debug(f'connecting to browser');
        browser = await pw.chromium.connect_over_cdp(browser_url)
        logger.debug('connected  to browser');
        page = await browser.new_page()

        logger.info(f'visiting {url}')
        try:
            await page.goto(url, timeout=120000)
        except Exception as e:
            return None

        await page.screenshot(path=f"{id}-screenshot.png")

        texts = await page.locator('div').all_inner_texts()

        await browser.close()

    return texts

if __name__ == "__main__":
    logger.info(f"Starting browser tool agent")
    visit_url.run()