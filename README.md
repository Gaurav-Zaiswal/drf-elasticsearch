1. Create virtual environment
2. install dependencies
3. start elasticsearch on your machine must be running on port 9200 (localhost:9200 or 127.0.0.1:9200). If you are running elasticsearch on any other port than 9200 then goto setting.py and update elasticsearch settings
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200' -> to your port number
    },
}
4. migrate 
5. run the project 
