import socket

# =================================
IN_MAINTENANCE = False
# IN_MAINTENANCE = False
# =================================

print(" ++ Configuration Setting ++")
host_name = socket.gethostname()
IP_address = socket.gethostbyname(host_name)
# --- SYSTEM CONFIG --- #
SECRET_KEY = "@002342562988603673976#131452@HHPLHKHHH"
# HOST = host_name;


LOCAL_IP ="127.0.0.1"
HOST = "0.0.0.0";
PORT = 5000;
_PORT = 5000;
IS_DEBUG = True;

LOCAL_PORT=3306
# LOCAL_HOST = "0.0.0.0";
LOCAL_HOST = "localhost";
LOCAL_USER = "root";
LOCAL_PASSWORD = "";
LOCAL_DATABASE = "emrg";

# LOCAL_DATABASE = "dti_rapidxi";
IS_ON_SERVER = False;
DB_CRED = [];
JSON_PATH =None
# SERVER_PORT=3306;
# SERVER_HOST = "dtirapid.mysql.pythonanywhere-services.com";
# SERVER_USER = "dtirapid";
# SERVER_PASSWORD = "ruralagro";
# SERVER_DATABASE = "dtirapid$dti_rapidxi";


# ================================
global __STORE ;
__STORE = {} ;
# ================================
