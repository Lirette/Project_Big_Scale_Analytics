# Team Rolex

This repository includes content of our project which scope is to  " Predict the difficulty of a french text".
To do so we've implement a flask interface to get user's input. This repository  provides the code used to achive this goal comprise the link to access to flask App.

## Our main folders:

* [Data](https://github.com/Rolex-Github/Team_Rolex_BigScale/tree/main/Data) : it holds usefull data to build the modelwith autoML
* [static](https://github.com/Rolex-Github/Team_Rolex_BigScale/tree/main/static)  : it contains the css files of our pages
* [templates](https://github.com/Rolex-Github/Team_Rolex_BigScale/tree/main/templates) : it contains the html code of our flask app  to get users' input and print the difficulty level 
* [Flask_app](https://github.com/Rolex-Github/Team_Rolex_BigScale/tree/main/Flask_app)  : it contains 3 files : the python code to run our application, the requirements.txt that holds the dependencies usefull to deploy the app and finally the app.yaml file to specify the app to deploy
* [Notebook](https://github.com/Rolex-Github/Team_Rolex_BigScale/tree/main/Notebook) : it contains 3 Notebook ; 2 for the the milestone and 1 for the final project

## Final Deliverables:

1. Score for the metric and test data prepared by your TAs.
2. Url of our main service : https://french-text-difficulty-350020.lm.r.appspot.com
3.  Endpoints of all the services used in our project  :
        - Cloud autoML API:  https://automl.googleapis.com 
        - Vertex AI API : https://us-central1-aiplatform.googleapis.com
4.  Tools: we've use 
        - Flask to build our web application
        - UI has been done from scracth without using any user framework
        - Docker has been use to containerize our application
        - google cloud storage to store the data, google cloud automl to build our model and make prediction
5.  [click here to wacth our youube video](https://www.youtube.com/watch?v=jZB6OaHvPEQ)



