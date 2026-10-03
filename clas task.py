# # class Bank :
# #     def __init__(self,owner,pinkod,balance):
# #         self.owner = owner
# #         self.__pinkod = pinkod
# #         self._balance = balance

# #     @property
# #     def show_balance(self):
# #             return f"Balance:{self._balance}"


# #     @show_balance.setter
# #     def show_balance (self,amout):
# #             if amout > 0 :
# #                 self._balance += amout
# #                 return f"New blanace {self._balance}"


# # card1 = Bank("Abdulloh", 1234 , 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)


# # print(card1.show_balance)
# # card1.show_balance = 10
# # print(card1.show_blance)








# from datetime import datetime

# task_db = []
# user_db = []
# is_login = None

# user_id = 0
# task_id = 0


# def create_task(title,description,dueration,user_id):
#     global task_id
#     task_id +=1
#     task = {
#         "task_id": task_id,
#         "title": title,
#         "description": description,
#         "dueration": dueration,
#         "status": False,
#         "user_id": user_id,
#         "created_at": datetime.now(),
#     }
#     task_db.append(task)


# def read_task(task_id, user_id):
#     for i in task_db:
#         if i["task_id"] == task_id and i["user_id"] ==user_id:
#             return f"""
# Your task {i["task_id"]}:
# Title:{i["title"]}
# Description:{i["description"]}
# Dueration :{i["dueration"]}
# Status:{i["status"]}
# """
#     return False


# def update_task(task_id,title,descp,due,status,user_id):
#     for i in task_db:
#         if i["task_id"] ==task_id and i["user_id"] ==user_id:
#             if title:
#                 i["title"] =title
#             if descp:
#                 i["description"] =descp
#             if due:
#                 i["dueration"] =due
#             if status:
#                 i["status"] =status
#             return True
#     return False


# def delete_task(task_id, user_id):
#     for i in task_db:
#         if i["task_id"] ==task_id and i["user_id"] ==user_id:
#             task_db.remove(i)
#             return True
#     return False


# def registration(username, password):
#     global user_id, is_login
#     for user in user_db:
#         if user["username"] == username:
#             print("This username is already taken!")
#             return False

#     user_id +=1
#     user = {
#         "user_id": user_id,
#         "username": username,
#         "password": password,
#         "created_at": datetime.now(),
#     }
#     user_db.append(user)
#     is_login =user
#     print("Registration successful!")
#     return True


# def login(username,pasword):
#     global is_login
#     for user in user_db:
#         if user["username"] ==username and user["password"] ==pasword:
#             is_login =user
#             print(f"Welcome ,{username}!")
#             return True
#     print("Invalid username or password!")
#     return False




# def change_password(user_id,oldpasword,nevpasword):
#     global is_login
#     if is_login["password"] ==oldpasword:
#         is_login["password"] =nevpasword
#         print("Pasword updated successfully!")
#         return True
#     else:
#         print("Old pasword is incorrect!")
#         return False


# def show_profile(user):
    
#     return f"""
#     salom {user["username"]}
#     id user: {user["user_id"]}
#     Username: {user["username"]}
#     aded : {user["created_at"]}
#     Fhone number:{user["phone_number"]}
    


# """


# while True:
#     if is_login is None:
#         n =int(
#             input("\n1)registration\n2)login\n0)exit\nchoose one: ")
#         )
#         match n:
#             case 1:
#                 username =input("Username: ")
#                 password =input("Password : ")
#                 registration(username, password)
#             case 2:
#                 username =input("Username: ")
#                 password =input("Password : ")
#                 login(username, password)
#             case 0:
#                 print("Good bye")
#                 break
#             case _:
#                 print("Invalid input!")

#     else:
#         n =int(
#             input(
#                 "\n1)Create Task\n2)Read task\n3)Update Task\n4)Delete Task\n5)Show Profile\n6)Change Password\n7)Logout\n0)Exit\nChoose one: "))

        
#         match n:
#             case 1:
#                 print("Start create task")
#                 title =input("Title: ")
#                 descp =input("Description: ")
#                 durat =input("Duration: ")
#                 create_task(title, descp, durat, is_login["user_id"])
#                 print("Task created !!")

#             case 2:
#                 k =int(input("Enter id task: "))
#                 print(read_task(k, is_login["user_id"]))

#             case 3:
#                 print("Start update task")
#                 k =int(input("Enter id task: "))
#                 if read_task(k, is_login["user_id"]):
#                     title =input("Title or put enter for continue: ")
#                     descp =input("Description or put enter for continue: ")
#                     durat =input("Duration or put enter for continue: ")
#                     status =bool(
#                         input("Status (leave empty for False, write anything for True): ")
#                     )
#                     update_task(
#                         k,title,descp,durat,status,is_login["user_id"]
#                     )
#                     print("Task updated !!")
#                 else:
#                     print("This profil not fond")

#             case 4:
#                 k =int(input("enter id task: "))
#                 if delete_task(k, is_login["user_id"]):
#                     print("your task delited !")
#                 else:
#                     print("This profil not fond")

#             case 5:
#                 print(show_profile(is_login))

            


#             case 6:
#                 kodikuhna =input("Enter current password: ")
#                 kodinav =input("Enter new password: ")
#                 change_password(is_login["user_id"], kodikuhna,kodinav)

#             case 7:
#                 is_login = None
#                 print("Logged out successfully!")

#             case 0:
#                 print("Exit")
#                 break

#             case _:
#                 print("Invalid input !!!")




