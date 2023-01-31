import requests

url = "https://www.facebook.com/api/graphql/"

cookie = "cookie nick đi follow"
User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
# vào facebook mở console và dán code dưới để lấy fb_dtsg
# let dtsg = document.body.innerHTML.match(/"fb_dtsg","value":"([^"]+)"/)[0];
# console.log(dtsg);
fb_dtsg = "" 
subscribee_id = "id nick cần follow"
actor_id = "id nick đi follow"

headers = {
    "accept": "*/*",
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
    "variables": '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,","subscribe_location":"PROFILE","subscribee_id":'f"{subscribee_id}"',"actor_id":'f"{actor_id}"',"client_mutation_id":"5"},"scale":1.5}',
    "doc_id": "5032256523527306"
}
response = requests.post(url, headers=headers, data=data)
print(response.json()['data']['actor_subscribe']['subscribee']['following_status']['title']['text'])