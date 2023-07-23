from async_proxy import get_connector
import asyncio
import aiohttp
import traceback


async def send_request(url, port: int, dom):
    async with aiohttp.ClientSession(
        connector=await get_connector(port),
        cookie_jar=aiohttp.CookieJar(unsafe=True),
        timeout=aiohttp.ClientTimeout(total=1),
    ) as session:
        url = url
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9",
            "cookie": f"QueueITAccepted-SDFrts345E-V3_lfchospseason111022=EventId%3Dlfchospseason111022%26RedirectType%3Dsafetynet%26IssueTime%3D1689940092%26Hash%3Dg966ddcbffa8467ff0b7345bad49975b5f18b4320d7754d2040a2bdfae277e75;datadome={dom};",
            "origin": "https://ticketing.liverpoolfc.com",
            "referer": "https://ticketing.liverpoolfc.com/",
            "cache-control": "max-age=0",
            "sec-ch-device-memory": "8",
            "sec-ch-ua": '"Chromium";v="115", "Not A(Brand";v="99", "Google Chrome";v="115"',
            "sec-ch-ua-arch": '"x86"',
            "sec-ch-ua-full-version-list": '"Chromium";v="115.0.5790.98", "Not A(Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.98"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": '""',
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Referrer-Policy": "strict-origin-when-cross-origin",
        }
        try:
            async with session.get(url=url, headers=headers) as response:
                response.close()
                print(response.status)
                # print(r.text)
                if response.status == 200:
                    print(port)
                    # print(f"cookie datadome: {r.cookies.get('datadome')}")
                    # return response.cookies.get("datadome")
        except asyncio.TimeoutError:
            # print("timeout")
            pass
        except Exception as error:
            pass
            # pass
            # tb = traceback.format_exc()
            # line_number = int(tb.split(", ")[1].replace("line ", ""))
            # print(f"Error on line {line_number}: {e}")


async def main():
    ports = range(35700, 35710)

    tasks = [
        send_request(
            "https://ticketing.liverpoolfc.com/usercontent/splash.html", port, ""
        )
        for port in ports
    ]
    await asyncio.gather(*tasks)


# send_request("https://ticketing.liverpoolfc.com/usercontent/splash.html", 35766, "")
asyncio.run(main())
