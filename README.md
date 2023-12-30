## ImageIdentify

Simple Python CLI application using vit-base-patch16-224 to perform image classification. 

Run instructions:

```
cd app
docker build -t image_identify .
docker run -dp 8000:8000 image_identify
```
From there, port 8000 listens for GET requests. Example request:
```
curl -X GET "http://localhost:8000?jpg_url=test_image.jpg"
```
