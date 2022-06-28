# Basic searching with Elasticsearch and DRF
This project is to demostrate how **Elasticsearch** can be integrated with **Django Rest Framework** to provide searching feature.

## Set up instruction
This project uses `Elasticsearch v7.16` as the backend search engine and `Django v4.0` as the backend framework. You can set up the project on your local environment in following steps:
### Part A: Project set up
1. **Setup Elasticsearch**
[Setup](https://www.elastic.co/downloads/past-releases/elasticsearch-7-16-2) and [run](https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-windows.html#windows-running) Elasticsearch v7.16.X on your local machine. Make sure Elasticsearch==7.X.X,<8.X.X is installed and running locally before proceeding to the next step
2. **Create and activate virtual environment**
3. **Install the dependencies**
4. **Run Elasticsearch**
Make sure Elasticsearch is running on port 9200 (localhost:9200 or 127.0.0.1:9200). If you are running elasticsearch on any other port than 9200 then goto **elasticsearch_project/setting.py** and update elasticsearch configurations
    ```
    ELASTICSEARCH_DSL = {
        'default': {
            'hosts': 'localhost/<port-number>'
        },
    }
    ```
5. **Run migrations** 
You may also need to populate the database, so that searching can be done.
6. **Run the project**
If any error is encountered at the time of running the project then make sure above steps have been followed correctly.

### Part B: Creating Index
Once part A is successfully executed, you can go ahead and create the index. Make sure elasticsearch is running on localhost on the same port as specified in the settings.py file. Run `python manage.py search_index --rebuild`  to create the index.

## Test
Once the server and elasticsearch is up and running, you can test the APIs as -
* To list all existing classrooms: [http://127.0.0.1:8000/classroom/](http://127.0.0.1:8000/classroom/)
* To search of a clssroom: `127.0.0.1:8000/classroom/<your-query-text>`
⋅⋅⋅For example, to search **python** classroom: `http://127.0.0.1:8000/classroom/python/`