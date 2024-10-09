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

    # Send a GET request to the Facebook API
    response = requests.get(endpoint, headers=headers)

    # Parse the JSON response
    data = response.json()

    # Initialize an empty dictionary to store the page tokens
    pages_tokens = {}

    # Iterate over the pages in the response
    for page in data["data"]:
        # Check if the page has an access token
        if "access_token" in page:
            # Add the page token to the dictionary
            pages_tokens[page["name"]] = page["access_token"]
        else:
            # If no access token, print a warning message
            print(f"Warning: No access token found for page {page['name']}")

    return pages_tokens

def main():
    # Prompt the user to enter their Facebook ID token
    fb_id_token = input("Enter your Facebook ID token: ")

    # Get the page tokens
    pages_tokens = get_pages_tokens(fb_id_token)

    # Print the page tokens
    for page, token in pages_tokens.items():
        print(f"Page: {page}, Token: {token}")

if __name__ == "__main__":
    main()
