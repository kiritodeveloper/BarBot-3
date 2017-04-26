#!/usr/bin/env python3
import logging

import momoko
from Order import Order
from Robot import Robot

import tornado
import tornado.tcpserver
import tornado.gen
import tornado.ioloop
from tornado import httpclient

class Scheduler(tornado.tcpserver.TCPServer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.http_client = httpclient.AsyncHTTPClient()

        self.numRobots = 2
        self.robots = []
        for i in range(self.numRobots):
            #TODO: replace this location with location from GLS
            self.robots.append(Robot(i, location=(0,0)))

    @tornado.gen.coroutine
    def handle_stream(self, stream, address):
        logging.info("Incoming connection request from %s", address)

    @tornado.gen.coroutine
    def sendPost(self):
        destination = 'http://localhost:8080/test/'
        request = httpclient.HTTPRequest(destination, body='woo', method="POST")
        response = yield self.http_client.fetch(request)
        print(response)

    #read orders from the database
    def getAllOrders(self):
        print("getting the orders")
        order_sql = """
            SELECT id, user_id, drink_id, completed, time, robot_id, priority
            FROM orders
            ORDER BY time
        """
        order_cursor = yield db.execute(order_sql)
        newOrders = order_cursor.fetchall()

        orders = []
        for (id, userId, drinkId, completed, time, robotId, priority) in newOrders:
            robot = None if robotId == -1 else self.robots[robotId]

            #TODO: get wristbandID then location from GLS
            orders.append(Order(id, userId, drinkId, completed=completed,
                                time=time, robot=robot, priority=priority))
        print("got all the orders")
        return orders


    #update the scheduler with stuff
    def updateScheduler(self):
        orders = list(self.getAllOrders())
        
        print("orders!", orders)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    scheduler = Scheduler()
    scheduler.listen(4242)

    ioloop = tornado.ioloop.IOLoop.instance()
    #set up database
    dsn = 'dbname=template1 user=Kim password=icanswim ' \
                  'host=localhost port=10601'
    db = momoko.Pool(dsn=dsn, size=2, ioloop=ioloop)
    dbConnection = db.connect()
    ioloop.add_future(dbConnection, lambda f: ioloop.stop())
    ioloop.start()
    dbConnection.result()

    ioloop.run_sync(scheduler.sendPost)

    tornado.ioloop.PeriodicCallback(scheduler.updateScheduler, 1000).start()
    ioloop.start()
