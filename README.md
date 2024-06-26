# Steps :
1. Run Airflow using `docker-compose up`
2. Create Plugins:
    - Finnhub loader
    - MongoDB loader
    - Sentiment Analysis
    - Postgres loader
3. Create python code to extract from Finnhub and load to MongoDB
4. Create Python code that Get data from MongoDB and do Sentiment Analysis then load the result to Postgres
5. Create Python Environment `python -m venv env`
6. Activate `env/Scripts/activate`
7. Run `pip install -r requirements.txt`
8. Run `python finhub_mongodb_loader.py`
9. Run `pip install psycopg2-binary`
10. Run `python sentiment_analysis_loader.py`
11. Create Database `Enter docker desktop -> postgres image -> terminal -> psql -Uairflow -> create database data_warehouse; -> \du -> \l ` or `docker exec it <postgres images id> bash -> psql -Uairflow -> create database data_warehouse; -> \du -> \l` 
12. Check the newly entered database `\c data_warehouse -> \d -> select * from sentiment_news_analysis limit 20;`

# Ouput
1. Output finnhub_mongodb_loader.py
![Alt text](Screenshot%20Output/Output%20finnhub_mongodb_loader.png)
2. Output sentiment_analysis_loader.py
![Alt text](Screenshot%20Output/Output%20sentiment_analysis_loader.png)
3. Output Image Postgres
![Alt text](Screenshot%20Output/Output%20Image%20Postgres.png)
4. Output Atlas MongoDB
![Alt text](Screenshot%20Output/Output%20Atlas%20MongoDB.png)
5. Output DBeaver
![Alt text](Screenshot%20Output/Koneksi%20DBeaver.png)