# Copyright: 北京物元数界科技有限公司
# Author: 邵芒
# Contact: 微信 stormx

import json
from pdb import set_trace as stop

from tornado.escape import json_decode
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler


class CustomHandler(RequestHandler):

    # def get_argument(self, id: str):
    #     if self.request.headers['Content-Type'] == 'application/json':
    #         args = json_decode(self.request.body)
    #         return args[id]
    #     return super(CustomHandler, self).get_argument(id)

    def get_argument_dict(self):
        params = self.request.arguments
        for k, v in params.items():
            params[k] = v[0].decode("utf-8")
        return params

class Http():
    def __init__(self, config: dict, srv_name: str) -> None:
        self.config = config
        self.srv_name = srv_name
        self.srv = None

        # print('sqlite:///{0}/dm.db'.format(self.config["WORKDIR"]))
        # engine = create_engine('sqlite:///{0}/dm.db'.format(self.config["WORKDIR"]))
        # Entry.__table__.create(engine, checkfirst=True)
        # self.sql = sessionmaker(bind=engine)()

    def Build(self):
        self.appList = [
            # ('/{0}/models'.format(self.srv_name), ModelProc, dict(sql=self.sql)),
            # ('/{0}/models/(.*)'.format(self.srv_name),
            #  ModelProcID, dict(sql=self.sql)),
            # ('/{0}/models_exist/(.*)'.format(self.srv_name),
            #  ModelExist, dict(sql=self.sql)),
            # ('/{0}/property/(.*)'.format(self.srv_name),
            #  Property, dict(srv=self.srv)),
            
            ('/{0}/([a-zA-Z0-9_]+)'.format(self.srv_name),
             Action, dict(srv=self.srv)),
            
            # ('/{0}/event/(.*)'.format(self.srv_name), Event, dict(srv=self.srv)),
            # ('/{0}/mqtt/(.*)'.format(self.srv_name), MqttOp, dict(srv=self.srv)),
            # ('/{0}/devices'.format(self.srv_name),
            #  DevProc, dict(sql=self.sql, srv=self.srv)),
            # ('/{0}/devices/(.*)'.format(self.srv_name),
            #  DevProcID, dict(sql=self.sql, srv=self.srv)),
            # ('/{0}/file_upload'.format(self.srv_name),
            #  FileUploader, dict(srv=self.srv)),
            # ('/{0}/file_download'.format(self.srv_name),
            #  FileDownloader, dict(srv=self.srv)),
            # ('/{0}/file_remove'.format(self.srv_name),
            #  FileRemover, dict(srv=self.srv)),
            # ('/{0}/(.*)'.format(self.srv_name),
            #  ServiceProc, dict(srv=self.srv)),
        ]
        if self.config['PORT'] < 65535:
            self.httpApp = Application(self.appList)
            self.httpServer = HTTPServer(self.httpApp)
            self.httpServer.bind(self.config['PORT'])
            if 'HTTP_THREAD' in self.config:
                self.httpServer.start(self.config['HTTP_THREAD'])
            else:
                self.httpServer.start(1)
            
            
        # 0.1.20 MQTT support
        topic = '/{0}/+'.format(self.srv_name)
        self.mqtt = self.srv.mqtt
        self.mqtt.subscribe(topic)
        def callback (client, userdata, msg):
            try:
                topic = msg.topic
                payload = msg.payload.decode('utf-8')
                # check response
                # print("MQTT callback: {0}".format(topic))
                func_name = topic.split('/')[2]
                res = self.selector(func_name, payload)
                # Check responseTopic exists
                if hasattr(msg, 'properties') and hasattr(msg.properties, 'ResponseTopic'):
                    # print("MQTT respond: {0}".format(msg.properties.ResponseTopic))
                    self.mqtt.publish(msg.properties.ResponseTopic, json.dumps(res))
            except Exception as e:
                print(e)
        self.mqtt.message_callback_add(topic, callback)

    def Run(self):
        IOLoop.current().start()
            
    def selector(self, func_name: str, content=None):
        if (content == None or content == {} or content == ""):
            return getattr(self.srv.app, func_name)()
        else:
            if isinstance(content, str):
                return getattr(self.srv.app, func_name)(**(json.loads(content)))
            elif isinstance(content, dict):
                try:
                    return getattr(self.srv.app, func_name)(**content)
                except:
                    return getattr(self.srv.app, func_name)(content)
            else:
                # self.app.alarmer.alarm(Err.SRV_REQ_INVALID, 1,
                #                    "f:%{0} - {1}".format(func_name, content))
                return "Content type is not supported"

# class ServiceProc(CustomHandler):
#     def initialize(self, srv):
#         self.srv = srv

#     def get(self, func_name: str):
#         self.write(json.dumps(self.srv.Execute(func_name), ensure_ascii=False))
#         self.set_status(200)

#     def post(self, func_name: str):
#         content = self.get_argument('content')
#         self.write(json.dumps(self.srv.Execute(
#             func_name, content), ensure_ascii=False))
#         self.set_status(200)


# class FileUploader(CustomHandler):
#     def initialize(self, srv):
#         self.srv = srv

#     def post(self):
#         self.srv.app.upload(self.request)
#         self.set_status(200)


# class FileDownloader(CustomHandler):
#     def initialize(self, srv):
#         self.srv = srv

#     def post(self):
#         dataset = self.get_argument('dataset')
#         file_id = self.get_argument('file_id')
#         block = self.get_argument('block')
#         type = self.get_argument('type')
#         data = self.srv.app.download(file_id, dataset, block, type)
#         self.write(data)
#         self.set_status(200)


# class FileRemover(CustomHandler):
#     def initialize(self, srv):
#         self.srv = srv

#     def post(self):
#         dataset = self.get_argument('dataset')
#         file_id = self.get_argument('file_id')
#         block = self.get_argument('block')
#         type = self.get_argument('type')
#         self.srv.app.remove(file_id, dataset, block, type)
#         self.set_status(200)


# class ModelProc(CustomHandler):
#     def initialize(self, sql):
#         self.sql = sql

#     # Add new model
#     def post(self):
#         print(self.request.headers['Content-Type'])
#         model = self.sql.query(Entry).filter_by(
#             id=self.get_argument('id')).first()

#         if model == None:
#             # Add
#             model = Entry(id=self.get_argument('id'),
#                           content=self.get_argument('content'))
#             print("Entry Added")
#             self.sql.add(model)
#         else:
#             # Update
#             model.content = self.get_argument('content')
#             print("Entry exists, update")
#         self.sql.commit()
#         self.set_status(200)
#         self.write('{0}'.format(model))

#     # Get all models
#     def get(self):
#         print("Get Models")
#         model = self.sql.query(Entry).all()
#         self.set_status(200)
#         self.write("{0}".format(model))


# class ModelProcID(CustomHandler):
#     def initialize(self, sql):
#         self.sql = sql

#     # Delete model
#     def delete(self, id):
#         print("Delete Entry - ID: " + id)
#         model = self.sql.query(Entry).filter_by(id=id).first()
#         self.sql.delete(model)
#         self.sql.commit()
#         self.set_status(200)
#         self.write("{0}".format(model))

#     # Update model
#     def post(self, id):
#         print("Update Entry - ID: " + id)
#         model = self.sql.query(Entry).filter_by(id=id).first()
#         model.content = self.get_argument('content')
#         self.sql.commit()
#         self.set_status(200)
#         self.write("{0}".format(model))

#     # Get model
#     def get(self, id: str):
#         print("Get Entry - ID: " + id)
#         model = self.sql.query(Entry).filter_by(id=id).first()
#         self.set_status(200)
#         self.write("{0}".format(model))


# class ModelExist(CustomHandler):
#     def initialize(self, sql):
#         self.sql = sql

#     # Check exist
#     def get(self, id: str):
#         model = self.sql.query(Entry).filter_by(id=id).first()
#         self.set_status(200)
#         if model == None:
#             print("Entry Not Exist - ID: " + id)
#             self.write("false")
#         else:
#             print("Entry Exist - ID: " + id)
#             self.write("true")


# 读取/操作

# GET: {srv-name}/property/{property-name}
# POST: {srv-name}/action/{function-name}
# POST & MQTT: {srv-name}/event/{event-name}

# class Property(CustomHandler):
#     def initialize(self, srv):
#         self.srv = srv

#     def post(self, key: str):
#         content = self.get_argument('content')
#         is_read = self.get_argument('is_read')
#         self.set_header('Access-Control-Allow-Origin', '*')
#         if is_read:
#             self.write(json.dumps(self.srv.ReadProperty(
#                 key, content), ensure_ascii=False))
#         else:
#             self.write(json.dumps(self.srv.WriteProperty(
#                 key, content), ensure_ascii=False))


class Action(CustomHandler):
    def initialize(self, srv):
        self.srv = srv

    def get(self, func_name: str):
        self.write(json.dumps(self.srv.Execute(func_name), ensure_ascii=False))

    def post(self, func_name: str):
        args = self.get_argument_dict()
        self.set_header('Access-Control-Allow-Origin', '*')
        self.write(json.dumps(self.selector(func_name, args)))

    def selector(self, func_name: str, content=None):
        if (content == None or content == {} or content == ""):
            return getattr(self.srv.app, func_name)()
        else:
            if isinstance(content, str):
                return getattr(self.srv.app, func_name)(**(json.loads(content)))
            elif isinstance(content, dict):
                try:
                    return getattr(self.srv.app, func_name)(**content)
                except:
                    return getattr(self.srv.app, func_name)(content)
            else:
                # self.app.alarmer.alarm(Err.SRV_REQ_INVALID, 1,
                #                    "f:%{0} - {1}".format(func_name, content))
                return "Content type is not supported"

# class Event(CustomHandler):
#     def initialize(self, srv):
#         self.srv = srv
#         self.mqtt = srv.mqtt

#     def post(self, event_name: str):
#         setup = int(self.get_argument('setup'))  # 0 = off, 1 = on
#         pub_topic = self.get_argument('pub_topic')
#         qos = 1
#         try:
#             qos = int(self.get_argument('qos'))
#         except:
#             pass

#         print("Event Subscribed: {0}, {1}".format(setup, pub_topic))

#         def on_event_callback(content):
#             if (setup > 0):
#                 print("Event auto-pubed: {0}, {1}".format(setup, pub_topic))
#                 self.mqtt.publish(pub_topic, json.dumps(
#                     {'content': content}, ensure_ascii=False), qos)

#         if not hasattr(self.srv.app, 'ecbs'):
#             print("ecb not initiated")
#             self.write("Error: ecb not initiated")
#         else:
#             self.srv.app.ecbs[event_name] = on_event_callback
#             self.write("OK")

# MQTT 操作 (Flow)


# class MqttOp(CustomHandler):
#     def initialize(self, srv):
#         self.srv = srv
#         self.mqtt = srv.mqtt

#     def post(self, func_name: str):
#         op = self.get_argument('op')
#         sub_topic = None

#         try:
#             sub_topic = self.get_argument('sub_topic')
#         except:
#             pass

#         pub_topic = self.get_argument('pub_topic')
#         qos = 1

#         try:
#             qos = int(self.get_argument('qos'))
#         except:
#             pass

#         print("MQTT Op: {0}, {1}, {2}".format(op, sub_topic, pub_topic))

#         # Automate: sub func input, pub func output
#         if (op == "add"):
#             if (sub_topic != None):
#                 self.mqtt.subscribe(sub_topic, qos)

#             # Inject constants
#             constants = {}
#             try:
#                 constants = json.loads(self.get_argument('constants'))
#             except:
#                 pass

#             def on_subs_callback(client, userdata, msg):
#                 msg.payload = json.loads(msg.payload)
#                 msg.payload.update(constants)

#                 result = self.srv.Execute(func_name, msg.payload)
#                 if result is not None:
#                     # Decode input
#                     self.mqtt.publish(pub_topic, json.dumps(
#                         {'content': self.srv.Execute(func_name, msg.payload)}, ensure_ascii=False), qos)
#             # Sub input
#             self.mqtt.message_callback_add(sub_topic, on_subs_callback)
#         elif (op == "remove"):
#             self.mqtt.unsubscribe(sub_topic)
#             self.mqtt.message_callback_remove(sub_topic)
#             # 0.1.19
#             if sub_topic in self.srv.gcbs:
#                 print("Remove global callback array at " +
#                       sub_topic)
#                 del self.srv.gcbs[sub_topic]
#         self.write("OK")

# # Protocol 协议服务专用


# class DevProc(CustomHandler):
#     def initialize(self, sql, srv):
#         self.sql = sql
#         self.srv = srv

#     # Add new model
#     def post(self):
#         print(self.request.headers['Content-Type'])

#         req = json.loads(self.request.body)
#         req_json = json.dumps(req, ensure_ascii=False)
#         id = req['id']

#         model = self.sql.query(Entry).filter_by(id=id).first()

#         if model == None:
#             # Add
#             model = Entry(id=id, content=req_json)
#             print("Device Added")
#             res = self.srv.AddDev(req)
#             # if res is not None:
#             #     self.write(str(res))
#             #     return
#             self.sql.add(model)
#         else:
#             # Update
#             res = self.srv.UpdateDev(req)
#             # if res is not None:
#             #     self.write(str(res))
#             #     return
#             model.content = req_json
#             print("Device exists, update")
#         self.sql.commit()
#         self.set_status(200)
#         self.write('Device Added: {0}'.format(id))

#     # Get all models
#     def get(self):
#         models = self.sql.query(Entry).all()
#         for m in models:
#             m.content = json.dumps(json.loads(m.content), ensure_ascii=False)
#         models = json.dumps([{"id": m.id, "content": m.content}
#                             for m in models], ensure_ascii=False)
#         self.set_status(200)
#         self.write(models)


# class DevProcID(CustomHandler):
#     def initialize(self, sql, srv):
#         self.sql = sql
#         self.srv = srv

#     # Delete model
#     def delete(self, id):
#         print("Delete Device - ID: " + id)
#         model = self.sql.query(Entry).filter_by(id=id).first()
#         if model is None:
#             self.write('Device does not exist - ID: ' + id)

#         res = self.srv.DeleteDev(id)
#         if res is not None:
#             print(res)
#             self.write(str(res))
#             return

#         self.sql.delete(model)
#         self.sql.commit()
#         self.set_status(200)
#         self.write('Device Deleted: {0}'.format(id))
#         if res == "exit":
#             self.set_status(200)
#             self.write('REBOOT, Device Deleted: {0}'.format(id))
#             import os
#             os._exit(1)

#     # Get model
#     def get(self, id: str):
#         print("Get Device - ID: " + id)
#         m = self.sql.query(Entry).filter_by(id=id).first()
#         model = json.dumps(
#             {"id": m.id, "content": m.content}, ensure_ascii=False)
#         self.set_status(200)
#         self.write(model)
