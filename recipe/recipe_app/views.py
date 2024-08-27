from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Recipe
from rest_framework.response import Response
from .serializers import RecipeSerializer


# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def recipe_list(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            recipe = serializer.save()

            response_data = {
                'message' : 'Recipe created successfully',
                'data':serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET','PUT','DELETE'])
def recipe_detail(request,pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response({'Error': 'Recipe not found'},status=404)
    
    if request.method == 'GET':
        serializer  = RecipeSerializer(recipe)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = RecipeSerializer(recipe,data=request.data)
        if serializer .is_valid():
            serializer.save()

            response_data = {
                'message':'Recipe  updated successfully',
                'data':serializer.data,
            }

            return Response(response_data)
        return Response(serializer.errors, status=400)
    

    elif request.method == 'DELETE':
        recipe.delete()
        return Response({"message":'Recipe deleted succesfully'}, 400)
    
    
    
    

            
    