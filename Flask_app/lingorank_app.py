from flask import Flask,render_template,flash, request, url_for
from google.cloud import automl
from google.api_core.client_options import ClientOptions
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/estellev_mbialeu/hello/french-text-difficulty-350020-42d146608f7d.json"
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('home.HTML')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        text = request.form.get("targetfrase")
        project_id = "french-text-difficulty-350020"
        model_id = "TCN228192643228631040"
        content = text
        options = ClientOptions(api_endpoint='eu-automl.googleapis.com')
        prediction_client = automl.PredictionServiceClient.from_service_account_json("french-text-difficulty-350020-42d146608f7d.json", client_options=options)
        model_full_id = automl.AutoMlClient.model_path(project_id,'eu',model_id)
        text_snippet = automl.TextSnippet(content=content,mime_type='text/')
        payload = automl.ExamplePayload(text_snippet=text_snippet)
        response = prediction_client.predict(name=model_full_id, payload=payload)
        return render_template("result.HTML", data=response.payload, result=text)
    if request.method == 'GET':
        return "<h3> nothing to show </h3>"
if __name__ == '__main__':
    #app.run(debug=True, host="127.0.0.1", port=5001)
    #app.run()
    #app.run(debug=True, host="0.0.0.0", port=5000)
    app.run(port=int(os.environ.get("PORT",8080)),host='0.0.0.0',debug=True)
