import requests
from scholarly import scholarly



if __name__ == "__main__":

    # Notion API URL
    database_id = r"8e7c060e079d30e079d30e079d30"
    url = "https://api.notion.com/v1/databases/%s/query" % (database_id)


    # Notion API headers
    Integration_token = r"Mntn_M877_n_Mntn_M877443077ntn_M877443077242"
    headers = {
        "Authorization": "Bearer %s" % (Integration_token),
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    # Query the database
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for result in data['results']:

            # Personalized logic
            if any(item['name'] == 'Sampling' for item in result['properties']['Domain']['multi_select']):

                title = result['properties']['Title']['rich_text'][0]['plain_text']
                search_query = scholarly.search_single_pub(title)
                if search_query is None:
                    print(f"Failed to find paper {title}")
                    continue

                update_url = f"https://api.notion.com/v1/pages/{result['id']}"
                update_data = {
                    "properties": {
                        "Citations": {  # Update the citations property
                            "number": search_query['num_citations']
                        }
                    }
                }
                
                update_response = requests.patch(update_url, headers=headers, json=update_data)
                if update_response.status_code == 200:
                    print(f"Successfully: {title}")
                else:
                    print(f"Failed: {title}, {update_response.text}")
    else:
        print(f"Error querying database: {response.status_code}, {response.text}")