# Batman
# Batman

This is fastapi project with integration of azure.

# About this Repo

This repo illustrates the basics of running a FastAPI application on Azure Functions.

Much of the code here has been borrowed/copied from:  https://github.com/tonybaloney/ants-azure-demos/tree/master/fastapi-functions

# To Deploy To Azure Functions

These steps assume that you are using the [Azure Functions VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions).

Step 1:  Create an [Azure Account](https://azure.microsoft.com/en-us/).

Step 2:  Install the [Azure Functions VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions).

Step 3:  Open your project in VSCode.  VSCode will automatically create a virtual environment for you and install all dependencies.

Step 4:  Run your Azure Function locally:

  * Just press F5!

Verify that your app is running by going to:  http://localhost:7071/user/1.  You should see a JSON response with some fake data.  For example:
    
    {
        "user_id":1,
        "username":"AdianaRestrict_1858",
        "firstname":"Beau",
        "lastname":"Lancaster"
    }

Step 5:  Deploy your function to Azure:

  * Open the VSCode Command Pallette.
  * Run "Azure Functions:  Deploy to Function App.
  * Follow the promps and wait a few minutes for everything to deploy.

Verify that your app is running by going to:  https://<APP_NAME>.azurewebsites.net/user/1.  You should see similar fake data as shown in Step 4.










Build container locally
docker build --tag sanjeettm/batmanazfuncimage:v1.0.0 .

Test container locally
docker run -p 8080:80 -it sanjeettm/batmanazfuncimage:v1.0.0

Push the image to docker hub
check available images
docker images

docker login
docker push sanjeettm/batmanazfuncimage:v1.0.0

if error try
docker login -u "myusername" -p "mypassword" docker.io
docker push myusername/myimage:0.0.1



Create Azure resources

create resource group
az group create --name AzureFunctionsContainers-batman-rg --location westeurope

az storage account create --name batman420storage --location westeurope --resource-group AzureFunctionsContainers-batman-rg --sku Standard_LRS

creat a premium plan
az functionapp plan create --resource-group AzureFunctionsContainers-batman-rg --name batmanmyPremiumPlan --location westeurope --number-of-workers 1 --sku EP1 --is-linux


create a function app
az functionapp create --name batman420azfun --storage-account batman420storage --resource-group AzureFunctionsContainers-batman-rg --plan batmanmyPremiumPlan --runtime python --deployment-container-image-name sanjeettm/batmanazfuncimage:v1.0.0

'''
az functionapp create --name alter-deployment-v1 --storage-account batman420storage --resource-group AzureFunctionsContainers-batman-rg --plan batmanmyPremiumPla--runtime python --functions-version 3

'''

display connection string
az storage account show-connection-string --resource-group AzureFunctionsContainers-batman-rg --name batman420storage --query connectionString --output tsv

DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=batman420storage;AccountKey=AmcenEX6/XCCKZL9rGNmsnJ0ejKqzvswaJkGe+I5SvB2mcbbTwMuHKuFoe0SXfVdRwu8zhUE15HpGa/pwQx/ng==

add setting to function app
az functionapp config appsettings set --name batman420azfun --resource-group AzureFunctionsContainers-batman-rg --settings AzureWebJobsStorage=DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=batman420storage;AccountKey=AmcenEX6/XCCKZL9rGNmsnJ0ejKqzvswaJkGe+I5SvB2mcbbTwMuHKuFoe0SXfVdRwu8zhUE15HpGa/pwQx/ng==


enable continuous deployment
az functionapp deployment container config --enable-cd --query CI_CD_URL --output tsv --name batman420azfun --resource-group AzureFunctionsContainers-batman-rg

https://$batman420azfun:xkBlzzx0gq3NMgPtP74PxYDtLkqvmYP4xMnpevGhE4tngip5edJ3QmTFKeh7@batman420azfun.scm.azurewebsites.net/docker/hook






























docker build --tag sanjeettm/batmanazfuncimage:v1.0.0 .

docker run -p 8080:80 sanjeettm/batmanazfuncimage:v1.0.0


http://localhost:8080/api/v1/home/

docker push sanjeettm/batmanazfuncimage:v1.0.0



docker tag local-image:tagname new-repo:tagname
docker push new-repo:tagname


modifying for tesing autobuild on docker hub