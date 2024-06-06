from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from .forms import ReviewForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'reviews/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ReviewForm()
    return render(request, 'reviews/product_detail.html', {'product': product, 'reviews': reviews, 'form': form})
