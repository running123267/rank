from django.shortcuts import render
from rest_framework.views import APIView
from rankings.models import *
from rest_framework.response import Response
from rankings.serializer import *
class Index(APIView):
    def post(self,request):
        """获取前端的数据"""
        name = request.data.get('name')
        grade = request.data.get('grade')
        """判断他们不为空"""
        if not all([name,grade]):
            return Response({'code':10020,'messet_age':'输入不能为空'})
        """分数只能在1到1000000之间"""
        if not grade.isdigit() or int(grade) not in range(1, 10000001):
            return Response({'code':10023,'messet_age':'分数范围必须在1-10000000'})
        """数据库添加数据"""
        user = User(name=name,grade=grade)
        """存入数据库"""
        user.save()
        """数据返回前端"""
        return Response({'code': 200, 'messet_age': '添加成功'})

# 展示
class Show(APIView):
    def get(self,request):
        """假设客户端5 进行访问"""
        username='客户5'
        """ 把所有分数从大到小排列"""
        user = User.objects.all().order_by('-grade')
        list_a=[]
        num=0
        alist = {}
        for i in user:
            num+=1
            if i.name == username:
                """给alist赋值 模拟显示"""
                alist['rank']=num
                alist['name']=i.name
                alist['grade']=i.grade
            try:
                """start end  如果获取到就查这个区间的值 获取不到就都查出来"""
                start = int(request.GET.get('start'))  # 查询任何名次段
                end = int(request.GET.get('end'))
                if num >= start and end>=num:
                    set_a = {}
                    set_a['name'] = i.name
                    set_a['grade'] = i.grade
                    set_a['rank'] = num
                    list_a.append(set_a)
                """跳出此次循环，继续执行下一次循环 """
                continue
                #报错执行的语句
            except Exception:
                set_a = {}
                set_a['name'] = i.name
                set_a['grade'] = i.grade
                set_a['rank'] = num
                list_a.append(set_a)
        """返回给前端"""
        return Response({'code':200,'messet_age':list_a,'alist':alist})
