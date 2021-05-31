from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import compare_img
from PIL import *
from  imgcompare import ImageCompareException

def home(request):
	if request.method == "POST":
		img_1 = request.FILES['img_1']
		img_2 = request.FILES['img_2']
		img_a = Image.open(img_1)
		img_b = Image.open(img_2)

		try:
		    percentage = compare_img(img_a,img_b)
		except ImageCompareException:
			messages.error(request,"Both image should be of same resolution and same type.")
			return redirect("/")


		result = percentage
		context = {'result':result}
		messages.success(request,f" {percentage} matched")

		return render(request,'index.html',context)

	return render(request,'index.html')		


