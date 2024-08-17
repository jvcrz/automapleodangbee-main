import requests
from PIL import Image
import numpy as np
import json
import cv2

def main():
    print("Hello, World!")
    
    myimg=None
    image_path = 'rune.png'
    try:
        with Image.open(image_path) as img:
            # Display the image
            # img.show()
            myimg=img.copy()
            
            # Print basic info about the image
            print(f"Image format: {img.format}")
            print(f"Image size: {img.size}")
            print(f"Image mode: {img.mode}")
    except FileNotFoundError:
        print(f"File {image_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


    # cv2.imshow('img',myimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    img = np.array(myimg)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    sendjson = {
        'image': img.tolist()
    }
    # link = 'http://'+self.ipaddress+':8001/'
    link = 'http://'+'127.0.0.1'+':8001/'
    link = link + 'predict'
    r = requests.post(url=link, json=sendjson)
    json_data = json.loads(r.text)
    print(json_data['prediction'])
    sms = json_data['prediction']
    # print(f"{sms}")
    for i in range(len(sms)):
        print(sms[i:i+1])
    
    # # Make a simple GET request to a URL
    # response = requests.get('https://api.github.com')    
    # # Print the status code of the response
    print("Status Code:", r.status_code)    
    # Print the content of the response
    print("Response Content:", r.json())

if __name__ == "__main__":
    main()
