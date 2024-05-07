import requests


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "cookie": "uuid_tt_dd=10_19753268650-1688438740442-655390; UN=qq_51689012; UserName=qq_51689012; UserInfo=ef81e0e0e6924128a57ec5ef2258de3f; UserToken=ef81e0e0e6924128a57ec5ef2258de3f; UserNick=%E6%B3%95%E5%85%8B%E9%98%BF%E5%BA%93%E7%8E%9B; AU=B01; BT=1704195476063; p_uid=U010000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22qq_51689012%22%2C%22scope%22%3A1%7D%7D; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_19753268650-1688438740442-655390!5744*1*qq_51689012; c_segment=14; dc_sid=4dbd1c995c1db9db09e60fd2ff68f17f; firstDie=1; _gid=GA1.2.1311959157.1714957095; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1713881104,1713961563,1714529216,1714957099; _clck=1mv57vi%7C2%7Cflj%7C0%7C1542; _ga=GA1.2.1956091268.1708933466; _ga_7W1N0GEY1P=GS1.1.1714957095.48.1.1714959901.60.0.0; historyList-new=%5B%5D; cf_clearance=w4lFgq95H6IcXrImP5x.cL46RctWEINp4Zk1WqNRGl0-1714963855-1.0.1.1-pyo67EnBFupnp_9Zo20CCSh2njHJUmbYJPHXNhM8pjbS11M3nxcsT6llij.4j1HQptdoMabJtFJaaNo4SgG1DQ; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B13%2C%22%5B%5C%22DBABBg~BUoAAACA%5C%22%2C%5B%5B8%2C%5B1714963852%2C932099000%5D%5D%5D%5D%22%5D%5D%5D; FCNEC=%5B%5B%22AKsRol_9sUILLLg3Lbd0ZD79XzJp6MlIyZaNdBehe1O2XNwYkZGi7ebZfoilcrntd-3coDxgDLIfyb4tfITHwea8G81A3JhTeY89JCiA6LVAfiLp5-hDfCgAtmmoeImc2w9LsdOUDumJp8M1f3Bb1tWLh7Qk7fp7cQ%3D%3D%22%5D%5D; ssxmod_itna=iqmxgD2DcG0=FwDl8Gmtn0DjxQqDvN+ipddeD/FmDnqD=GFDK40ooBhND7mYnoWAMTqWxMCrrv=A/jOG3GE8YepUfb9Yx0aDbqGk1IGYdGGAxBYDQxAYDGDDPDogPD1D3qDkD7EZlMBsqDEDYp9DA3Di4D+8MQDmqG0DDtHB4G2D7tBnxDlngT1K7qRSAiPgRrMjmUtWexe8qDM0eGXWGF18TR8Xa5/WjcH5epuDB6+xBQljLNXjeDHGuXlKjvvY7DoBOeoWiptiBqqKi5pRIDnZ7qw8i+t8AxeYAhx4S46XH5DG4xzBxxxD; ssxmod_itna2=iqmxgD2DcG0=FwDl8Gmtn0DjxQqDvN+ipdeG9t=QYDBwArx7pxgaHGFiDGrKh0Fd1uCYLhi41mcxhrmKFtMYUtcfYMwiinSOiMjxerAZq6IkzUj9ITDKkHdDLxij14D=; tfstk=f3Vti4ciXMjiqX601P630MJqfZ7hE5Uw9lzWimmMhkELDkigjrsZcqEKxx2imftXMl4_SxfZcXtISquXCVNYLIUzu5bZiNla7jlfqgfoMPzZgaTC3aS3RZg2JapAI_4a7e9AOnS5ZKLQZM_xcoMsdvgqAVOs5otCODuqlhgX1wUIYqGXGAi_RvgqoKgXGXWMWmYsDIFnZh3YZOmwGINCgAn85KAXGW3tBSasvza79VHtVvmKRCV_xrNg_vW9Cjz3eoebVMvif838vY2O2CE8bqaxllCyyDNTkWHaKh9syfntF5M9raznhJFKs5s2Uy4KfYh3K9SinfETU0k1LMrYJcqb6vtOxm2u-5MLVMAL0xebsXN1A_Irl7VRq3-o2qv1Jwp23AgnbJgE2u-PwR3KqwvH3Kkn82nlJwp23AgEJ0bhtKJqK25..; c_dl_prid=1714226113092_902983; c_dl_rid=1714964120169_929370; c_dl_fref=https://blog.csdn.net/; c_dl_fpage=/; c_dl_um=distribute.pc_feed_blog_category.none-task-blog-classify_tag-1-138048939-null-null.nonecase; __gads=ID=3311a4b0d2dc9dbc-2283d2e381e20068:T=1688445470:RT=1714966771:S=ALNI_MaUPeJJPNPk6EHLJMByPJiWHvmvLQ; __gpi=UID=00000c9387c04b3c:T=1688445470:RT=1714966771:S=ALNI_MZ10XNpuly-Mhvg2E9qkqbQ7R90rA; __eoi=ID=f48fb3819f2a200c:T=1706629271:RT=1714966771:S=AA-AfjZ9_B3HfJ-YdkqcBa31MrDx; dc_session_id=10_1714978484312.517131; c_pref=default; c_first_ref=default; c_first_page=https%3A//blog.csdn.net/weixin_41793160; c_dsid=11_1714978484246.841602; c_page_id=default; creativeSetApiNew=%7B%22toolbarImg%22%3A%22https%3A//img-home.csdnimg.cn/images/20231011044944.png%22%2C%22publishSuccessImg%22%3A%22https%3A//img-home.csdnimg.cn/images/20240229024608.png%22%2C%22articleNum%22%3A0%2C%22type%22%3A0%2C%22oldUser%22%3Afalse%2C%22useSeven%22%3Atrue%2C%22oldFullVersion%22%3Afalse%2C%22userName%22%3A%22qq_51689012%22%7D; c_ref=https%3A//www.csdn.net/%3Fspm%3D1001.2101.3001.4476; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1714978486; fe_request_id=1714978485916_8144_3351581; log_Id_click=636; log_Id_pv=317; _clsk=dex6tt%7C1714978488306%7C1%7C0%7Ct.clarity.ms%2Fcollect; log_Id_view=2574; dc_tos=sd1xw5",
    "origin": "https://blog.csdn.net",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://blog.csdn.net/nav/back-end",
    "sec-ch-ua": "Chromium;v=124, Microsoft",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}
url = "https://cms-api.csdn.net/v1/web_home/select_content"
params = {
    "componentIds": "www-blog-recommend",
    "cate1": "back-end"
}
response = requests.get(url, headers=headers, params=params)

# print(response.text)
data=response.json()['data']["www-blog-recommend"]["info"]
items=[each["extend"]["url"] for each in data]
