import os
from flask_appbuilder.security.manager import AUTH_DB

# Authentication type (DB or OAuth)
AUTH_TYPE = AUTH_DB
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Gamma"

# Connection strings (from Railway environment variables)
SQLALCHEMY_DATABASE_URI = os.getenv("SUPERSET_DB_URI", "sqlite:////app/superset_home/superset.db")

# Snowflake connection
SNOWFLAKE_CONN_URI = os.getenv("SNOWFLAKE_CONN_URI")

# Synapse connection (optional)
SYNAPSE_CONN_URI = os.getenv("SYNAPSE_CONN_URI")

ENABLE_PROXY_FIX = True
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "yoursecretkeyhere")
