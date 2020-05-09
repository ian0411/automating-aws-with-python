# coding: utf-8
import json
event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-1:087725229265:handleLabelDetectionTopic:ff501176-c287-4e1c-8c34-4c8cd90068e5', 'Sns': {'Type': 'Notification', 'MessageId': '7359b4c9-5cee-5f0f-bd39-e3f942937a4d', 'TopicArn': 'arn:aws:sns:us-east-1:087725229265:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"f939688467d038124c3205ed52acf41882cd09cfbdf193e7d21b025c5e75e7af","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1588993085209,"Video":{"S3ObjectName":"video.mp4","S3Bucket":"ianvideolyzervideos"}}', 'Timestamp': '2020-05-09T02:58:05.328Z', 'SignatureVersion': '1',
                                                                                                                                                                                                            'Signature': 'GO8O0yJ47gfvnc7WcZTgBb+86cgSL3M3x4uXmNVG1nwtJyEEZsOIXzie/wVvdENIvZgHlD4W5FbpbLZkXxE8BhNvGUmwXi6OIdt1mfEeTEq+jBiR36bCCMxRizf27vr+XOleqFyEVf2KO2G3+UJLR7JZnvBDtstg99gfnpBI5Tp2ZJVGA3dOCJzjpRIrA9aiCu94RvsBks1m0tKsnCsELfjSSPzTDUpccz/uV3FnwVynE2FXkyJ7QdcVLpbVBYnmdrmEiEskJeP6YpCSzObk563GsxhN7qE9iQQclBONxHXiSoRS4sbvNLexowQ+5mDueuVI4XcZOqbVz/MYQPQ52A==', 'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-a86cb10b4e1f29c941702d737128f7b6.pem', 'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:087725229265:handleLabelDetectionTopic:ff501176-c287-4e1c-8c34-4c8cd90068e5', 'MessageAttributes': {}}}]}
event.keys()
event['Records'][0]
event['Records'][0].keys()
event['Records'][0]['EventSource']
event['Records'][0]['EventVersion']
event['Records'][0]['EventSubscriptionArn']
event['Records'][0]['Sns']
event['Records'][0]['Sns']['Message']
event['Records'][0]['Sns']['Message']['JobId']
type(event['Records'][0]['Sns']['Message'])
json.loads(event['Records'][0]['Sns']['Message'])
