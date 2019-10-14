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
