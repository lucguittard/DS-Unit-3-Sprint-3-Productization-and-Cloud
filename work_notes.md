# Module 1 - work-related update

The material covered today dealt with web-apps, terminology and initial steps to setting them up. 
    - The front-end may be distinguished from the back-end as the former (the web-client) has to do with the user interface and the latter (the web-server, associated applications and databases all of which lie behind a firewall) has primarily to do with the infrastructure that supports that user interface.

    - A distinction may be made between databases and servers. The former is where data is collected, stored, and managed in a formulated way; the latter is that network of computers that manage the storage system.

    - The setup of an app involves a few initial steps:
        1)  pipenv install Flask (while outside of the pipenv shell)
        2)  import flask (while in python)
        3)  initiate flask using the following command: FLASK_APP=hello.py flask run
    
    - To introduce additional features:
        1)  pipenv install flask_sqlalchemy
        2)  make a new directory NEW within TwitOff to hold application specific files (__init__.py, app.py, models.py, and any desired templetes files)
        3)  models.py should contain DB = SQLAlchemy()
        4)  FLASK_APP=NEW:APP flask shell
        5)  from APP.models import *
        6)  DB.create_all()
        7)  ls NEW/ 

    - I will save review of this process for tomorrow's as I am convinced the lecture will consist of such a review.

Link to TwitOff project repo: https://github.com/lucguittard/TwitOff


# Module 2 - work-related update

The material covered today dealt with implementing APIs in Flask apps. Not much new terminology or concepts were introduced. 

Embedding is one new concept and it may be thought of as encoding. What it involves is taking in textual data and converting to numeric form, as this is the only form of data that computers can work with. 

Another concept introduced involved making a framework for a relational database. To do this, introduce user_id=DB.Columns() and user=DB.relationship() into the models.py file. 

Overall, I managed to follow along with much of what was covered in class. Where I fell behind was in using the Twitter API keys, as I was awaiting approval of my Developer status. I did revisit the lecture after its recording was posted and was able to replicate all the code. 
When I got started on the assignment, I decided to first delve into the additional resources. I checked out one of the previous lecture videos and followed along for the most part on the subject on applied embedding via the Basilica API. Where I encountered errors was for the most part where there were differences in the names of my files,classes, and functions compared to the names used in class and in the videos. I feel that, to reduce confusion in the future, there can be made a better distinction between the tweet variable and Tweets class in particular.  


# Module 3 - progress update

The materials of today dealt mainly with building off of the framework established the previous day, with the prime goal being to have code and files in place to support interaction with the back-end data via the Flask app. What remains to be covered as regards full interactivivity is how to pull/reference data via the app. The daily assignment I feel is appropriate, if I understand it correctly. It is to comprehend the lecture material of which there is lot of code to mull over. Also included in the assignment, is the task of adding features to the app webpage via html; this I found to be a nice change of pace. Also disclosed today were the project topics for this upcomming Build Week - another welcomed distraction. I will be spending the remainder of the day reviewing the code from today and attending TL hours for perhaps better insight into the material. 


# Module 4 - progress update 

We finished the underlying code for the app today and I can run it in flask, taking two users and comparing the likelihood that they will tweet a given phrase. Issues were encountered the moment I tried to git push to heroku. I feel these can be resolved later on, so I spent the remainder of the time practicing taking in API links, converting to json, and showing this data in flask, all in a simple .py file. This is a straight-forward process I find. I encounter trouble when adding features to the app.py file that would manipulate the data and return visual representations in flask. For example, I tried to export a plot (created in the code of the .py file
to flask and it breaks down when I try to access the webpage. More practice is needed on building upon the basics. 