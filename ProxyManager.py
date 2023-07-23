from dotenv import load_dotenv
import os
import requests


def env(name):
    load_dotenv()
    return os.environ.get(name)


host = env("PROXY_HOST")
username = env("PROXY_USERNAME")
password = env("PROXY_PASSWORD")


def createSession(port):
    proxies = {
        "http": f"http://{username}:{password}@{host}:{port}",
        "https": f"http://{username}:{password}@{host}:{port}",
    }

    session = requests.Session()
    session.proxies.update(proxies)
    return session


if __name__ == "__main__":
    response = session.get("https://api.ipify.org")
    print(response.text)
