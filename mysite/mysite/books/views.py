from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from mysite.books.models import Book
from mysite.books.forms import ContactForm



def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('book/search_results.html', {'books': books, 'query': q})
    return render_to_response('book/search_form.html', {'errors': errors})


# def contact(request):
#     errors = []
#     if request.method == 'POST':
#         if not request.POST.get('subject', ''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message', ''):   # 如果未获得数据就添加错误信息，这里的get中的默认空字符串也表示有数据传递进来
#             errors.append('Enter a message.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid e-mail address.')
#         if not errors:
#             send_mail(request.POST['subject'],
#                       request.POST['message'],
#                       request.POST.get('email', 'noreply@example.com'),
#                       ['siteowner@example.com'])
#             return HttpResponseRedirect('/contact/thanks/')
#     return render_to_response('book/contact_form.html', {'errors': errors,
#                                                          'subject': request.POST.get('subject', ''),
#                                                          'message': request.POST.get('message', ''),
#                                                          'email': request.POST.get('email', ''),
#                                                          })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com']
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love this site.'})
    return render_to_response('book/contact_form_rest.html', {'form': form})