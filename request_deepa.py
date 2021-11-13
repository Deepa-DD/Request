import json
import requests
def courses():
    a = requests.get("http://saral.navgurukul.org/api/courses")
    a1 = a.text
    print(a1)
    print("------------------------")
    with open("courses.json","w") as f:
        python_dict=json.loads(a1)
        json.dump(python_dict,f,indent=4)
    with open("courses.json","r") as f:
        data = json.load(f)
    id_of_courses = [] 
    i = 0
    while i < len(data['availableCourses']):
        print(i,".",data['availableCourses'][i]['name'],"---",data['availableCourses'][i]['id'])
        id_of_courses.append(data['availableCourses'][i]['id'])
        i+=1 
    select_course = int(input("select the course u want by selecting cooresponding number:"))
    excercises = requests.get("http://saral.navgurukul.org/api/courses/"+str(id_of_courses[select_course])+"/exercises")
    a=excercises.json()
    j=0
    l=1
    list_of_slug = []
    while j<len(a["data"]):
        print(l,":",a["data"][j]["name"])
        list_of_slug.append(a['data'][j]["slug"])
        l+=1
        j+=1
    slug_num = int(input("choose the corresp3onding slug number"))
    slug_list = requests.get("http://saral.navgurukul.org/api/courses/"+ str(select_course )+"/exercise/getBySlug?slug=" + list_of_slug[slug_num])
    b=slug_list.json()
    print("content:",b["content"]) 
    next_step = input("coose your next step: \n back \n prev \n next \n exit \n :   ")
    i=0   
    while i<len(list_of_slug):
        if next_step == "back":
            courses()
        elif next_step == "prev":
            slug_list = requests.get("http://saral.navgurukul.org/api/courses/"+ str(select_course )+"/exercise/getBySlug?slug=" + list_of_slug[slug_num-1])
            print("content:",b["content"]) 
            break
        elif next_step == "next":
            slug_list = requests.get("http://saral.navgurukul.org/api/courses/"+ str(select_course )+"/exercise/getBySlug?slug=" + list_of_slug[slug_num+1])
            print("content:",b["content"]) 
            break
        elif next_step == "exit":
            break
courses()
