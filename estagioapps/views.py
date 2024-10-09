from allauth.account.decorators import verified_email_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Company, Review
from .forms import ReviewForm  # Assuming you have a ReviewForm defined
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse


def home(request):
    return render(request, "internships/home.html")


def internship_list(request):
    companies = Company.objects.all()
    return render(request, 'internships/internship_list.html', {'companies': companies})


@login_required(login_url='/accounts/login')
def internship_detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    try:
        reviews = Review.objects.filter(company=company)
    except Review.DoesNotExist:
        reviews = {}
    return render(request, 'internships/internship_detail.html', {'company': company, 'reviews': reviews})


def login(request):
    return redirect("/accounts/login")


def signup(request):
    return redirect("/accounts/signup")


@login_required(login_url='/accounts/login')
def profile(request):
    return redirect("/accounts/profile")


@login_required(login_url='/accounts/login')
def logout(request):
    return redirect("/accounts/logout")


@verified_email_required
def add_review(request, company_id):
    company = Company.objects.get(pk=company_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.company = company
            review.user = request.user  # Assuming you have authentication set up
            review.save()
            return redirect('internship_detail', company_id=company_id)
    else:
        form = ReviewForm()
    return render(request, 'internships/internship_detail.html', {'form': form, 'company': company})


@verified_email_required
def remove_review(request, company_id, review_id):
    review = Review.objects.get(pk=review_id)
    if review.user != request.user or not request.user.is_staff:
        messages.error(request, 'You are not authorized to delete this review')
        return redirect('internship_detail', company_id=company_id)
    review.delete()
    messages.success(request, 'Review deleted')
    return redirect('internship_detail', company_id=company_id)


@verified_email_required
def edit_review(request, company_id, review_id):
    review = Review.objects.get(pk=review_id)
    if review.user != request.user or not request.user.is_staff:
        messages.error(request, 'You are not authorized to edit this review')
        return redirect('internship_detail', company_id=company_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('internship_detail', company_id=company_id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'internships/edit_review.html',
                  {'form': form, 'company_id': company_id, 'review_id': review_id})


def search(request):
    query = request.GET.get('query')
    companies = Company.objects.filter(company__icontains=query)
    return render(request, 'internships/internship_list.html', {'companies': companies})


def average_rating(company):
    reviews = Review.objects.filter(company=company)
    if not reviews.exists():
        return 0
    return sum([review.rating for review in reviews]) / len(reviews)


def top_companies(request):
    companies = Company.objects.all()
    companies = sorted(companies, key=lambda company: -average_rating(company))
    return render(request, 'internships/top_companies.html', {'companies': companies})
