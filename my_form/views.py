from django.shortcuts import render
from my_form.models import MyFormModel
from django.views.generic import View,ListView



class MyFormView(View):
	template_name = 'my_form/main_form.html'

	def get(self, request, *args, **kwargs):
		return render(request,self.template_name)

	def post(self, request, *args, **kwargs):
		input_dict ={}
		for key,value in request.POST.items():
			if 'name' in key:
				input_dict[key]=value
		MyFormModel.objects.create(json_field=input_dict)
		return render(request,self.template_name)



class DataFormView(ListView):
	model = MyFormModel
	template_name ='my_form/data_form.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context