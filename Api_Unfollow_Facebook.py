import requests

url = "https://www.facebook.com/api/graphql/"

cookie = "cookie nick đi hủy follow"
User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70"
# vào facebook mở console và dán code dưới để lấy fb_dtsg
# let dtsg = document.body.innerHTML.match(/"fb_dtsg","value":"([^"]+)"/)[0];
# console.log(dtsg);
fb_dtsg = ""
unsubscribee_id = "id nick cần hủy follow"
actor_id = "id nick đi hủy follow"


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
    "variables": '{"action_render_location":"WWW_COMET_FRIEND_MENU","input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,","subscribe_location":"PROFILE","unsubscribee_id":'f"{unsubscribee_id}"',"actor_id":'f"{actor_id}"',"client_mutation_id":"5"},"scale":1.5}',
    "doc_id": "7083037361770482"
}

response = requests.post(url, headers=headers, data=data)
print("Đã hủy "+response.json()['data']['actor_unsubscribe']['unsubscribee']['profile_action']['title']['text'])
