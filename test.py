import requests

url = "https://taplio.com/api/search"

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://taplio.com",
    "referer": "https://taplio.com/find-viral-linkedin-posts",
    "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}

cookies = {
    "_ga": "GA1.1.1013414746.1746099592",
    "rl_anonymous_id": "RS_ENC_v3_IjQ5YjMwYjQzLTJlNzQtNDJkOS1iMmZmLTc2YWVmN2M3NTNlOSI%3D",
    "rl_page_init_referrer": "RS_ENC_v3_Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIg%3D%3D",
    "rl_page_init_referring_domain": "RS_ENC_v3_Ind3dy5nb29nbGUuY29tIg%3D%3D",
    "intercom-id-nlu9qthh": "20411dae-e4bd-4d09-9faa-6853880f85fb",
    "intercom-device-id-nlu9qthh": "accbe3c1-5dc4-4495-9ea7-9e75e51de055",
    "mf_user": "e74e71e4c38997fb0224a725cd2ff64a|",
    "mf_e1d2c821-5584-46bf-887d-6290af76285a": "af9c5afb97ee7a2146d94da6de11f06c|05020453432cbfc3dfc520126a7bcc2111f73bc1.1455327696.1746187984154$05024678ab7c32e7cd53b0ce6cc099a92f4e941c.2600906565.1746188026580$05020085b4a2022444bc55fdae0c474e5cb7a7c0.2600906565.1746188040889$0502354750c7d03b85f0964fa258bd1512f4a7fb.-131358213.1746188075750$050236811f620610ec370de0361538c676af4ff6.2600906565.1746188076182$05025729341325f632e4f14d97f1290c5601fa49.46411358.1746188157832|1746189724759||9||||0|18.29|43.34557",
    "AMP_MKTG_bf7de8e37d": "JTdCJTdE",
    "_clck": "13sr6kj%7C2%7Cfvn%7C0%7C1947",
    "rewardful.referral": '{"id":"29edb132-dcb3-453f-8a1a-9044224c67c4","created_at":"2025-05-05T08:53:05.739Z","affiliate":{"id":"11bf74f8-e830-4fcc-8cf2-2eae6793ea88","name":"Diem Dinhh","first_name":"Diem","last_name":"Dinhh","token":"diem"},"campaign":{"id":"9d1bef86-f03f-4bf8-b7b9-bc284823f5ee","name":"Taplio Creators"},"coupon":null,"cookie":{"domain":"taplio.com"}}',
    "_gcl_aw": "GCL.1746438308.Cj0KCQjww-HABhCGARIsALLO6XwvZvsDYMXJ8T3yLRQ0iO5nn9jumfCudRTDIS4dG3QgVyX0C1PlVCcaAsQoEALw_wcB",
    "_gcl_gs": "2.1.k1$i1746438304$u213062289",
    "_gcl_au": "1.1.1546814397.1746099592.618778448.1746439687.1746439689",
    "rl_session": "RS_ENC_v3_eyJpZCI6MTc0NjQzNTE4NTIxNCwiZXhwaXJlc0F0IjoxNzQ2NDQxODIyMjIzLCJ0aW1lb3V0IjoxODAwMDAwLCJhdXRvVHJhY2siOnRydWUsInNlc3Npb25TdGFydCI6ZmFsc2V9",
    "_clsk": "gn682o%7C1746440022696%7C12%7C1%7Ck.clarity.ms%2Fcollect",
    "AMP_bf7de8e37d": 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJhYWY3MDU1My1kZjlhLTRjMmItOWVkZi0wNjM3ZTg5YTE2ODAlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJhdXRoMCU3QzhkZGRlN2QzLTEyZGItNDcxOS04MjY3LWM0ZDcwMmQwMjIyMyUyMiUyQyUyMnNlc3Npb25JZCUyMiUzQTE3NDY0Mzc3NDE1NTAlMkMlMjJvcHRPdXQlMjIlM0FmYWxzZSUyQyUyMmxhc3RFdmVudFRpbWUlMjIlM0ExNzQ2NDQxMTMyMzk1JTJDJTIybGFzdEV2ZW50SWQlMjIlM0E1NCUyQyUyMnBhZ2VDb3VudGVyJTIyJTNBMTMlN0Q=",
    "_ga_8NMHVEJP2M": "GS1.1.1746432936.6.1.1746441133.50.0.0",
    "intercom-session-nlu9qthh": "K3I3QUU2T2RZSzlDYktBMWNtekFYeGNDVUJYOCtWZGdudjU1ZzhablE1NlQ3WWhtcGM1NVd1TXZUZjBlNDA3NFJuaWsyTWFxMURoaXpsWU0wdU1wbGt0a2NKM09HUTlmTkRjNEdHTVdZMk09LS0yTG9EL1Vzd3B6bzZyRFhUdU5NOGZBPT0=--6269d8b249855a127afaa4a59b27d02cf02df164",
    "_ga_KK3KJVRHMT": "GS2.1.s1746441250$o2$g0$t1746441250$j0$l0$h0"
}

data = {
    "keyword": "Artificial Intelligence",
    "isPersonalized": False,
    "about": "",
    "description": ""
}

response = requests.post(url, headers=headers, cookies=cookies, json=data)

print("Status code:", response.status_code)
print("Response body:", response.text)