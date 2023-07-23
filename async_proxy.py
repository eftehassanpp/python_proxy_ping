from dotenv import load_dotenv
import os
import requests
import aiohttp
import aiohttp_proxy
import asyncio


def env(name):
    load_dotenv()
    return os.environ.get(name)


host = env("PROXY_HOST")
username = env("PROXY_USERNAME")
password = env("PROXY_PASSWORD")


async def get_connector(port) -> aiohttp_proxy.ProxyConnector:
    proxies = f"http://{username}:{password}@{host}:{port}"
    connector = aiohttp_proxy.ProxyConnector.from_url(proxies)
    return connector


if __name__ == "__main__":
    response = session.get("https://api.ipify.org")
    print(response.text)
