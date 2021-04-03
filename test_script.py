from asyncio import run
from time import time

import proxygrab


class Test:
    @staticmethod
    async def run_all():
        print("Starting test...")
        start = time()
        success = 0
        try:
            p1 = await proxygrab.get_http()
            success += 1
            print("HTTP:", len(p1))
        except Exception as ef:
            print("Error:", ef)

        try:
            p2 = await proxygrab.get_https()
            success += 1
            print("HTTPS:", len(p2))
        except Exception as ef:
            print("Error:", ef)

        try:
            p3 = await proxygrab.get_socks4()
            success += 1
            print("SOCKS4:", len(p3))
        except Exception as ef:
            print("Error:", ef)

        try:
            p4 = await proxygrab.get_socks5()
            success += 1
            print("SOCKS5:", len(p4))
        except Exception as ef:
            print("Error:", ef)

        try:
            p5 = await proxygrab.get_proxy("http")
            success += 1
            print("HTTP(GetProxyM):", len(p5))
        except Exception as ef:
            print("Error:", ef)

        try:
            p6 = await proxygrab.get_proxy("https")
            success += 1
            print("HTTPS(GetProxyM):", len(p6))
        except Exception as ef:
            print("Error:", ef)

        try:
            p7 = await proxygrab.get_proxy("socks4")
            success += 1
            print("SOCKS4(GetProxyM):", len(p7))
        except Exception as ef:
            print("Error:", ef)

        try:
            p8 = await proxygrab.get_proxy("socks5")
            success += 1
            print("SOCKS5(GetProxyM):", len(p8))
        except Exception as ef:
            print("Error:", ef)

        try:
            g = await proxygrab.get_all_proxies()
            success += 1
            print("All(GetProxyM):", len(g))
        except Exception as ef:
            print("Error:", ef)

        try:
            s = await proxygrab.save_all_proxies()
            success += 1
            print(f"Saved all proxies to {s}")
        except Exception as ef:
            print("Error:", ef)

        try:
            p1 = await proxygrab.save_http()
            success += 1
            print("Saved http proxies")
        except Exception as ef:
            print("Error:", ef)

        try:
            p2 = await proxygrab.save_https()
            success += 1
            print("Saved https proxies")
        except Exception as ef:
            print("Error:", ef)

        try:
            p3 = await proxygrab.save_socks4()
            success += 1
            print("Saved socks4 proxies")
        except Exception as ef:
            print("Error:", ef)

        try:
            p4 = await proxygrab.save_socks5()
            success += 1
            print("Saved socks5 proxies")
        except Exception as ef:
            print("Error:", ef)

        try:
            p5 = await proxygrab.save_proxy("http")
            success += 1
            print("Saved http SaveM proxies")
        except Exception as ef:
            print("Error:", ef)

        try:
            p6 = await proxygrab.save_proxy("https")
            success += 1
            print("Saved https SaveM proxies")
        except Exception as ef:
            print("Error:", ef)

        try:
            p7 = await proxygrab.save_proxy("socks4")
            success += 1
            print("Saved socks4 SaveM proxies")
        except Exception as ef:
            print("Error:", ef)

        try:
            p8 = await proxygrab.save_proxy("socks5")
            success += 1
            print("Saved socks5 SaveM proxies")
        except Exception as ef:
            print("Error:", ef)

        end = time()
        print(f"Time Taken for running the test: {round(end-start,3)}s")
        return success


run(Test.run_all())
