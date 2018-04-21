import requests

# 第一步 从红颜平台获取验证码
response = requests.get("https://api.cuewbs.cn/ali/get.php", params={
    "token": "FFFF00000000017AB4A1",  # 阿里云Token
    "scene": "othrt",  # 阿里云场景
    "accesskey": "MXYTKXDKLO"  # 你的AccessKey
}).json()
print(response)
csessionid = response["data"]["csessionid"]
sig = response["data"]["sig"]
token = response["data"]["token"]

# 第2步 发送
data = {
    "email": "1843630466@qq.com",
    "operationType": "25",
    "afs_token": "",
    "afs_scene": "register",
    "csessionid": csessionid,
    "sig": sig,
    "token": token,
    "scene": "other",

}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "referer": "https://www.coineal.com/mregister-email.html?inviteCode=EAWAW%23%23",
    "x-requested-with": "XMLHttpRequest"
}
response = requests.post("https://www.coineal.com/emailValidCode.html", data=data, headers=headers).text
print(response)