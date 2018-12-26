__author__ = 'DozingWolf'
from basic_consumer_database_option import *
from basic_consumer_mq_option import *
from basic_tool import *
import json
import io
import sys
import _pickle as cPickle
#用于解决print乱码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# MQ parameter
mq_ip = '10.62.24.70'
mq_user = 'admin'
mq_password = 'admin@123'
mq_exchange = 'TEST_EXCHANGE_TOPIC'
mq_routing_ket = 'interface.001'
# DB parameter
db_ip = '10.62.24.24'
db_port = 1521
db_sid = 'orcl12c'
db_user = 'MQ_IN'
db_password = 'MQ_IN'
