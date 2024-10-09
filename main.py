import requests

def get_account_info(fb_id_token):
    url = "https://graph.facebook.com/me"
    params = {'access_token': fb_id_token}
    response = requests.get(url, params=params)
    data = response.json()
    return data['name']

def get_pages_tokens(fb_id_token):
    url = "https://graph.facebook.com/me/accounts"
    params = {'access_token': fb_id_token}
    response = requests.get(url, params=params)
    data = response.json()
    pages_tokens = {}
    if 'data' in data:
        for page in data['data']:
            pages_tokens[page['name']] = page['access_token']
    return pages_tokens

def main():
    fb_id_token = input("Enter your Facebook ID token: ")
    account_name = get_account_info(fb_id_token)
    print("Account Name:", account_name)

    pages_tokens = get_pages_tokens(fb_id_token)
    print("Pages:")
    for page, token in pages_tokens.items():
        print(f"  {page} - Token: {token}")

if __name__ == '__main__':
    main()
