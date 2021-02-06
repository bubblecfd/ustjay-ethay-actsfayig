import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    page = """
    <html><br>
    <body><br>
    <a href="{url}">{url}<a><br>
    </body><br>
    </html>
    """
        
    fact = get_fact().strip()
    #print(fact)
    response = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/",
                             data={'input_text':fact})
    #print(response.headers)
    #print(response.status_code)
    #print(response.url)
    body = page.format(url=response.url)
    
    return Response(response=body, mimetype='text/html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

