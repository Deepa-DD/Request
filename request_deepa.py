import json
import requests
result=requests.get("https://saral.navgurukul.org/api/courses")
data=result.json()
f=open("fileDeepa.json","w")
data2=json.dump(data,f,indent=6)
f.close()
def navigation(temp,list,slug_user,data_new):
    while True:
        i=slug_user
        navigatiion_user=int(input(" \n what navigation part you want ? \n for up : 1 \n for next : 2 \n for back : 3 \n  for quit: 0 \n   " ))
        if navigatiion_user==1:
            slug_api=requests.get(" http://saral.navgurukul.org/api/courses/"+str(temp)+"/exercise/getBySlug?slug="+str(list[i-2]))
            cont=slug_api.json()
            print(cont["content"])
        elif navigatiion_user==2:
            slug_api=requests.get(" http://saral.navgurukul.org/api/courses/"+str(temp)+"/exercise/getBySlug?slug="+str(list[i]))
            cont=slug_api.json()
            print(cont["content"])
        elif navigatiion_user==3:
            c2=1
            for i3 in data_new["data"]:
                print(c2,i3["name"])
                c2+=1
                c3=1
                for i4 in i3["childExercises"]:
                    print(c3,i4["name"])
                    c3+=1
        else:
            break
        

def request():
    c=1
    for i in data["availableCourses"]:
        print(c," ",i["name"],":_ ",i["id"])
        c+=1
    for i2 in data["availableCourses"]:
        user=int(input(" enter couse id :   "))
        temp=data["availableCourses"][user-1]["id"]
        api=requests.get("http://saral.navgurukul.org/api/courses/"+str(temp)+"/exercises")
        data_new=api.json()
        # print(data_new)

        list=[]
        c2=1
        for i3 in data_new["data"]:
            print(c2,i3["name"])
            list.append(i3["slug"])
            c2+=1
            c3=1
            for i4 in i3["chixercildEses"]:
                print(c3,i4["name"])
                list.append(i4["slug"])
                c3+=1
        slug_user=int(input(" enter number for slug content :   "))
        slug_api=requests.get(" http://saral.navgurukul.org/api/courses/"+str(temp)+"/exercise/getBySlug?slug="+str(list[slug_user-1]))
        content=slug_api.json()
        print(content['content'])
        navigation(temp,list,slug_user,data_new)
request()

