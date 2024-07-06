import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Entrada: nombre del bucket
    bucket_name = event['body']['bucket_name']
    
    # Validación de entrada
    if not bucket_name:
        return {
            'statusCode': 400,
            'message': 'bucket_name es requerido'
        }
    
    # Proceso
    s3 = boto3.client('s3')
    try:
        response = s3.create_bucket(Bucket=bucket_name)
        message = f'Bucket {bucket_name} creado exitosamente'
    except ClientError as e:
        message = e.response['Error']['Message']
        return {
            'statusCode': 500,
            'message': message
        }

    # Salida
    return {
        'statusCode': 200,
        'message': message
    }
