from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .convert_string_json import book_str_converted
from .models import book_str

@api_view(['GET','POST'])
def add_show_books(request):
    if request.method=='GET':
        try:
            query_of_sql=book_str.objects.all()
        except Exception as e:
            return Response ({"data":"don't exist"},status=204)
        serializer=book_str_converted(query_of_sql,many=True)
        return Response (serializer.data)
    elif request.method=='POST':
        check=isinstance(request.data,list)
        serializer=book_str_converted(data=request.data,many=check)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data":"Entered"},status=201)
        return Response(serializer.errors,status=400)
@api_view(['GET'])
def get_by_id(request,id):
    try:
        query=book_str.objects.get(id=id)
    except book_str.DoesNotExist:
        return Response({"error":"Book not found"},status=404)
    serializer=book_str_converted(query,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def replace(request,id):
    try:
        query=book_str.objects.get(id=id)
    except Exception as e:
        return Response ({"Element":"not found"},status=404)
    serializer=book_str_converted(query,data=request.data,many=False)
    if serializer.is_valid():
        serializer.save()
        return Response({"data":"is add"},status=200)
    return Response (serializer.errors,status=400)

@api_view(['PATCH'])
def patch_using(request,id):
    try:
        query=book_str.objects.get(id=id)
    except Exception as e:
        return Response ({"No":"Data is their"},status=404)
    serializer=book_str_converted(query,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response ({"Data":"updated"},status=200)
    return Response (serializer.errors,status=204)

@api_view(['DELETE'])
def delete_records(request,id):
    try:
        query=book_str.objects.get(id=id)
    except Exception as e:
        return Response({"Data":"Not Found"},status=404)
    query.delete()
    return Response({"data":"Deleted"},status=200)