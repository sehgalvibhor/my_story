from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import NameForm
import imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com')

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                M.login(request.POST.get('gmail_id',''),request.POST.get('gmail_pass',''))
                rv, mailboxes = M.list()
                M.select("INBOX")
                if rv == 'OK':
                    result,data = M.uid('search', None, "ALL")
                    #result,mail = M.uid('fetch', '4' ,'(RFC822)')

            except Exception as e:
                print e
        else:
            form = NameForm()
    else:
        form=NameForm()
    return render(request, 'emails/index.html', {'form': form})

def thanks(request):

	return render(request, 'emails/thanks.html')


