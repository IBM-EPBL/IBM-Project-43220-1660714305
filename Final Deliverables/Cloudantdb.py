from cloudant.client import Cloudant

#Authenticate using an IAM API key
client = Cloudant.iam('55a4f815-9a4a-4711-b663-d2733b89f3f9-bluemix', 'Ga7SGlD639xERt-F6egdft3j2dNntgT5CelqppKEgSLp', connect = True)

# Create a database using an initialized client
my_database = client.create_database('ibm-deeplearning')