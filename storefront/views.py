def fruit_list():
    fruits=['Apple','Banana','Cherry','Date']
    return render(request,'fruits.html',{'fruits':fruits})

def courses_and_instructors(request):
    context={
        'courses':['python','Django','Mongo'],
        'instructors':['Alice','Bob','Charlie']
    }
    
    return render(request,'courses.html',context)