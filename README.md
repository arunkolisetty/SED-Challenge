---
maintainer: ArunK
---

# SED-Challenge setup


## Preparations
### AWS account 
If you don't have account, you may get a free AWS account. In the setup will be used free t2.micro instances. 
#### SSH keys
Before to start, create ssh keys. Terraform will create key-pair in AWS, based on these keys. See [how to create ssh keys](https://confluence.atlassian.com/bitbucketserver/creating-ssh-keys-776639788.html)
Create a pem file with private ssh key you generated. Terraform will need to the pem file to connect to instances for provisioning.
#### Update the project file with new information
There are three file need your credentials for successing run up. First of all, update *key-pair.tf* set there a path to the public ssh key, generated earlier. In *variables.tf* update your AWS account information. In *app-instances.tf* update connection block for each resources, set there the path to ssh private key.    

## How to use
After all configuration files are ready, you can do check if there are no mistakes.
```
terraform plan
```
This command will show either syntax errors or list of resources will be created. After you can run:
```
terraform apply
```
This command will build and run all resources in the *.tf files. If you run this command many times, Terraform will destroy previous instances before creating new ones. 
That is it. Now you have fully functioned docker swarm cluster in AWS.

If you want to terminate instances and destroy the configuration you may call:
```
terraform destroy
```
