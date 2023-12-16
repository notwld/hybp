from flask import Flask, render_template, request, redirect, url_for
import requests
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


def login(username, password):
    req = requests.Session()
    with open("config/payload.json") as f:
        payload = json.load(f)
    url = "http://erp.uit.edu:803/StudentPortal/Student/EDU_EBS_STU_Login.aspx"
    payload["ctl00$ContentPlaceHolder1$txtRegistrationNo_cs"] = username
    payload["ctl00$ContentPlaceHolder1$txtPassword_m6cs"] = password
    req.post(url, data=payload)
    res = req.get(
        "http://erp.uit.edu:803/StudentPortal/Student/EDU_EBS_STU_Dashboard.aspx"
    )
    return res.text

