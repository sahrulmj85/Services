import requests
from datetime import datetime
import os
import time

# List of URLs
urls = [
"https://ss.shipmentlink.com/tvs2/download_txt/APG_9.txt",
"https://ss.shipmentlink.com/tvs2/download_txt/AUE_W.txt",
"https://ss.shipmentlink.com/tvs2/download_txt/CEM_E.txt",
"https://ss.shipmentlink.com/tvs2/download_txt/CES_E.txt",
"https://ss.shipmentlink.com/tvs2/download_txt/HTW_W.txt",
"https://ss.shipmentlink.com/tvs2/download_txt/CMEX_9.txt",
"https://ss.shipmentlink.com/tvs2/download_txt/MEX1_E.txt",
"https://ss.shipmentlink.com/tvs2/download_txt/BEX_E.txt",
"https://ss.shipmentlink.com/tvs2/download_txt/BEX2_E.txt",
"https://ss.shipmentlink.com/tvs2/download_txt/FAL1_E.txt",
"https://ss.shipmentlink.com/tvs2/download_txt/FAL3_E.txt",
"https://ss.shipmentlink.com/tvs2/download_txt/PE1_1.txt",
"https://ss.shipmentlink.com/tvs2/download_txt/CBX_W.txt",
    # Add more URLs here
]

# Create save folder based on today's date
today_str = datetime.now().strftime("%Y-%m-%d")  # example: '2025-04-27'
save_folder = os.path.join("downloads", today_str)
os.makedirs(save_folder, exist_ok=True)

# Show where the files will be saved
print("Saving files into:", os.path.abspath(save_folder))

# Download each file
for url in urls:
    try:
        print(f"\nStarting download: {url}")
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            # Get original filename from URL
            original_filename = url.split("/")[-1]
            name_part, extension = os.path.splitext(original_filename)

            # Generate unique timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")

            # New filename
            new_filename = f"{name_part}_{timestamp}{extension}"
            filepath = os.path.join(save_folder, new_filename)

            # Save file
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(response.text)

            print(f"✅ Downloaded and saved as {filepath}")
        else:
            print(f"❌ Failed to download {url}: Status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error downloading {url}: {e}")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")

    # Sleep 1 second between downloads
    time.sleep(1)
