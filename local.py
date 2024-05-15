from flask import Flask, render_template, redirect, flash, url_for
import Configurations as c
from flask_cors import CORS,cross_origin

def _init_config_():
	c._SERVER_PORT = c.LOCAL_PORT
	c._HOST = c.LOCAL_HOST
	c._USER = c.LOCAL_USER
	c._PASSWORD = c.LOCAL_PASSWORD
	c._DATABASE = c.LOCAL_DATABASE
	c.DB_CRED = [c.LOCAL_HOST,c.LOCAL_USER,c.LOCAL_PASSWORD,c.LOCAL_DATABASE] # DEV
	c.PORT = 80
	c.IS_ON_SERVER = False
	c.IP_address = c.LOCAL_IP
	c.JSON_PATH = "assets/response/"
	c.LOGIN_PATH = "assets/login/"

# ===========================================================================
print(" * LOCAL Launch")
_init_config_()
import bp_app as bp
_init_config_()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.register_blueprint(bp.app);

@app.route("/")
def index():
	return redirect("/home")
	

if __name__ == "__main__":	
		app.run(debug=True,host="0.0.0.0")

