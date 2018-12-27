# -*- coding: utf-8 -*-
import xml.dom.minidom
import io
import sys
#用于解决print乱码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

doc = xml.dom.minidom.Document()
desc = 'This xml document was a parameter of project Interface_MQ_Python, dont edit any paremeter node\'s name and node\'s location ,thanks a lot. '
root = doc.createElement('Parameter_Producer')
root.setAttribute('Author','Edmond Chen')
root.setAttribute('Description',desc)
root.setAttribute('Alarm','DO NOT USE ANY CHINESE CHARACTERS AS DB_NAME OR MQ_NAME !!!')
doc.appendChild(root)
DB_PARA =[
        {'DB_IP':'XXX.XXX.XXX.XXX','DB_PORT':1521,'DB_USER':'XXXXXXXX','DB_PASWD':'000000000','DB_SRVNAME':'XXXXXXXX'}
        ]
MQ_PARA =[
        {'MQ_IP':'XXX.XXX.XXX.XXX','MQ_PORT':15672,'MQ_USER':'XXXXXXXX','MQ_PASWD':'000000000','MQ_EXCHANGE':'XXXXXXXX','MQ_HB':60,'MQ_ROUTER_KEY':'interface.mq'}
        ]
for i in DB_PARA:
    nodeDB_P = doc.createElement('DB_PARA')
    nodeDB_IP = doc.createElement('DB_PORT')
    nodeDB_PORT = doc.createElement('DB_PORT')
    nodeDB_USER = doc.createElement('DB_USER')
    nodeDB_PASWD = doc.createElement('DB_PASWD')
    nodeDB_SRVNAME = doc.createElement('DB_SRVNAME')
    nodeDB_IP.appendChild(doc.createTextNode(str(i['DB_IP'])))
    nodeDB_PORT.appendChild(doc.createTextNode(str(i['DB_PORT'])))
    nodeDB_USER.appendChild(doc.createTextNode(str(i['DB_USER'])))
    nodeDB_PASWD.appendChild(doc.createTextNode(str(i['DB_PASWD'])))
    nodeDB_SRVNAME.appendChild(doc.createTextNode(str(i['DB_SRVNAME'])))
    nodeDB_P.appendChild(nodeDB_IP)
    nodeDB_P.appendChild(nodeDB_PORT)
    nodeDB_P.appendChild(nodeDB_USER)
    nodeDB_P.appendChild(nodeDB_PASWD)
    nodeDB_P.appendChild(nodeDB_SRVNAME)
    root.appendChild(nodeDB_P)
for i in MQ_PARA:
    nodeMQ_P = doc.createElement('MQ_PARA')
    nodeMQ_IP = doc.createElement('MQ_PORT')
    nodeMQ_PORT = doc.createElement('MQ_PORT')
    nodeMQ_USER = doc.createElement('MQ_USER')
    nodeMQ_PASWD = doc.createElement('MQ_PASWD')
    nodeMQ_EXCHANGE = doc.createElement('MQ_EXCHANGE')
    nodeMQ_HB = doc.createElement('MQ_HB')
    nodeMQ_ROUTER_KEY = doc.createElement('MQ_ROUTER_KEY')
    nodeMQ_IP.appendChild(doc.createTextNode(str(i['MQ_IP'])))
    nodeMQ_PORT.appendChild(doc.createTextNode(str(i['MQ_PORT'])))
    nodeMQ_USER.appendChild(doc.createTextNode(str(i['MQ_USER'])))
    nodeMQ_PASWD.appendChild(doc.createTextNode(str(i['MQ_PASWD'])))
    nodeMQ_EXCHANGE.appendChild(doc.createTextNode(str(i['MQ_EXCHANGE'])))
    nodeMQ_ROUTER_KEY.appendChild(doc.createTextNode(str(i['MQ_ROUTER_KEY'])))
    nodeMQ_HB.appendChild(doc.createTextNode(str(i['MQ_HB'])))
    nodeMQ_P.appendChild(nodeMQ_IP)
    nodeMQ_P.appendChild(nodeMQ_PORT)
    nodeMQ_P.appendChild(nodeMQ_USER)
    nodeMQ_P.appendChild(nodeMQ_PASWD)
    nodeMQ_P.appendChild(nodeMQ_EXCHANGE)
    nodeMQ_P.appendChild(nodeMQ_HB)
    nodeMQ_P.appendChild(nodeMQ_ROUTER_KEY)
    root.appendChild(nodeMQ_P)
output = open('C:\\Users\\Administrator\\Documents\\GitHub\\MicroESB_by_mq_python\\data_interface\\db.parameter','w')
doc.writexml(output,indent='\t',addindent='\t',newl='\n',encoding='utf-8')
