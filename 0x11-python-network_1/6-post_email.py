import requests
import sys
"""" Sends a POST request to the passed URL with the email as a parameter """

def send_post_request(url, email):
    try:
        payload = {'email': email}
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print("Response body:")
        print(response.text)
    except requests.RequestException as e:
        print(f"Error sending POST request: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url, email = sys.argv[1], sys.argv[2]
    send_post_request(url, email)
