import itchat

itchat.auto_login(hotReload = True, enableCmdQR=2)


# memberList = itchat.get_friends(update= True)[1:]
# the member list excloud the chatroom

# theChatroom = itchat.search_chatrooms(name='itchatroom')

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def reply_chatroom_msg(msg):
    print("收到一条群信息：", msg['ActualNickName'], msg['Content'])

@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    print("收到一条信息：", msg['User'], msg['Content'])

# r = itchat.send('Hello, itchatroom', theChatroom[0]['UserName'])
# print(r)

itchat.run()
itchat.dump_login_status()