# Team Rolex Big-Scale Analytics
## University of Lausanne, HEC
### Lingorank project by : **Estelle Valerie Tsague Mbialeu** & **Lirette Teiffouet Noumbo Epse Keumedjio**

### 

This repository includes content of our project which scope is to   ### Predict the difficulty of a french text.
To do so we've implement a flask interface to get user's input. This repository  provides the code used to achive this goal comprise the link to access to flask App.

## Our main folders:

* [Data](https://github.com/Rolex-Github/Team_Rolex_BigScale/tree/main/Data) : it holds usefull data to build the model with autoML
* [static](https://github.com/Rolex-Github/Team_Rolex_BigScale/tree/main/static)  : it contains the css files of our pages
* [templates](https://github.com/Rolex-Github/Team_Rolex_BigScale/tree/main/templates) : it contains the html code of our flask app  to get users' input and print the difficulty level 
* [Flask_app](https://github.com/Rolex-Github/Team_Rolex_BigScale/tree/main/Flask_app)  : it contains 4 files : the python code to run our application, the requirements.txt that holds the dependencies usefull to deploy the app , the app.yaml file to specify the app to deploy and finally a Dockerfile 
* [Notebook](https://github.com/Rolex-Github/Team_Rolex_BigScale/tree/main/Notebook) : it contains 3 Notebook ; 2 for the the milestone and 1 for the final project

## Final Deliverables:

1. Score for the metric :
     * accuracy :0.56
     * precision : 0.69
     * recall : 0.32
2. Url of our service deployed on APP ENGINE: https://french-text-difficulty-350020.lm.r.appspot.com/
3. Url of our dockerized application deployed on cloud run: https://predict-hfjvhfouoa-uc.a.run.app
4. Services used in our project:
     *  Cloud autoML API:  https://automl.googleapis.com 
     *  Cloud RUN service :
     *  Vertex AI API : https://us-central1-aiplatform.googleapis.com
5.  Tools: we've use 
     * Flask to build our web application
     * UI has been done from scracth (using html, css, javascript) without using any user framework
     * Docker has been use to containerize our application
     * Google App Engine to deploy the flask app on the web
     * Google cloud Run to deploy our dockerised flask application on the web
     * Google cloud storage to store the data imported from csv file
     * Google cloud automl to build our model and make prediction 
6.  [click here to wacth our youube video](https://www.youtube.com/watch?v=jZB6OaHvPEQ)
7.  [click here to wacth our youube video](https://youtu.be/cbpn4Eaki-E)



