# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: register.py
@time: 2024/2/25 21:21
@desc:

"""
import requests

cookie = "pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_693fff2719a04827bcd9b89d6823ab2f|1708612073193; __jdu=1196808241; areaId=1; ipLoc-djd=1-2901-0-0; PCSYCityID=CN_110000_110100_0; shshshfpa=e2e20aee-c0dc-2ec1-1b71-1bd093b94c57-1708612074; shshshfpx=e2e20aee-c0dc-2ec1-1b71-1bd093b94c57-1708612074; mba_muid=1196808241; TrackerID=yFMGhvwHM7yjCIAt_55NoXs8SfnzkKLYigg_nwgLKKfdS2kSBsrtiKiZawMDYqzUxw7k6pKk3SMHKLhOKECjIXp688P1L51Zxp7r4lWnr2A; pt_key=AAJl11ovADAoP_fzHYf9ptbm0rfzbpXs6TX2YJOtL7MKppbaFxH-mpMzRz-DkjjuxgNYkEHCxn0; pt_pin=jd_kcXPzeDWNMsE; pt_token=hwn1okwz; pwdt_id=jd_kcXPzeDWNMsE; sfstoken=tk01medda1d69a8sMysyKzNKeXp6OfycMRuKhN9KF0NySxpocQjplhDU7a/0qAq0VqY3ki9qvmks1fEmpcGqDjASj1r1; TrackID=1befmoIHGM0oV1PqFPCYnt45bo_B-AYMvBU-4fXJwWDVS7WI0XtOGp4EDQkhP3xgs2HLApVHtAxeRKryQPShkju-6EnossNYAiZjZ5K5uTAc; thor=41172D78D002F4B61AE3A45008C009FBB6A6E8C5BCA69A1060446BF635D1B6029770987F9BFC63789A1D19D079CE05B3DB2BDB97E85A62AAE04FBF673DB5F69C2D7E26E1A2F696EAE58275891C0D398554AC8A67AB98E6AA23F3C4B2A975F3E6BB6D9BA390F021C573D49FC8F4C0B35E17B95D288B6C3BCD83F6DAD91ADB36B417564D52731C6DD316C9C19322A343D36CB0C53915E3DEB23AEBD1BBF6B4AFE5; flash=2_Qpr1ohwgyEadMaMRPqKF2npLB2mh8aEL6Dfbjj-EXVmKNWcZB2nbFkZsPlKdgCMa9woc27KvRnbM77fS5ihKOxgCJ5SufuU9A1gFkJ0VdkD*; pinId=i10KvcpL-p6U_Aku7EcoJbV9-x-f3wj7; pin=jd_4f775868cad90; unick=jd_188458kec; _tp=rSLkx6RIb7hSOoFlTxZfDPA7HT3OCjuwgGmxxeEFAtk%3D; _pst=jd_4f775868cad90; 3AB9D23F7A4B3CSS=jdd03I4BIZKBQ23NQSWBRAKAQDZF6UF66KKWCTXFK4OHBMJ2VIGVSREY35VGKV4KPKT43DHRYJ5JHHP3YL6KADIDPOVDCPMAAAAMN2E4RUFQAAAAACECAKOW5F37FIYX; shshshfpb=BApXet2Uz0uhAFKT-MpvAdam4cqcof_2NBkogJ1ti9xJ1PdZfQo3VqirxiQ_NHatgVj9hAaTn; unpl=JF8EAIZnNSttCx8EVhMAHxsYG1hWWwoNTx8LOjAGBFpZGFUNHAEcFhd7XlVdWBRKFB9sYhRUXlNIUA4bBisSEHtdVV9eDkIQAmthNWRVUCVXSBtsGHwQBhAZbl4IexcCX2cFXFpRSl0GHgIrEyBLW2RubQl7FjNuV046XBVLVA0cCxobE05dZF9tCw; __jda=238604254.1196808241.1708612072.1708612073.1708748719.2; __jdb=238604254.1.1196808241|2.1708748719; __jdc=238604254; 3AB9D23F7A4B3C9B=I4BIZKBQ23NQSWBRAKAQDZF6UF66KKWCTXFK4OHBMJ2VIGVSREY35VGKV4KPKT43DHRYJ5JHHP3YL6KADIDPOVDCPM"

url = ("https://api.m.jd.com/client.action?functionId=signBeanAct&body=%7B%22fp%22%3A%22-1%22%2C%22shshshfp%22%3A%22-1"
       "%22%2C%22shshshfpa%22%3A%22-1%22%2C%22referUrl%22%3A%22-1%22%2C%22userAgent%22%3A%22-1%22%2C%22jda%22%3A%22-1"
       "%22%2C%22rnVersion%22%3A%223.9%22%7D&appid=ld&client=apple&clientVersion=10.0.4&networkType=wifi&osVersion=14"
       ".8.1&uuid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&openudid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&jsonp"
       "=jsonp_1645885800574_58482")

headers = {"Connection": 'keep-alive',
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Cache-Control": 'no-cache',
           "User-Agent": "okhttp/3.12.1;jdmall;android;version/10.3.4;build/92451;",
           "accept": "*/*",
           "connection": "Keep-Alive",
           "Accept-Encoding": "gzip,deflate",
           "Cookie": cookie
           }

response = requests.post(url=url, headers=headers)
print(response.text)