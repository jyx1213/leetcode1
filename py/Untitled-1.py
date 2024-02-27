d={"name":"张三","english":80,"python":90,"math":100}
d1={}
d2={}
d3={}
d4={}
d5={}
scores=[d1,d2]
for score in scores:
    score["name"]=input('请输入姓名')
    score["english"]=eval(input('请输入英语成绩'))
    score["python"]=eval(input('请输入python成绩'))
    score["math"]=eval(input('请输入数学成绩'))
print(scores)
for score in scores:
    temp= (score["english"]+score["python"]+score["math"])/3
    score["avg"]=temp
i=1
while i>0:
    j=i-1
    while j>=0:
        if scores[i]["avg"]>scores[j]["avg"]:
            scores[i],scores[j]=scores[j],scores[i]
            j=j-1
print(scores)
