#AUTHOR: VŨ VĂN HẢI
import requests
import json
import base64

url = "https://www.facebook.com/api/graphql/"
reactions = {
    "LIKE": 1635855486666999,
    "LOVE": 1678524932434102,
    "CARE": 613557422527858,
    "HAHA": 115940658764963,
    "WOW": 478547315650144,
    "SAD": 908563459236466,
    "ANGRY": 444813342392137,
}
def encode_to_base64(string):
    string_bytes = string.encode("utf-8")
    base64_string = base64.b64encode(string_bytes)
    return base64_string.decode("utf-8")

cookie = "cookie nick thả cảm xúc"
User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70"
# vào facebook mở console và dán code dưới để lấy fb_dtsg
# let dtsg = document.body.innerHTML.match(/"fb_dtsg","value":"([^"]+)"/)[0];
# console.log(dtsg);
fb_dtsg = ""
reaction_id = reactions.get('LOVE')
actor_id = "id nick thả cảm xúc"
#thay 3295710027338600 bằng id bài viết bạn muốn thả cảm xúc
id_bai_viet = "feedback:"+"3295710027338600"
feedback_id = encode_to_base64(id_bai_viet)

headers = {
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.facebook.com",
    "sec-fetch-dest": "empty",
    "ec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": f"{cookie}",
    "User-Agent": f"{User_Agent}",
}

data = {
    "fb_dtsg": f"{fb_dtsg}",
    "variables": '{"input":{"feedback_id":"'f"{feedback_id}"'","feedback_reaction_id":'f"{reaction_id}"',"actor_id":'f"{actor_id}"',"client_mutation_id":"18"},"useDefaultActor":false,"scale":1.5}',
    "doc_id": "5703418209680126",
}

response = requests.post(url, headers=headers, data=data)
if "errors" not in response.json():
    print("success")
else:
    print("fail")
