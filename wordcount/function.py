#from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html')

def count(request):
    user_text=request.GET['text']
    total_count=len(user_text)
    word_dict={}
    maxcount=0
    for i in user_text:
        if i not in word_dict:
            word_dict[i] = 1
        else:
            word_dict[i] += 1
    sorted_dict=\
        sorted(word_dict.items(),key=lambda w:w[1],reverse=True)
    for j in word_dict:
        if word_dict[j]>=maxcount:
            maxcount=word_dict[j]
            max_text=j

    return render(request,'count.html',
                    {'count':total_count,
                    'text':user_text,'worddict':word_dict,
                    'max':maxcount,'maxtext':max_text,
                    'sorted':sorted_dict}
                    )
    
def about(request):
    return render(request,'about.html')