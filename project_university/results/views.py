from django.db import connection
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from results.forms import StudentForm, MarksForm
from results.models import Student, Marks
from django.views.generic.detail import DetailView


def hello(request):
    return HttpResponse("Hello welcome to django, Vicky, Bogga.........") 

def hello_year(request, year):
    return HttpResponse("hello_year::"+str(year)) 

def hello_year_month(request, year, month):
    return HttpResponse("Received year:: "+str(year)+" month :: "+str(month)) 

def display_person(request, name):
    sql = "select id, name, city, pin, phone, email from person where name = '"+ name +"'"
    print sql
    cursor = connection.cursor()
    rs = cursor.execute(sql)
    print rs
    results = cursor.fetchall ()
    print len(results)
    my_html = "<html><body>"
    for row in results:
        print row
        my_html += "<br/><table border='3'><tr><td><b>ID</b></td><td>"+str(row[0])+"</td></tr><tr><td><b>Name</b></td><td>"+row[1]+"</td></tr></tr><tr><td><b>City</b></td><td>"+row[2]+"</td></tr><tr><td><b>Pin</b></td><td>"+row[3]+"</td></tr><tr><td><b>Phone</b></td><td>"+row[4]+"</td></tr><tr><td><b>Email</b></td><td>"+row[5]+"</td></tr></table>"
     
    my_html +="</body></html>"   
        
    print my_html
    return HttpResponse(my_html)
        
def year_archive(request, year):
    return HttpResponse("year_archive::"+str(year))

def person_registration(request):
    template = 'person_registration.html'
    data = {}
    return render_to_response( template, data, RequestContext(request) )

def submit_person(request):
    name = request.GET['name']
    city = request.GET['city']
    pin = request.GET['pin']
    phone = request.GET['phone']
    email = request.GET['email']
    print name, city, pin, phone, email
    
    sql = "insert into person (name,city,pin,phone, email) values ('"+name+"','"+city+"','"+pin+"','"+phone+"' ,'"+email+"')"
    print sql
    
    cursor = connection.cursor()
    rs = cursor.execute(sql)
    print rs
        
    return HttpResponse("User Registration successfully")

def display_all_person(request):
    sql = "select id, name, city, pin, phone, email from person"
    print sql
    cursor = connection.cursor()
    rs = cursor.execute(sql)
    print rs
    results = cursor.fetchall ()
    print len(results)
    my_html = "<html><body>"
    for row in results:
        print row
        my_html += "<br/><table border='3'><tr><td><b>ID</b></td><td>"+str(row[0])+"</td></tr><tr><td><b>Name</b></td><td>"+row[1]+"</td></tr></tr><tr><td><b>City</b></td><td>"+row[2]+"</td></tr><tr><td><b>Pin</b></td><td>"+row[3]+"</td></tr><tr><td><b>Phone</b></td><td>"+row[4]+"</td></tr><tr><td><b>Email</b></td><td>"+row[5]+"</td></tr></table>"
     
    my_html +="</body></html>"   
        
    print my_html
    return HttpResponse(my_html)

# def student_registration(request):
#     template = 'results/student_form.html'
#     data = {'student_form': StudentForm()}
#     #template = 'person_registration.html'
#     #data = {}
#     #return render_to_response( template, data, RequestContext(request) )
#     return render( request, template, data )


###########
# List Student View    
class StudentList(ListView):
    model = Student
    context_object_name = 'student_list'

###########
# Create Student View   
class CreateStudent(CreateView):
    model = Student
    form_class = StudentForm
    success_url = "/results/student_list/"
    
###########
# Delete Student View   
class DeleteStudent(DeleteView):
    model = Student    
    success_url = "/results/student_list/"
    
    def get_object(self, queryset=None):
        obj = Student.objects.get(id=self.kwargs['id'])
        return obj

###########
# Detail Student View 
class StudentDetail(DetailView):
    model = Student
    
###########
# Update Student View 
class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = "/results/student_list/"
    
    def get_object(self, queryset=None):
        obj = Student.objects.get(id=self.kwargs['id'])
        return obj
    
###########
# Create Student View   
class CreateMarks(CreateView):
    model = Marks
    form_class = MarksForm
    success_url = "/results/create_marks/"
    