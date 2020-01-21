# aws-image-moderation
 
* Launch the cloudformation (cf.yaml)
* Create two S3 bucket : UNIQUE_NAME_images, UNIQUE_NAME_web
  * Make both of buckets public
  * Paste the CORS configuration for UNIQUE_NAME_images
  * Upload all the file in the resource folder (drag and drop) and enable public access
* Create Lambda 
  * Copy and paste the code from lambda_function.py (python 3.7)
  * Add policy for S3, DynamoDB and Rekognition
* Create Cognito (+add policy for S3)



## CORS configuration
```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>HEAD</AllowedMethod>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedMethod>DELETE</AllowedMethod>
    <ExposeHeader>x-amz-server-side-encryption</ExposeHeader>
    <ExposeHeader>x-amz-request-id</ExposeHeader>
    <ExposeHeader>x-amz-id-2</ExposeHeader>
    <AllowedHeader>*</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```
