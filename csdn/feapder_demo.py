import feapder
import requests


class AirSpiderDemo(feapder.AirSpider):
    def start_requests(self):
        url = "https://ipinfo.io"
        params = {
            # "offset": "1646711833825",
            # "page_num": "2"
        }
        yield feapder.Request(url, params=params, method="GET")


    def download_midware(self, request):
        request.headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "cookie": "_zap=39f2a52b-bb47-4448-8cb5-6e0edf93768f; d_c0=AHBZEgLGBxePTv7Iou3TBv_P4rTmCrEN85E=|1688438659; q_c1=29a0cbf1555248baa74efbb094bc0889|1688444236000|1688444236000; _xsrf=l3LB6QHrrks8qzawnVShBqTZZ1EKpUW8; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1713882730,1713961801,1714745881,1714957473; z_c0=2|1:0|10:1714975961|4:z_c0|80:MS4xQjRkTkJ3QUFBQUFtQUFBQVlBSlZUZG5DSldkVG1sY3Q4QkJldEkwVFBZdGpUQ1gtdlZ3Vnd3PT0=|dac84543e85a4864f896241c6502fb0be9498d272b49bdcbda4a185ce43fd8e6; tst=r; SESSIONID=SbPLPnfaSUSM9AsOWm9wJr7xIkDr6YNheSd3X4uKVrl; JOID=W14TBEzGcRpByY-wQMjwjG3NR7ZYmhNLDZfu1iCbK0kN8MDMDzLYIynIgLFB8LXPA1C3qsGKYgH7XZeBsZ-w5fA=; osd=VFsdAULJdBREx4C1Ts3-g2jDQrhXnx1OA5jr2CWVJEwD9c7DCjzdLSbNjrRP_7DBBl64r8-PbA7-U5KPvpq-4P4=; BEC=43d4532fd57f0c3c659e43172114057d; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1715050760; KLBRSID=0a401b23e8a71b70de2f4b37f5b4e379|1715050762|1715047760",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.zhihu.com/people/nuo-ni-71-19",
            "sec-ch-ua": "Chromium;v=124, Microsoft",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "x-api-version": "3.0.40",
            "x-requested-with": "fetch",
            "x-zse-93": "101_3_3.0",
            "x-zse-96": "2.0_OpMFUPmU7SFJLM=ITGCknGvXhDRlcyIn7gOCMl2hhpakUhpvwHRwvCAj3oiKJdwK",
            "x-zst-81": "3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZKTY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPF4OydCSBDCS1oge9-go9vq3mOhg_8DLYuU3_8H28b7VYoXcMrLwfdG2BebcTvAx1k8tfAutKBv392L3OeMtKscS8fbN_3u2mIgOfGwFYDCe80CeVUG3O1q31JTXKeAes1cfMKvO8wC3GrXc1wucLButC-vCfwqNVDB3G-rNMavV_VGpsCqfzfTH06rHCr02MWUXKMiLqo6eYEDw8XhHMBCCfWqO_2QXxh9xYwvH8r7xM2vS96GVZUJN8eM7YQwO9NCoGFwL9wwxyr8C9gJe_FbH1SbS1WCVpCwXBwBHC"
        }
        response=requests.get(request.url)
        return request,response

    def parse(self, request, response):
        print(response.text)
        # print(response.status_code)
        # print(response.headers)


if __name__ == "__main__":
    AirSpiderDemo(thread_count=1).start()
