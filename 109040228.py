import json

j = 0
with open("drugstore.json", encoding = "utf-8") as store:
    data = json.load(store)

    for i in data:
        if i["機構狀態"] == "開業" and i["地址縣市別"] == "新北市":
            j += 1
            if 11 <= j and j <= 20:
                print(i["機構名稱"])
                print(i["地址縣市別"]+i["地址鄉鎮市區"]+i["地址街道巷弄號"], "\n")

