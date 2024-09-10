from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Candy Baby Parfum',
        'price': 'Rp 150.000',  
        'description': 'Candy Baby adalah body mist yang manis dan menyegarkan, dengan aroma permen kapas yang menggoda dan vanilla yang lembut. Parfum ini memberikan sensasi seperti berada di dunia permen yang ceria, sempurna untuk mereka yang ingin menonjolkan sisi playful dan feminin. Dengan aroma ringan namun tahan lama, Candy Baby adalah pilihan ideal untuk digunakan sehari-hari.',
        'quantity': '10',
    }

    return render(request, "main.html", context)
