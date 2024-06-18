import requests
import time
from colorama import Fore, Style, init

init(autoreset=True)

def get_token(init_data):
    url = 'https://galaxywallet.xyz/api/create_account'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'cookie': '_ga=GA1.1.1562856008.1718620506; _ga_BD3BZ6GR39=GS1.1.1718620505.1.1.1718620507.0.0.0',
        'origin': 'https://galaxywallet.xyz',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://galaxywallet.xyz/create-account',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    data = {
        'init_data': init_data
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200 and response.json().get("success"):
        return response.json().get("auth_token")
    return None

def get_user_info(auth_token):
    url = 'https://galaxywallet.xyz/api/get_user_info'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {auth_token}',
        'cache-control': 'no-cache',
        'content-length': '0',
        'origin': 'https://galaxywallet.xyz',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://galaxywallet.xyz/create-account',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        user_info = response.json().get("user")
        if user_info:
            print(f"{Fore.YELLOW+Style.BRIGHT}[ Balance ] BNB: {user_info['bnb_balance']} | Galaxy: {user_info['galaxy_balance']}")
            print(f"{Fore.CYAN+Style.BRIGHT}[ Address ] {user_info['deposit_address']}")
            print(f"{Fore.CYAN+Style.BRIGHT}[ Claim ] {user_info['last_claim']}")
            print(f"{Fore.CYAN+Style.BRIGHT}[ Spaceship ] {user_info['spaceship_level']}")
            print(f"{Fore.CYAN+Style.BRIGHT}[ Astronaut ] {user_info['astronaut_level']}")
            print(f"{Fore.CYAN+Style.BRIGHT}[ Planet ] {user_info['planet_level']}")
            print(f"{Fore.CYAN+Style.BRIGHT}[ Countdown ] {user_info['countdown']}")
        return user_info
    return None


def claim_token(auth_token):
    url = 'https://galaxywallet.xyz/api/claim'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {auth_token}',
        'cache-control': 'no-cache',
        'content-length': '0',
        'origin': 'https://galaxywallet.xyz',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://galaxywallet.xyz/gas',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    response = requests.post(url, headers=headers)
    # print(response.text)
    if response.status_code == 200:
        print("Claim successful!")
      
    elif response.status_code == 400:
        # print(response.text)
        error_msg = response.text
        if "Not enough transaction fees" in error_msg:
            print("Not enough transaction fees.")
        elif "You have claimed enough quantity per day" in error_msg:
            print("You have claimed enough quantity per day. Wait until the next day to continue claiming!")
def animated_loading(duration):
    frames = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        for frame in frames:
            print(f"\rMenunggu waktu claim berikutnya {frame} - Tersisa {remaining_time} detik         ", end="", flush=True)
            time.sleep(0.25)
    print("\rMenunggu waktu claim berikutnya selesai.                            ", flush=True)     
def main():
    with open('query.txt', 'r') as file:
        accounts = file.readlines()

    while True:
        for account in accounts:
            init_data = account.strip()
            auth_token = get_token(init_data)
            if auth_token:
                get_user_info(auth_token)
                # print(f"{Fore.GREEN+Style.BRIGHT}Clearing task..{Style.RESET_ALL}")
                # clear_tasks(auth_token)
                print(f"{Fore.GREEN+Style.BRIGHT}Claiming rewards..{Style.RESET_ALL}")
                claim_token(auth_token)
                    
        animated_loading(300)  # Wait for 30 minutes before restarting the loop

if __name__ == "__main__":
    main()
