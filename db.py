import pymongo 



class db:
    database=0
    collection=0 # users
    products=0#products
    def __init__(self):
        self.connect()
        
        return
    def connect(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database=self.client["hack"]
        self.collection=self.database["users"]
        self.products=self.database["products"]
        # print("!11111111111111111111")
        return

    def add_product(self,input):
        temp=self.products
        temp.insert_one(input)
    
    # def delet_product(self,input):
    #     temp=self.products
    #     temp.insert_one(input)

    
    def update_product(self,input):
        temp=self.products
        uq={"owner":input["owner"],"name":input["name"]}
        new={"$set":input}
        if(input["status"]=="-1"):
            temp.delete_one(uq)
        else:
            temp.update_one(uq,new)

    def get_all(self,input):
        temp=self.products
        lis=[]        
        ans=temp.find({"owner":input})
        for x in ans:
            lis.append(x)
        return lis

    def get_details(self,input):
        temp=self.products
        lis=[]
        print(input)
        ans=temp.find()
        for x in ans:
                print(x)
        if(input["tog"]==1):
            ans=temp.find({"name":input["name"],"location":input["location"],"status":"1"})
            for x in ans:
                # print(x)
                lis.append(x)
        elif(input["tog"]==0):
            ans=temp.find({"holder":input["name"],"status":"0"})
            for x in ans:
                lis.append(x)
        elif(input["tog"]==3):
            print("3333")
            print(input)
            ans=temp.find({"owner":input["name"],"status":"0"})
            for x in ans:
                print(x)
                lis.append(x)
        else:
            ans=temp.find({"owner":input["name"],"status":"2"})
            for x in ans:
                lis.append(x)

        return lis

    def get_notifs(self,input):
        temp=self.products
        lis=[]
        ans=temp.find({"owner":input})
        for x in ans:
            lis.append(x)
        return x


    
    def add_user(self,input):
        
        # dicti={"name":"nikhil","pass":"123"}
        # dicti2={"name":"manoj","pass":"234"}
        # self.collection.insert_one(dicti)
        # self.collection.insert_one(dicti2)
        temp=self.collection
        temp.insert_one(input)
        #temp.delete_many({})
        for x in temp.find():
            print(x)
    
    def validate_user(self,name,passed):
        temp=self.collection
        for x in temp.find():
            print(x)
        #print(temp.find({"name":name,"pass":passed}).count(),"ans",name,type(passed))
        if(temp.find({"name":name,"pass":passed}).count()!=0):
            return True
        else:
            return False




# def ini_global_vars():
# 	global database,collection,client
# 	client = pymongo.MongoClient("mongodb://localhost:27017/") 
# 	database=client[database_name]
# 	collection=client[collection_name]

# def clear_database():
# 	delete_from_db({})

# def ins_to_db(input):
# 	global database,collection,client
# 	if(database.collection_name.find({"uid":input["uid"]}).count()==0):		
# 		if "name" in input.keys() and "contact" in input.keys() and "qualification" in input.keys() and "uid" in input.keys():
# 			database.collection_name.insert_one(input)
# 		else:
# 			print("some mandatory information missing")
# 	else:
# 		print("Same uid already exists so database would be updated")
# 		upd_db(input)

# def upd_db(input):
# 	global database,collection,client
# 	input_temp={}
# 	input_temp["$set"]=input
# 	database.collection_name.update_one({"uid":input["uid"]},input_temp)

# def print_all_data():
# 	global database,collection,client
# 	ans=database.collection_name.find()
# 	for res in ans:
# 		print(res)

# def delete_from_db(input):
# 	global database,collection,client
# 	database.collection_name.delete_many(input)
	
# def external_listener(input):
# 	global client
# 	ini_global_vars()
# 	if input["mode"]=="insert":
# 		ins_to_db(input["data"])
# 	elif input["mode"]=="update":
# 		upd_db(input["data"])
# 	elif input["mode"]=="print":
# 		print_all_data()s
# 	elif input["mode"]=="delete":
# 		delete_from_db(input["data"])
# 	else:
# 		print("invalid option")

# 	client.close()	
	

