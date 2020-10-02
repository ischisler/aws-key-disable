from datetime import datetime, timezone

import boto3
from botocore.exceptions import ClientError

MAX_AGE = 90

iam = boto3.client('iam')

def days_old(last_used): 
    now = datetime.now(timezone.utc)
    age = now - last_used

    return age.days

def lambda_handler(event, context): 
    print('Hello World')
    paginator = iam.get_paginator('list_users')

    for response in paginator.paginate(): 
        for user in response['Users']: 
            print(user['UserName'])
            username = user['UserName']
            res = iam.list_access_keys(UserName=username)
            print(res)

            for access_key in res['AccessKeyMetadata']: 
                access_key_id = access_key['AccessKeyId']
                last_used_date = iam.get_access_key_last_used(AccessKeyId=access_key_id)

                age = days_old(last_used_date['AccessKeyLastUsed']['LastUsedDate'])
                print('Last used date: ', age)

                if age < MAX_AGE:
                    continue
                else: 
                    print('Key not in use', access_key)
                    print('Deleting....')
                    iam.update_access_key(
                        UserName=username,
                        AccessKeyId=access_key_id,
                        Status='Inactive')

                    iam.delete_access_key(
                        UserName=username,
                        AccessKeyId=access_key_id)


