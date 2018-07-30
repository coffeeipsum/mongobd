# Mongo DB

$ bash command:
wget -q https://git.io/vFb1J -O /tmp/setupmongodb.sh && source /tmp/setupmongodb.sh


# Connecting to Mongo Shell:
mongo ds247141.mlab.com:47141/anniestestdb -u <dbuser> -p <dbpassword>

mongo ds247141.mlab.com:47141/anniestestdb -u root -p PASSWORD


# install dev package
sudo apt-get install build-essential space python-dev

# install py mongo
sudo pip3 install pymongo

# to connect to Mongo's URI (a.k.a. the connection string)
export MONGO_URI=mongodb://<dbuser>:<dbpassword>@ds247141.mlab.com:47141/anniestestdb
export MONGO_URI=mongodb://root:PASSWORD@ds247141.mlab.com:47141/anniestestdb

# to echo back the connection string:
echo $MONGO_URI


