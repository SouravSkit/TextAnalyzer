#this filke is created by me
from django.http import HttpResponse
from django.shortcuts import render
import re

#def index(request):
#   file = open("1.txt",'r+')
 #  return HttpResponse(file.read())

#def about(request):
#    return HttpResponse('''<a href="https://www.facebook.com">about</a>''')


def ex1(request):
    s = '''<a href = "http://facebook.com">facebook.com</a><br>
        <a href = "https://www.google.com/intl/en-GB/gmail/about/#">Gmail</a><br>
        <a href = "http://yahoo.com">Yahoo.com</a>'''
    return HttpResponse(s)

def index(request):
    params = {'name':'harry', 'place': "mars"}

    return render(request, 'index.html', params)
    #return HttpResponse("Home")

def removepunc(request):

    charcount = request.POST.get("charcount", 'off')
    spaceRemover = request.POST.get("spaceremover", 'off')
    fullc = request.POST.get("fullcaps", 'off')
    dj = request.POST.get('text', 'default')
    state = request.POST.get('removepunc', 'off')
    #return HttpResponse('remove punc <a href= "/">back</a>')
    #analyzed = dj
    if state == "on":
        string = re.sub('[:;\][.,!]', "", dj)
        analyzed = string
        params = {"purpose": 'remove punctuations', 'analyzed_text': analyzed}
        return render (request, 'analyze.html', params)

    elif fullc == "on":
        analyzed = ""
        for char in dj:
            analyzed = analyzed + char.upper()
        params = {"purpose": 'UpperCase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif spaceRemover=="on":
        analyzed = ""
        for index, char in enumerate(dj):
            if dj[index] == " " and dj[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {"purpose": 'spaceRemove', "analyzed_text": analyzed}
        return render(request, "analyze.html", params)

    elif charcount=="on":
        return HttpResponse(len(dj))

    else:
        return HttpResponse(dj)



def capfirst(request):
    return HttpResponse('cap')

def newlineremove(request):
    return HttpResponse('newline remove')

def spaceremover(request):
    return HttpResponse('space remove<a href= "/">back</a>')

def charcount(request):
    return HttpResponse('char count')
