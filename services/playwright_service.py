import csv
from playwright.sync_api import sync_playwright

def scrape_and_save_csv(business_name, limit):
    output_file = f"{business_name.replace(' ', '_')}_results.csv"
    results = []

    with sync_playwright() as p:
        # Launch browser in view mode (headless=False)
        browser = p.chromium.launch(headless=False)  # Open browser with UI
        page = browser.new_page()
        
        # Navigate to Google Maps
        page.goto("https://www.google.com/maps")
        page.fill("input[aria-label='Search Google Maps']", business_name)
        page.keyboard.press("Enter")
        page.wait_for_timeout(5000)  # Wait for search results to load

        # Scrape results
        for i in range(limit):
            try:
                business = page.locator(".Nv2PK").nth(i)
                name = business.locator(".qBF1Pd").inner_text()
                address = business.locator(".HlvSq").inner_text()
                phone = business.locator(".MVVflb").inner_text()  # May vary by structure
                
                results.append({
                    "name": name,
                    "address": address,
                    "phone": phone
                })
            except Exception as e:
                # Skip if there's an error (e.g., missing element)
                print(f"Error scraping item {i + 1}: {e}")
                continue

        browser.close()

    # Save results to a CSV file
    with open(output_file, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "address", "phone"])
        writer.writeheader()
        writer.writerows(results)

    return output_file
