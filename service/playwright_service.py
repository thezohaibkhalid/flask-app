import csv
from playwright.sync_api import sync_playwright

def scrape_and_save_csv(business_name, limit):
    output_file = f"{business_name}_results.csv"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Navigate to the search page
        page.goto("https://example.com/search")
        
        # Perform the search
        page.fill("input[name='search']", business_name)
        page.click("button[type='submit']")
        page.wait_for_timeout(3000)
        
        # Scrape the results
        results = []
        for i in range(min(limit, len(page.locator(".result-item").all()))):
            result = page.locator(".result-item").nth(i)
            name = result.locator(".name").inner_text()
            address = result.locator(".address").inner_text()
            phone = result.locator(".phone").inner_text()
            
            results.append({
                "name": name,
                "address": address,
                "phone": phone
            })
        
        browser.close()
    
    # Save results to a CSV file
    with open(output_file, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "address", "phone"])
        writer.writeheader()
        writer.writerows(results)
    
    return output_file
