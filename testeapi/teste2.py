import pandas as pd
import requests

def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception if the request was unsuccessful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def create_dataframe(data):
    filtered_data = [item for item in data if len(item.get("gtin14", "")) == 13]
    df = pd.DataFrame(filtered_data)
    return df


base_url = "https://www.brocade.io/api/items?page="
pages = range(7222)  # Add more page numbers if needed

all_data = []

for page in pages:
    print(f"page {page + 1} from 7222 {(page + 1) / 7222 * 100:.2f}% concluido")
    api_url = base_url + str(page+1)

    # Fetch data from the API
    data = fetch_data_from_api(api_url)

    if data:
        all_data.extend(data)

# Create a DataFrame from all the API data
df = create_dataframe(all_data)

# Display the DataFrame
print(df)

    # If you want to save the DataFrame to a CSV file, uncomment the following line
df.to_csv("api_data.csv", index=False)

print("concluido")
