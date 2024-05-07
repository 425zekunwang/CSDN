import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "uuid_tt_dd=10_19752565560-1714957620820-495310; c_first_ref=default; c_segment=14; hide_login=1; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1714957622; dc_sid=6bccaadb50d2f07268f63292fd3d0815; _clck=1w7g4dn%7C2%7Cflj%7C0%7C1587; csrfToken=sdrDCdKdEJy3KAySkUtkxNV3; creative_btn_mp=3; __gads=ID=82b05343bd4c3b4f:T=1714958866:RT=1714958866:S=ALNI_MbhTWnK-5FhCstwdK56bXJAEjwn4A; __gpi=UID=00000e0d6ecfe6ab:T=1714958866:RT=1714958866:S=ALNI_Ma4hpOBhSOqo546YrrkaiCRmCx4CA; __eoi=ID=01bf9e072789f0be:T=1714958866:RT=1714958866:S=AA-AfjaZFUZO5pb35dpjctqR6Twh; loginbox_strategy=%7B%22taskId%22%3A349%2C%22abCheckTime%22%3A1714957621651%2C%22version%22%3A%22exp11%22%2C%22blog-threeH-dialog-exp11tipShowTimes%22%3A5%2C%22blog-threeH-dialog-exp11%22%3A1714957621651%7D; popPageViewTimes=5; cf_clearance=q4.YFzerbbs1fiJrWPbSUZfhgGhIu3WzMuhnc69vEuM-1714958914-1.0.1.1-oUxMM7E0LKgZa7.Kv82uOJJ_lu06Y7mv7Qs_7MTVoQ7f5ONtP1k1_8kZdtVxJKq_vmxpmI97.o2QAzOOtLqYKg; FCNEC=%5B%5B%22AKsRol-W76UE_qbNNN9QMgxITdhhIaDZVBM5b4h4rLdEzH0veISU1O_N7fQ-VZSLCvWSYTnYLVCg-CbCibd7TvhlIcSTz7v94tabssK9wP7d592DLvB6uvdyVIKCjPVrpWlBBIW53GjnZuXCN7TJw-YZLXolUTtsdA%3D%3D%22%5D%5D; dc_session_id=10_1714966107297.217137; SESSION=7519234c-38f6-488b-ba56-23517f52adc0; UserName=2401_84388637; UserInfo=2016029168c74f73a8ce1d1bbc9635cf; UserToken=2016029168c74f73a8ce1d1bbc9635cf; UserNick=2401_84388637; AU=BD8; UN=2401_84388637; BT=1714966234234; p_uid=U110000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%222401_84388637%22%2C%22scope%22%3A1%7D%7D; c_utm_source=zhuzhantoolbar; utm_source=zhuzhantoolbar; dp_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTUwMjQ1MiwiZXhwIjoxNzE1NTcxMjYzLCJpYXQiOjE3MTQ5NjY0NjMsInVzZXJuYW1lIjoiMjQwMV84NDM4ODYzNyJ9.pXO235SAM4qIO5kST_Eh3_joW_rR0V4YinlUjTW2Zk8; firstDie=1; dc_tos=sd1on3; relevant_index=1; creativeSetApiNew=%7B%22toolbarImg%22%3A%22https%3A//img-home.csdnimg.cn/images/20231011044944.png%22%2C%22publishSuccessImg%22%3A%22https%3A//img-home.csdnimg.cn/images/20240229024608.png%22%2C%22articleNum%22%3A0%2C%22type%22%3A0%2C%22oldUser%22%3Afalse%2C%22useSeven%22%3Atrue%2C%22oldFullVersion%22%3Afalse%2C%22userName%22%3A%222401_84388637%22%7D; referrer_search=1714966553562; SidecHatdocDescBoxNum=true; fe_request_id=1714966650955_3044_5397811; c_utm_relevant_index=5; log_Id_click=37; c_pref=default; c_ref=default; c_first_page=https%3A//blog.csdn.net/DeepLies/article/details/82143988%3Fops_request_misc%3D%25257B%252522request%25255Fid%252522%25253A%252522171496676816800188524052%252522%25252C%252522scm%252522%25253A%25252220140713.130102334.pc%25255Fblog.%252522%25257D%26request_id%3D171496676816800188524052%26biz_id%3D0%26utm_medium%3Ddistribute.pc_search_result.none-task-blog-2%7Eblog%7Efirst_rank_ecpm_v1%7Erank_v31_ecpm-1-82143988-null-null.nonecase%26utm_term%3Dcsdn%25E6%2596%2587%25E7%25AB%25A0%25E6%2589%25B9%25E9%2587%258F%25E4%25B8%258B%25E8%25BD%25BD%25E5%2599%25A8%26spm%3D1018.2226.3001.4450; c_dsid=11_1714966777068.393820; c_utm_medium=distribute.pc_search_result.none-task-blog-2%7Eblog%7Efirst_rank_ecpm_v1%7Erank_v31_ecpm-1-82143988-null-null.nonecase; c_utm_term=csdn%E6%96%87%E7%AB%A0%E6%89%B9%E9%87%8F%E4%B8%8B%E8%BD%BD%E5%99%A8; c_page_id=default; log_Id_pv=31; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1714966777; _clsk=1dt3o2k%7C1714966777778%7C9%7C0%7Ct.clarity.ms%2Fcollect; log_Id_view=1587; waf_captcha_marker=b0847068578d9c2e9be6c6e2ce21fe13f3a627c6bd3086f6ffa2965da59b9a32; dc_tos=sd1oub",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    "sec-ch-ua": "Chromium;v=124, Microsoft",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows"
}
url = "https://blog.csdn.net/DeepLies/article/details/82143988"
params = {
    "ops_request_misc": "%257B%2522request%255Fid%2522%253A%2522171496676816800188524052%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D",
    "request_id": "171496676816800188524052",
    "biz_id": "0",
    "utm_medium": "distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-82143988-null-null.nonecase",
    "utm_term": "csdn%E6%96%87%E7%AB%A0%E6%89%B9%E9%87%8F%E4%B8%8B%E8%BD%BD%E5%99%A8",
    "spm": "1018.2226.3001.4450"
}
response = requests.get(url, headers=headers, params=params)

print(response.status_code)
with open("./csdn_vip.html","w",encoding="utf-8") as f:
    f.write(response.text)


    # 点赞，评论量，评论数量，收藏量