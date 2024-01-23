from django.shortcuts import render, redirect, get_object_or_404
from .models import Notice
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

def notice_list(request):
    notices = Notice.objects.all().order_by('-timestamp')
    return render(request, 'notices/index.html', {'notices': notices})

def remove_notice(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    if request.method == 'POST':
        notice.delete()
        return redirect('notice_list')
    return render(request, 'notices/remove_notice.html', {'notice': notice})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'notices/user_login.html')

@staff_member_required
def admin_login(request):
    return render(request, 'notices/admin_login.html')

