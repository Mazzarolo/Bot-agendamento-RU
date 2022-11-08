def getInfo():
    user = []

    with open ('info.txt', 'rt') as infos:  
        for info in infos:              
            user.append(info.replace("\n", ""))

    return user