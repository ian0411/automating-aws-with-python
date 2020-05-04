# coding: utf-8

import boto3

session = boto3.Session(profile_name='Ian-pfb')
as_client = session.client('autoscaling')
as_client.execute_policy(
    AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Up')
