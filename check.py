from curl_cffi import requests
import sys

LOG_FILE = "log.txt"

def log(message: str):
    """
    Prints a message to the console and writes the same message to log.txt
    """
    print(message)
    with open(LOG_FILE, 'a', encoding='utf-8') as lf:
        lf.write(message + "\n")

def main():
    with open(LOG_FILE, 'w', encoding='utf-8') as lf:
        lf.write("=== NodePay Token Checker Logs ===\n")
    tokens = []
    try:
        with open('token.txt', 'r', encoding='utf-8') as f:
            tokens = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        log("Could not find 'token.txt'. Make sure the file exists.")
        sys.exit(1)

    if not tokens:
        log("'token.txt' is empty. Please add at least one token.")
        sys.exit(1)

    log(f"Loaded {len(tokens)} token(s).")
    proxies_list = []
    try:
        with open('proxy.txt', 'r', encoding='utf-8') as f:
            proxies_list = [line.strip() for line in f if line.strip()]
        if proxies_list:
            log(f"Loaded {len(proxies_list)} proxy/proxies.")
            log("Proxy format is expected as: http://username:password@ip:port")
        else:
            log("No valid proxies found in 'proxy.txt'. Proceeding without proxies.")
    except FileNotFoundError:
        log("No 'proxy.txt' found. Proceeding without proxies.")
    url = "https://api.nodepay.ai/api/season/airdrop-status"
    base_headers = {
        "Accept": "*/*",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Content-Type": "application/json",
        "Priority": "u=1, i",
        "Sec-CH-UA": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                      "AppleWebKit/537.36 (KHTML, like Gecko) " \
                      "Chrome/131.0.0.0 Safari/537.36",
    }

    total_tokens = 0.0

    log("\nStarting checks...\n")
    for i, token in enumerate(tokens, start=1):
        log(f"[Token #{i}] Checking token: {token[:10]}{'...' if len(token) > 10 else ''}")
        headers = dict(base_headers)
        headers["Authorization"] = f"Bearer {token}"
        if proxies_list:
            proxy_index = (i - 1) % len(proxies_list)
            proxy_str = proxies_list[proxy_index]
            current_proxy = {
                "http":  proxy_str,
                "https": proxy_str
            }
            log(f" -> Using proxy: {proxy_str}")
        else:
            current_proxy = None
        try:
            response = requests.get(url, headers=headers, proxies=current_proxy, timeout=10)
            try:
                data = response.json()
            except ValueError:
                log(" -> Warning: Response is not valid JSON. Raw text:")
                log(response.text)
                continue
            status_code = response.status_code
            log(f" -> Status Code: {status_code}")
            log(f" -> Response JSON: {data}")
            if data.get("success") and isinstance(data.get("data"), dict):
                season_0_1_2_tokens = data["data"].get("season_0_1_2_tokens") or 0.0
                if season_0_1_2_tokens is None:
                    season_0_1_2_tokens = 0.0

                total_tokens += float(season_0_1_2_tokens)
            
            log("")

        except requests.exceptions.RequestException as e:
            log(f" -> Error: {e}\n")
    log("All tokens have been checked.\n")
    log(f"Congratulations!! From Phantom :  Your total NodePay tokens are: {total_tokens} $NC")

if __name__ == "__main__":
    main()
