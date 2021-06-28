from django.http import request
from django.shortcuts import render,redirect
from personal_detail import forms
from personal_detail.models import AddContact
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
#show information

def contact_list(request):
    contact_lists  = AddContact.objects.all()
    row_count  = AddContact.objects.count()
    diction={'title' : 'Contact List', 'contact_lists' : contact_lists, 'row_count' : row_count}
    return render(request,'contact_list.html',context=diction)


#add information
def add_contact(request):
    add_contact_form = forms.AddContactForm()
    
    if request.method == 'POST':
        add_contact_form = forms.AddContactForm(request.POST, request.FILES)
        
        if add_contact_form.is_valid():

            #this section is for sending mail to others...

            # email = request.POST['email']
            # subject = 'Test django mail'
            # message = 'This is a test email from a django project'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [email,]
            # send_mail( subject, message, email_from, recipient_list )


            add_contact_form.save()
            messages.success(request,'Successfully added')

            # recall form for clearing form field after saving data into database                                                   
            add_contact_form = forms.AddContactForm()

                     
        else:
            messages.error(request,add_contact_form.errors)
            
    diction = {'title':'Add Contact', 'add_contact_form':add_contact_form,}

    return render(request,'add_contact.html',context=diction)

# Individual contact information

def show_individual_contact(request,contact_id):
    
    single_contact = AddContact.objects.get(pk=contact_id)

    diction={'title':'Show Contact | '+single_contact.name,'single_contact':single_contact}
    return render(request,'show_individual_contact.html', context=diction)

#delete information

def delete_contact(request,contact_id):
    AddContact.objects.get(pk=contact_id).delete()
    # if delete:
    #     message="Successfully deleted"
    diction = {}
    return redirect('/')


# Edit contact information

def edit_contact(request,contact_id):
    contact_detail  = AddContact.objects.get(pk=contact_id)
    edit_contact_form = forms.AddContactForm(instance= contact_detail,)

    if request.method=='POST':
        edit_contact_form = forms.AddContactForm(request.POST, request.FILES, instance= contact_detail)
         
        if edit_contact_form.is_valid():
            edit_contact_form.save()
            return contact_list(request)

    diction={'title':'Edit Contact', 'edit_contact_form':edit_contact_form}
    return render(request,'edit_contact.html', context=diction)

# Create your views here.
