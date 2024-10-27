import requests
from scholarly import scholarly
from concurrent.futures import ThreadPoolExecutor

def update_notion_page(page, headers):
    title = page['properties']['Title']['rich_text'][0]['plain_text']
    search_query = scholarly.search_single_pub(title)
    
    if search_query is None:
        print(f"Failed to find paper {title}")
        return

    update_url = f"https://api.notion.com/v1/pages/{page['id']}"
    update_data = {
    "properties": {
        "Citations": {  # Update the citations property
            "number": search_query['num_citations']
        },
        "Date": {  # Update the date property as rich_text
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": search_query['bib']['pub_year']  # Set the date as text
                    }
                }
            ]
        }
    }
}
    
    update_response = requests.patch(update_url, headers=headers, json=update_data)
    if update_response.status_code == 200:
        print(f"Successfully updated: {title}")
    else:
        print(f"Failed to update: {title}, {update_response.text}")





if __name__ == "__main__":
    database_id = r"939da8e7c0e78e7c070e78e7c07"
    url = f"https://api.notion.com/v1/databases/{database_id}/query"

    Integration_token = r'M9RPpcTyDuUwSXNcTywSXNCPpc77LM9RPpcTyDuUwSXNcTyDuUwSXNC'
    headers = {
        "Authorization": "Bearer %s" % (Integration_token),
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        with ThreadPoolExecutor() as executor:
            futures = []
            for page in data['results']:

                # Personalized logic
                if any(item['name'] == 'Sampling' for item in page['properties']['Domain']['multi_select']):
                    futures.append(executor.submit(update_notion_page, page, headers))
            for future in futures:
                future.result()  # Wait for the future to complete
    else:
        print(f"Error querying database: {response.status_code}, {response.text}")
