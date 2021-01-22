from flask import Flask
from processing import do_calculation

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def adder_page():
    return '''
        <html>
            <body>
                <p>Enter your serial number:</p>
                <form>
                    <p><input name="number1" /></p>
                    <p><input name="number2" /></p>
                    <p><input type="submit" value="Do your thing" /></p>
                </form>
            </body>
        </html>
    '''
