# Multi-Face-Comparison

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
# Run
```
> karthick_aravindan@ml-machine:~/Two-Face-Comparison$ python app.py
```
Flask api will be hosted 8000 port
### Endpoints
- /api/v1/compare_faces 
- /api/v1/detect_faces


## Output for compare_image.py 

Distance and Boolean value. Distance is higher means it is false and lower is True

###### command line output 
```
> karthick_aravindan@ml-machine:~/Two-Face-Comparison$ python compare_image.py  ami.jpg AMI.jpg  
> 0.5439451765528829
> True
```
## Output for compare face API 

Output will be in  json format. Addition I have calculate time take to predict

###### Example

```
[
    {
        "result": "True",
        "distance": 0.0,
        "time_taken": 0.29,
        "target": "rajini.jpeg",
        "face": "rajini.jpeg"
    },
    {
        "result": "False",
        "distance": 0.77,
        "time_taken": 0.339,
        "target": "rajini.jpeg",
        "face": "kamal.jpg"
    }
]    
```
I have used postman to check the api. The url mostly will be like http://localhost:8000/compare_faces in POST format.
#### form-data key name will be target and faces in Postman

![request](https://github.com/12345k/Multi-Face-Comparison/blob/master/screenshot/compare_faces.png)



## Detect Faces API

It will returns list of face coordinates for the images. 

#### Example

```
[
    {
        "coordinates": [
            {
                "ymin": 46,
                "xmin": 175,
                "ymax": 136,
                "xmax": 86
            }
        ],
        "time_taken": 0.046,
        "image_name": "kamal.jpg"
    },
    {
        "coordinates": [
            {
                "ymin": 32,
                "xmin": 101,
                "ymax": 84,
                "xmax": 49
            }
        ],
        "time_taken": 0.016,
        "image_name": "harry.jpg"
    }
]
```
![request](https://github.com/12345k/Multi-Face-Comparison/blob/master/screenshot/detect_faces.png)


###### command line output 
```
> karthick_aravindan@ml-machine:~/Two-Face-Comparison$ python detect_face.py image_path/ami.jpg
> Coordinates:  [(53, 114, 115, 52)]
```

Links for other resources

https://face-recognition.readthedocs.io/en/latest/installation.html


