from elasticsearch import Elasticsearch

# instantiate Elasticsearch
# make sure elasticsearch is up and running on localhost:9200
es = Elasticsearch("http://127.0.0.1:9200")

# test if the connection is successfull
# if returns True -> connection established successfully
print(es.ping())  
# es.indices.create(index='test-index', ignore=400)

