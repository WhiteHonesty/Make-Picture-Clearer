import base64
import requests
import streamlit as st
import json
import time

st.set_page_config(page_title="基于Streamlit的图像综合增强器", layout="wide")

def baidu_tupian_duibidu_zengqiang(target):
    # client_id为从官网获取的AK， client_secret为从官网获取的SK
    client_id = "yZCjtfAuBRkQGwctFzNZ2Dy5"
    client_secret = "jivcc3ZbI5dvHjW3SY6r6ZxNGIH6Hs7w"

    token_url = "https://aip.baidubce.com/oauth/2.0/token"
    host = f"{token_url}?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"

    response = requests.get(host)
    access_token = response.json().get("access_token")

    request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/contrast_enhance"
    image = base64.b64encode(target.read())

    body = {
        "image": image,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    request_url = f"{request_url}?access_token={access_token}"
    response = requests.post(request_url, headers=headers, data=body)
    content = response.content.decode("UTF-8")

    picture =  open("enhanced_picture.png", "wb")
    picture.write(base64.b64decode(json.loads(content)["image"]))

def baidu_tupian_secai_zengqiang(target):
    client_id = "yZCjtfAuBRkQGwctFzNZ2Dy5"
    client_secret = "jivcc3ZbI5dvHjW3SY6r6ZxNGIH6Hs7w"

    token_url = "https://aip.baidubce.com/oauth/2.0/token"
    host = f"{token_url}?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"

    response = requests.get(host)
    access_token = "24.3cbc3c51638046d08fbb791ffd4afd17.2592000.1684468294.282335-32579897"
    #response.json().get("access_token")
    print(access_token)
    print("1")

    request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/color_enhance"
    image = base64.b64encode(target.read())

    body = {
        "image": image,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    request_url = f"{request_url}?access_token={access_token}"
    response = requests.post(request_url, headers=headers, data=body)
    content = response.content.decode("UTF-8")

    picture =  open("enhanced_picture.png", "wb")
    print(type(list(json.loads(content).keys())[0]))
    print("2")
    picture.write(base64.b64decode(json.loads(content)["image"]))


def baidu_tuxiang_qingxidu_zengqiang(target):
    client_id = "yZCjtfAuBRkQGwctFzNZ2Dy5"
    client_secret = "jivcc3ZbI5dvHjW3SY6r6ZxNGIH6Hs7w"

    token_url = "https://aip.baidubce.com/oauth/2.0/token"
    host = f"{token_url}?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"

    response = requests.get(host)
    access_token = response.json().get("access_token")

    request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/image_definition_enhance"
    image = base64.b64encode(target.read())

    body = {
        "image": image,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    request_url = f"{request_url}?access_token={access_token}"
    response = requests.post(request_url, headers=headers, data=body)
    content = response.content.decode("UTF-8")

    picture =  open("enhanced_picture.png", "wb")
    print(list(json.loads(content).keys()))
    print(json.loads(content).get('image'))
    print(3)
    picture.write(base64.b64decode(json.loads(content).get('image')))

    c1, c2 = st.columns(2)
    with c1:
        st.image(file, caption="增强前", use_column_width="always")
    with c2:
        st.image("enhanced_picture.png", caption="增强后", use_column_width="always")

st.sidebar.title("图像增强")
file = st.sidebar.file_uploader("请上传要进行综合增强的图片", type=["jpg", "png", "jpeg", "png"])

if file is not None:
    baidu_tupian_duibidu_zengqiang(file)
    time.sleep(1)
    with open("enhanced_picture.png", "rb") as picture:
        baidu_tupian_secai_zengqiang(picture)
        time.sleep(1)
    with open("enhanced_picture.png", "rb") as picture2:
        baidu_tuxiang_qingxidu_zengqiang(picture2)