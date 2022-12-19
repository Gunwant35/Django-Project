from django.shortcuts import render
from home.models import *
# from django_datatables_view.base_datatable_view import BaseDatatableView
# from django.utils.html import escape


# class OrderListJson(BaseDatatableView):
#     # The model we're going to show
#     model = Student

#     # define the columns that will be returned
#     columns = ['sname', 'reg_no', 'taluka', 'address', 'state']

#     # define column names that will be used in sorting
#     # order is important and should be same as order of columns
#     # displayed by datatables. For non-sortable columns use empty
#     # value like ''
#     order_columns = ['number', 'user', 'state', '', '']

#     # set max limit of records returned, this is used to protect our site if someone tries to attack our site
#     # and make it return huge amount of data
#     max_display_length = 500

#     def render_column(self, row, column):
#         # We want to render user as a custom column
#         if column == 'user':
#             # escape HTML for security reasons
#             return escape('{0} {1}'.format(row.customer_firstname, row.customer_lastname))
#         else:
#             return super(OrderListJson, self).render_column(row, column)

#     def filter_queryset(self, qs):
#         # use parameters passed in GET request to filter queryset

#         # simple example:
#         search = self.request.GET.get('search[value]', None)
#         if search:
#             qs = qs.filter(name__istartswith=search)

#         # more advanced example using extra parameters
#         filter_customer = self.request.GET.get('customer', None)

#         if filter_customer:
#             customer_parts = filter_customer.split(' ')
#             qs_params = None
#             for part in customer_parts:
#                 q = Q(customer_firstname__istartswith=part) | Q(customer_lastname__istartswith=part)
#                 qs_params = qs_params | q if qs_params else q
#             qs = qs.filter(qs_params)
#         return qs


# Create your views here.
def index(request):
  return (render(request, 'index.html'))
def view_stud_info(request):
  if(request.method=="POST"):
    sname = request.POST.get('sname')
    reg_no = request.POST.get('reg_no')
    address = request.POST.get('address')
    taluka = request.POST.get('taluka')
    district = request.POST.get('district')
    taluka = request.POST.get('taluka')
    state = request.POST.get('state')
    view_stud_info = Student(address = address, taluka = taluka, district = district, state = state,sname=sname,reg_no = reg_no)
    view_stud_info.save()
  return(render(request, 'student.html'))

def view_marks(request):
  if(request.method=="POST"):
    reg_no = request.POST.get('reg_no')
    subject = request.POST.get('subject')
    marks = request.POST.get('marks')
    semester = request.POST.get('semester')
    view_marks = Marks(reg_no = reg_no, subject = subject, marks = marks, semester = semester)
    view_marks.save()
  return(render(request, 'marks.html'))

def view_admission(request):
  return(render(request, 'admission.html'))

def view_feedback(request):
  return(render(request, 'feedback.html'))



def view_data(request):
  student_data = Student.objects.all()
  student_marks = Marks.objects.all()
  student_feedback = Feedback.objects.all()
  context = {'student' : student_data , 'marks' : student_marks , 'feedback' : student_feedback}
  return render(request , 'view.html' , context)
# Create your views here.
