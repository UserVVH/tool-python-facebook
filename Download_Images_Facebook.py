import requests
import os

access_token = "token nick facebook"
user_id = "id nick cần lấy ảnh"

headers = {
    "Authorization": f"Bearer {access_token}",
    "content-type": "application/json; charset=UTF-8",
    "cookie": "cookie nick facebook",

}

url = f"https://graph.facebook.com/{user_id}/feed?fields=full_picture&access_token={access_token}"
nameFB = requests.get(f"https://graph.facebook.com/{user_id}?fields=name&access_token={access_token}", headers=headers)
nameFolder = nameFB.json()["name"]
if not os.path.exists(nameFolder):
    os.makedirs(nameFolder)

response = requests.get(url, headers=headers)
count = 0
while url:
    response = requests.get(url, headers=headers)
    for i in response.json()["data"]:
        try:
            img_url = i["full_picture"]
            img_data = requests.get(img_url).content
            print("Downloading: " + i["id"])
            with open(nameFolder + '/' + i["id"] + '.jpg', 'wb') as vvh:
                count+=1
                vvh.write(img_data)
        except:
            pass
    if "paging" not in response.json():
        print("Done")
        print("Number of images: " + str(count))
        break
    if "next" in response.json()["paging"]:
        url = response.json()["paging"]["next"]

