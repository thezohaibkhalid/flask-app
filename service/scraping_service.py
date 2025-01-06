from playwright.sync_api import sync_playwright
import pandas as pd
from ..utils.csv_helper import save_to_csv

def scrape_and_save_csv(search_for, total):
    names_list, address_list, website_list, phones_list = [], [], [], []

    def extract_data(xpath, data_list, page):
        if page.locator(xpath).count() > 0:
            data = page.locator(xpath).inner_text()
        else:
            data = ""
        data_list.append(data)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.google.com/maps/@32.9817464,70.1930781,3.67z?", timeout=60000)
        page.locator('//input[@id="searchboxinput"]').fill(search_for)
        page.keyboard.press("Enter")
        page.wait_for_selector('//a[contains(@href, "https://www.google.com/maps/place")]')

        listings = page.locator('//a[contains(@href, "https://www.google.com/maps/place")]').all()[:total]

        for listing in listings:
            listing.click()
            page.wait_for_selector('//div[@class="TIHn2 "]//h1[@class="DUwDvf lfPIob"]')
            extract_data('//div[@class="TIHn2 "]//h1[@class="DUwDvf lfPIob"]', names_list, page)
            extract_data('//button[@data-item-id="address"]//div[contains(@class, "fontBodyMedium")]', address_list, page)
            extract_data('//a[@data-item-id="authority"]//div[contains(@class, "fontBodyMedium")]', website_list, page)
            extract_data('//button[contains(@data-item-id, "phone:tel:")]//div[contains(@class, "fontBodyMedium")]', phones_list, page)

        # Save to CSV
     

        data = list(zip(names_list, website_list, phones_list, address_list))
        columns = ['Name', 'Website', 'Phone Number', 'Address']
        save_to_csv(data, 'result.csv', columns)
        browser.close()
