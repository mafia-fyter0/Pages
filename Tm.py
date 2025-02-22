import requests

def get_pages_tokens(fb_id_token):
    """
    Get a list of pages and their corresponding access tokens
    """
    # Set the Facebook API endpoint and headers
    endpoint = "https://graph.facebook.com/v13.0/me/accounts"
    headers = {
        "Authorization": f"Bearer {fb_id_token}"
    }

    try:
        # Send a GET request to the Facebook API
        response = requests.get(endpoint, headers=headers)

        # Check if the response was successful
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return {}

        # Parse the JSON response
        data = response.json()

        # Initialize an empty dictionary to store the page tokens
        pages_tokens = {}

        # Iterate over the pages in the response
        for page in data["data"]:
            # Extract the page ID and name
            page_id = page["id"]
            page_name = page["name"]

            # Get the page access token using the Facebook ID token
            page_token_endpoint = f"https://graph.facebook.com/v13.0/{page_id}?fields=access_token&access_token={fb_id_token}"
            page_token_response = requests.get(page_token_endpoint, headers=headers)

            # Check if the response was successful
            if page_token_response.status_code != 200:
                print(f"Error: {page_token_response.status_code}")
                continue

            # Parse the JSON response
            page_token_data = page_token_response.json()

            # Extract the page access token
            if "access_token" in page_token_data:
                page_token = page_token_data["access_token"]
                pages_tokens[page_id] = {"name": page_name, "token": page_token}
            else:
                print(f"Warning: No access token found for page {page_name} (ID: {page_id})")

        return pages_tokens

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return {}

def main():
    # Prompt the user to enter their Facebook ID token
    fb_id_token = input("Enter your Facebook ID token: ")

    # Get the page tokens
    pages_tokens = get_pages_tokens(fb_id_token)

    # Print the page tokens
    for page_id, page_info in pages_tokens.items():
        print(f"Page ID: {page_id}, Name: {page_info['name']}, Token: {page_info['token']}")

if __name__ == "__main__":
    main()
