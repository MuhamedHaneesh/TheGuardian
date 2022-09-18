
Guardian Scrapper

The project is created by following the official scrapy webbsite.

https://docs.scrapy.org/en/latest/topics/commands.html?highlight=startproject#startproject


A Perfect scrapper to crawl the contents from TheGuardian newspaper and store it into the Cloud.MongoDB

Usage.

Here I have already provided/hardcoded my cloud.mongo DB account and the database, collection name in the settings file. Once it starts to crawl the data, it will automatically create
the DB , collection with the name I mentioned here in settings.py

Install using pip

pip install -r requirements.txt

Run the application

scrapy crawl TheGuardian

Stored data details

Here I have tested two links and both are working using this crawler application.

The two links are : https://www.theguardian.com/world/all
                    https://www.theguardian.com/international


I am commented one url in TheguardianSpider and using one for this. if need to test, uncomment it and pls try


Note : Here I have used the HTTPCACHE_ENABLED = True in settings.py and it's saving to a directory as well. Before I crawling the content from the site I am checking
       it's already scrapped or not. so the same url won't scrap again and will help us to remove the duplicates as well.



API details

To get the saved data in various ways (number of records with collection details, filter the documents through headline/content/author) from cloud.mongo DB, create API.
 Run this API by using the below command.


env FLASK_APP=server.py flask run    -- This will run the application in localhost address

To view the data in a beautiful structure and easy to pass parameters, recommending to use the postman tool (chrome extension)

The sample screen shots are attached in email.













