# aws-cdk-demo
aws-cdk-demo


## Steps

Prepration:
```sh
npm install -g aws-cdk
pip install -r requirements.txt
```


# Build & Deploy
```
cdk bootstrap aws://MY_ACCOUNT_ID/us-east-1 --profile sam-admin
cdk synth --profile sam-admin
cdk deploy --profile sam-admin
```
