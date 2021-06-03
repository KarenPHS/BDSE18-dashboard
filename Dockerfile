FROM python:3.7
RUN apt-get update
RUN apt-get install -y git
RUN git clone https://github.com/KarenPHS/BDSE18-dashboard.git
WORKDIR ./BDSE18-dashboard
RUN pip install -r requirements.txt && pip install pandas flask flask_sqlalchemy pymysql gunicorn
EXPOSE 5000
ENTRYPOINT ["gunicorn -w 1 -b 0.0.0.0:5000 router:app --daemon"]
