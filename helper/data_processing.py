def process_raw_data(raw_data):
    # Initialize an empty list to store processed items
    processed_data = []
    
    # Process each item in raw_data
    for item in raw_data:
        processed_item = {
            "name": item["name"].upper(),  # Convert the name to uppercase
            "address": item["address"].title(),  # Capitalize each word in the address
            "website": item["website"],  # Keep the website as it is
            "phone": item["phone"],  # Keep the phone number as it is
            "reviews": item["reviews"],  # Keep the reviews as they are
            "rating": item["rating"],  # Keep the rating as it is
        }
        processed_data.append(processed_item)
    
    return processed_data
