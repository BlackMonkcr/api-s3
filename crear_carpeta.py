import boto3

def lambda_handler(event, context):
    # Entrada: nombre del bucket y nombre de la carpeta
    bucket_name = event['body']['bucket_name']
    folder_name = event['body']['folder_name']
    
    # Validación de entrada
    if not bucket_name or not folder_name:
        return {
            'statusCode': 400,
            'message': 'bucket_name y folder_name son requeridos'
        }
    
    # Proceso
    s3 = boto3.client('s3')
    response = s3.put_object(Bucket=bucket_name, Key=(folder_name + '/'))

    # Salida
    return {
        'statusCode': 200,
        'message': f'Carpeta {folder_name} creada en el bucket {bucket_name}'
    }
