# AWS Infra for Lambda Delete Unused Keys Function
Labmda templates and source code to disable and delete any AWS access keys not used in the last 90 days. 

## Prerequisites

* [Docker](https://docs.docker.com/get-docker/)
* [AWS Serverless Appication Model CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

You will need to change the AWS account number to match your AWS account number in the template.yaml file. AWS account number set to 012345678912 as a placeholder. 


## How It Works

1. In the src/ directory there is the source code for the AWS Lambda Function. 
2. The template.yaml file in the root directory contains the AWS CloudFormation configuration for the infra of the function. 
3. The samconfig.toml file in the root directory contains the deployment configuration. Such as the name of the CloudFormation stack, the name of the s3 bucket to deploy the lambda function package, which region to deploy to, and whether to confirm the changeset before deploying. 

## Setup
From the root directory run to setup the role and s3 for the lambda.
```sh
$ /bin/bash infra_init.sh
```

## Usage

1. Build the lambda package locally: 
   ```sh
   $ sam build 
   ```

2. (Optional) Test locally:
   ```sh
   $ sam local invoke
   ```

3. Deploy package: 
   ```sh
   $ sam deploy
   ```
