from django.shortcuts import render,redirect
from .models import Profile,Expense

# Create your views here.
def home(request):
    user = request.user
    profile = Profile.objects.filter(user = user).first()
    expenses = Expense.objects.filter(user=user)

    if request.method == 'POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('expense_type')
        expense = Expense(name=text,amount=amount,expense_type=expense_type,user=user)
        expense.save()

        if expense_type == 'Positive':
            profile.balance += float(amount)
        else:
            profile.expense += float(amount)
            profile.balance -= float(amount)

        profile.save()
        return redirect('/')

    
    context = {'profile':profile,'expenses':expenses}
    return render(request,'home/index.html',context)