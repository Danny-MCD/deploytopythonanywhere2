# actor dao 
# this is a demonstration a data layer that connects to a datbase
# Author: Daniel Mc Donagh

import mysql.connector
import dbconfig as cfg
class actorDAO:
    connection =""
    cursor =""
    host =""
    user =""
    password =""
    database =""

    

    def __init__(self): 
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']
    
    def getCursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
    
    
    def getAll(self):
        cursor = self.getCursor()
        sql="select * from actor"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))

        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getCursor()
        sql="select * from actor where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue
    
    def create(self, actor):
        cursor = self.getCursor()
        sql="insert into actor (filmography, name, age) values (%s,%s,%s)"
        values = (actor.get("filmography"), actor.get("name"), actor.get("age"))
        cursor.execute(sql, values )

        self.connection.commit()
        newid = cursor.lastrowid
        actor["id"] = newid
        self.closeAll()
        return actor


    def update(self, id,  actor):
        cursor = self.getCursor()
        sql="update actor set filmography=%s, name= %s, age=%s  where id = %s"
        print(f"update actor {actor}")
        values = (actor.get("filmography"), actor.get("name"), actor.get("age"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        

    def delete(self, id):
        cursor = self.getCursor()
        sql="delete from actor where id = %s"
        values = (id,)
        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll
        print("delete done")
        

    def convertToDictionary(self, result):
        actorKeys = ["id", "filmography", "name", "age"]
        actor = {}
        currentkey = 0
        for attrib in result:
            actor[actorKeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return actor

ActorDAO = actorDAO()