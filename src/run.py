#!/usr/bin/env python3

import os
import requests
import json
import re

def send_http_req(feedback_entry, url):
    response = requests.post(url, data=feedback_entry)
    if response.ok:
        print("success")
    else:
        #print("request: " + str(response.request))
        print("request: " + str(response.request.body))
        print("response: " + str(response))
        #print("feedback_entry: " + feedback_entry)

def construct_dict(file_path):
    feedback = {}
    with open(file_path, 'r') as file_obj:
        for idx, line in enumerate(file_obj):
            if idx == 0:
                feedback["name"] = line.strip()
            elif idx == 1:
                feedback["weight"] = re.sub(r'\s*[a-zA-Z]', '', line.strip())
            elif idx == 2:
                feedback["description"] = line.strip()
        feedback["image_name"] = os.path.basename(file_path).replace(".txt", ".jpeg")
    return feedback

def dict_to_json(dict):
    return json.dumps(dict)

def process_files(folder_path):
    for data_file_name in os.listdir(folder_path):
         data = construct_dict(os.path.join(folder_path, data_file_name))
         send_http_req(dict_to_json(data), "http://localhost/")

if __name__ == '__main__':
    process_files('../data/supplier-data/descriptions/')
