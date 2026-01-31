# Lab 1 - Dockerised Model Training 
In this lab, a RandomForest Model is trained on the load_diabetes dataset, makes predictions and deployed using Docker containerization. 
The purpose of this lab was to practice basic Docker operations like creation of image, building a container, exporting the image and running it on a local machine. 

## Build Docker Image 
Run inside, MLOps_Labs/Lab1_docker
```
docker build -t mlops_lab1:v1 . 
```

## Run the Container 
```
docker run mlops_lab1:v1
```

## Export the Image 
```
docker save mlops_lab1:v1 ? mlops_lab1.tar 
```


