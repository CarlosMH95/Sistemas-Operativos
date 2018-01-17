#import sys
#import os
#sys.path.append(os.path.join(os.path.dirname(__file__), 'microservice'))
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'microservice.settings')

#from django.conf.urls import include, url
#from django.conf.urls.static import static
#from django.conf import settings
#from api.views import home, justdatabase, sendNews
import grpc
from concurrent import futures
import time
import requests
import json
import microservice_pb2
import microservice_pb2_grpc
import memcache
import pymysql.cursors
from datetime import datetime

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

mc = memcache.Client(['127.0.0.1:11211'], debug=0)
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='Aisakataiga1',
                            db='newsfeed',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

class Microservice(microservice_pb2_grpc.MicroserviceServicer):
    def ListNews(self, request, context):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `news` ORDER BY `numero_accessos`  DESC LIMIT %s"
                cursor.execute(sql, (10,))
                result = cursor.fetchall()
                resultjson = json.dumps(result)
                resjson = json.loads(resultjson)
                for news in resjson:
                    yield microservice_pb2.News(id=news['id'],title=news['title'],
                                        url=news['url'],publisher=news['publisher'],
                                        category=news['category'],story=news['story'],
                                        hostname=news['hostname'],time_stamp=news['time_stamp'],
                                        numero_accessos=news['numero_accessos'])
        finally:
            print("DONE :3")


def serve():
    server =grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    microservice_pb2_grpc.add_MicroserviceServicer_to_server(Microservice(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
