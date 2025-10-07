FROM apache/superset:latest

# Install extra drivers (Snowflake + Synapse)
USER root
RUN pip install \
    snowflake-sqlalchemy \
    pyodbc \
    sqlalchemy-azure-synapse \
    azure-identity

# Copy Superset config
COPY config/superset_config.py /app/pythonpath/superset_config.py

USER superset
EXPOSE 8088
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8088", "superset.app:create_app()"]