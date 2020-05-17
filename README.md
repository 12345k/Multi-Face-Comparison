# Two-Face-Comparison

Compare two images and it will return True or False. This is the main focus of this repo. I have attached two py file.
One is compare_image.py this can be run in the terminal with two images name like

> karthick_aravindan@ml-machine:~/Documents/Two-Face-Comparison$ python compare_image.py image_1.jpg image_2.jpg 

Another File is app.py. This file is api which can be attached to website or other apps. In this we compare multiple faces with one target image.

## Requirment

```
pip install face_recognition
pip install flask
pip install scipy
```

## Output for compare_image.py 

Distance and Boolean value. Distance is higher means it is false and lower is True

###### Example
```
> karthick_aravindan@ml-machine:~/Documents/Two-Face-Comparison$ python compare_image.py  ami.jpg AMI.jpg  
> 0.5439451765528829
> True
```
## Output for API app.py

Output will be in  json format. Addition I have calculate time take to predict

###### Example

```
[
    {
        "result": "True",
        "distance": 0.0,
        "time_taken": "0.3203427791595459",
        "target": "rajini.jpeg",
        "face": "rajini.jpeg"
    },
    {
        "result": "False",
        "distance": 0.7720132497612807,
        "time_taken": "0.311934232711792",
        "target": "rajini.jpeg",
        "face": "kamal.jpg"
    }
]    
```
I have used postman to check the api. The url mostly will be like http://localhost:8000/upload in POST format.
### form-data key name will be target and faces in Postman

![request](https://github.com/12345k/Multi-Face-Comparison/blob/master/images/postman.png) 

Links for other resources

https://face-recognition.readthedocs.io/en/latest/installation.html


