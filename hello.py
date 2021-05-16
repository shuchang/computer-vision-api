import boto3

client = boto3.client('rekognition')

response = client.detect_labels(
    Image={
        'S3Object': {
            'Bucket': 'learn-computer-vision-api',
            'Name': 'flowers.JPG',
            },
        },
    )

print(response)