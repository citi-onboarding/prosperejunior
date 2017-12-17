from django.shortcuts import render, redirect
from django.core.mail import send_mail
from templated_email import send_templated_mail

# Create your views here.
def index(request):
	if request.method == 'POST':
		nome = request.POST.get('nome')
		e_mail = request.POST.get('e_mail')
		assunto = request.POST.get('assunto')
		menssagem = request.POST.get('menssagem')

		send_templated_mail(
			template_name = 'e_mail',
			from_email = e_mail,
			recipient_list = ['msgn2@cin.ufpe.br'],
			context ={
			'nome': nome,	
			'e_mail': e_mail,
			'assunto': assunto,
			'menssagem': menssagem,
			},
			)
	return render(
		request,
		'index.html',
		)
