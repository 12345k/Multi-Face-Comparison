# Two-Face-Comparison

Compare two images and it will return True or False. This is the main focus of this repo. I have attached two py file.
Oneis compare_image.py this can be run in the terminal with two images name like
> desktop-su-02@Desktop-SU-02:~/Documents/face-recongition-master$ python compare_image.py image_1.jpg image_2.jpg 

Another File is Compare_api.py. This file is api which can be attached to website or other apps

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
> desktop-su-02@Desktop-SU-02:~/Documents/face-recongition-master$ python compare_image.py  ami.jpg AMI.jpg  
> 0.5439451765528829
> True
```
## Output for compare_api.py

Output will be in  json format. Addition I have calculate time take to predict

###### Example

```
{
    "result": "True",
    "distance": 0.46566292058258163,
    "time_taken": "0.6611621379852295"
}
```
I have used postman to check the api. The url mostly will be like http://127.0.0.1:5000/upload in POST format.
### form-data key name will be img_1 and img_2 in Postman

Links for other resources

https://face-recognition.readthedocs.io/en/latest/installation.html


