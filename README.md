# Toko Anita

### Proyek Django sederhana yang diperuntukkan untuk pemenuhan Tugas mata kuliah Pemrograman Berbasis Platfrom oleh Anita Khoirun Nisa dengan NPM 2306152273.
### Link PWS dapat diakses di [sini](https://anita-khoirun-tokoanita.pbp.cs.ui.ac.id/)

# Tugas 2
## Proses Pembuatan Projek Django

1. Buat _repository_ baru dengan nama `anitashop`.
2. Hubungkan _repository_ dengan local direktori dengan :
   
   ```
   git remote add origin <URL_REPO>
    ```
3. Buat virtual environment dengan menjalankan perintah berikut :

   ```
   python -m venv env
    ```
4. Aktifkan virtual environment dengan perintah berikut:

   ```
   env\Scripts\activate
    ```
5. Buat berkas `requirements.txt` dan isi dengan :

    ```
   django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
6. Lakukan instalasi terhadap dependencies yang ada dengan perintah berikut:
   
   ```
   pip install -r requirements.txt
    ```
7. Buat proyek Django bernama `toko_anita` dengan perintah berikut:
   
   ```
   django-admin startproject toko_anita .
    ```
8. Ubah `ALLOWED_HOSTS` pada file `settings.py` tambahkan dengan string berikut :
   ```
   ...
   ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
   ...
      ```
9. Buat aplikasi `main` dengan :
    ```
    python manage.py startapp main
      ```
    
10. Buat berkas bernama `.gitignore` dan isi dengan :
    ```
    # Django
      *.log
      *.pot
      *.pyc
      __pycache__
      db.sqlite3
      media
      
      # Backup files
      *.bak
      
      # If you are using PyCharm
      # User-specific stuff
      .idea/**/workspace.xml
      .idea/**/tasks.xml
      .idea/**/usage.statistics.xml
      .idea/**/dictionaries
      .idea/**/shelf
      
      # AWS User-specific
      .idea/**/aws.xml
      
      # Generated files
      .idea/**/contentModel.xml
      .DS_Store
      
      # Sensitive or high-churn files
      .idea/**/dataSources/
      .idea/**/dataSources.ids
      .idea/**/dataSources.local.xml
      .idea/**/sqlDataSources.xml
      .idea/**/dynamic.xml
      .idea/**/uiDesigner.xml
      .idea/**/dbnavigator.xml
      
      # Gradle
      .idea/**/gradle.xml
      .idea/**/libraries
      
      # File-based project format
      *.iws
      
      # IntelliJ
      out/
      
      # JIRA plugin
      atlassian-ide-plugin.xml
      
      # Python
      *.py[cod]
      *$py.class
      
      # Distribution / packaging
      .Python build/
      develop-eggs/
      dist/
      downloads/
      eggs/
      .eggs/
      lib/
      lib64/
      parts/
      sdist/
      var/
      wheels/
      *.egg-info/
      .installed.cfg
      *.egg
      *.manifest
      *.spec
      
      # Installer logs
      pip-log.txt
      pip-delete-this-directory.txt
      
      # Unit test / coverage reports
      htmlcov/
      .tox/
      .coverage
      .coverage.*
      .cache
      .pytest_cache/
      nosetests.xml
      coverage.xml
      *.cover
      .hypothesis/
      
      # Jupyter Notebook
      .ipynb_checkpoints
      
      # pyenv
      .python-version
      
      # celery
      celerybeat-schedule.*
      
      # SageMath parsed files
      *.sage.py
      
      # Environments
      .env
      .venv
      env/
      venv/
      ENV/
      env.bak/
      venv.bak/
      
      # mkdocs documentation
      /site
      
      # mypy
      .mypy_cache/
      
      # Sublime Text
      *.tmlanguage.cache
      *.tmPreferences.cache
      *.stTheme.cache
      *.sublime-workspace
      *.sublime-project
      
      # sftp configuration file
      sftp-config.json
      
      # Package control specific files Package
      Control.last-run
      Control.ca-list
      Control.ca-bundle
      Control.system-ca-bundle
      GitHub.sublime-settings
      
      # Visual Studio Code
      .vscode/*
      !.vscode/settings.json
      !.vscode/tasks.json
      !.vscode/launch.json
      !.vscode/extensions.json
      .history
       ```
12. Menambahkan nama aplikasi ke `INSTALLED_APPS` pada file `settings.py` di direktori
13. Buat direktori baru bernama `templates` di dalam direktori aplikasi `main`, lalu buat berkas baru bernama `main.html` dan isi dengan :
     ```
      <h1>Toko Anita</h1>

      <h5>Nama Produk:</h5>
      <p>{{ name }}</p> 
      
      <h5>Harga:</h5>
      <p>{{ price }}</p> 
      
      <h5>Deskripsi:</h5>
      <p>{{ description }}</p> 
      
      <h5>Jumlah:</h5>
      <p>{{ quantity }}</p>

       ```
14. Isi file `urls.py` dengan :
    ```
      from django.contrib import admin
      from django.urls import path, include
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('', include('main.urls')),
      ]
       ```
15. Mengubah file `models.py` dengan :
    
    ```
    class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    mood_intensity = models.IntegerField(default=0)

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5

       ```
16. Migrasi dengan command :
    
     ```
      python manage.py makemigrations
      python manage.py migrate
       ```
17. Menambahkan fungsi untuk me-render laman main pada file `views.py` :
    ```
    from django.shortcuts import render

      # Create your views here.
      def show_main(request):
          context = {
              'name': 'Candy Baby Parfum',
              'price': 'Rp 150.000',  
              'description': 'Candy Baby adalah body mist yang manis dan menyegarkan, dengan aroma permen kapas yang menggoda dan vanilla yang lembut. Parfum ini memberikan sensasi seperti berada di dunia permen       yang ceria, sempurna untuk mereka yang ingin menonjolkan sisi playful dan feminin. Dengan aroma ringan namun tahan lama, Candy Baby adalah pilihan ideal untuk digunakan sehari-hari.',
              'quantity': '10',
          }

    return render(request, "main.html", context)
      ```
18. Mengetest aplikasi pada localhost dengan command:

     ```
     python manage.py runserver
       ```
    kemudian buka [localhost](http://localhost:8000/) di browser.

19. Lakukan `add, commit, push` .


## Bagan yang berisi request client
![URL](https://github.com/user-attachments/assets/8604d46d-3972-409f-b986-ff755e80c105)

## Fungsi Git dalam Pengembangan Perangkat Lunak
Git adalah sistem kontrol versi yang membantumu melacak perubahan pada kode sumber proyek. Kita dapat memantau semua perubahan, revisi yang terjadi di proyek kita
Jadi, git emungkinkan tim untuk melacak perubahan kode, menyimpan versi, dan bekerja bersama dalam proyek secara efisien. Sehingga memainkan peran penting dalam pengembangan perangkat lunak modern dan kolaborasi tim.

## Mengapa Django sebagai Framework Permulaan?
Django menyediakan struktur yang kuat dan banyak fitur built-in, seperti ORM dan sistem routing, yang membuatnya cocok untuk pemula belajar pengembangan web. Selain itu, Django menggunakan bahasa pemrograman Python sehingga lebih mudah dipahami karena bahasa ini memiliki sintaksis yang elegan dengan menggunakan kunci bahasa Inggris yang sederhana. Kerangka kerja web Django mendukung pengembangan cepat dan desain yang bersih dan pragmatis. Langkah-langkah keamanan bawaan Django menawarkan perlindungan yang cukup bagi banyak bisnis dan kerangka kerjanya mudah diperluas untuk memenuhi kebutuhan kepatuhan tambahan juga.

## Mengapa Django ORM?
Django ORM atau singkatan dari Object-Relational Mapping. Object adalah apa yang kita gunakan dalam bahasa pemrograman, relasi adalah basis data pada proyek sedangkan pemetaan adalah tautan antara keduanya. Django ORM memetakan model-model Python ke tabel-tabel dalam database sehingga memungkinkan manipulasi data yang mudah dan efisien. Lalu, abstraksi yang disediakan oleh Django ORM membantu pengembang fokus pada logika aplikasi dan meningkatkan produktivitas secara keseluruhan.

# Tugas 3
## Proses Pembuatan Projek Django

1. Buat direktori baru bernama `templates` di dalam `root folder`, lalu buat berkas baru bernama `base.html` dan isi dengan :
   ```
      {% load static %}
      <!DOCTYPE html>
      <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          {% block meta %} {% endblock meta %}
        </head>
      
        <body>
          {% block content %} {% endblock content %}
        </body>
      </html>
   ```
2. Buka file bernama `settings.py` yang ada di dalam direktori proyek `toko_anita`, lalu sesuaikan :
    ```
      ...
      TEMPLATES = [
          {
              'BACKEND': 'django.template.backends.django.DjangoTemplates',
              'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
              'APP_DIRS': True,
              ...
          }
      ]
      ...
    ```
3. Ubah kode pada berkas `main.html` menjadi :
   ```
      {% extends 'base.html' %}
       {% block content %}
       <h1>Toko Anita</h1>
      
       <h5>Nama Produk:</h5>
        <p>{{ name }}</p>
      
        <h5>Deskripsi:</h5>
        <p>{{ description }}</p>
      
        <h5>Jumlah:</h5>
        <p>{{ quantity }}</p>
       {% endblock content %}

    ```
4. Buka `models.py` dan tambahkan kode ini :
   ```
      import uuid  # tambahkan baris ini di paling atas
      
      class Product(models.Model):
       id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # tambahkan baris ini
       name = models.CharField(max_length=255)
       price = models.IntegerField()
       description = models.TextField()
       quantity = models.IntegerField(default=0)
       mood_intensity = models.IntegerField(default=0)
   
       @property
       def is_mood_strong(self):
           return self.mood_intensity > 5


    ```
5. Migrasi dengan command :
    
     ```
      python manage.py makemigrations
      python manage.py migrate
     ```
6. Buat berkas baru pada direktori `main` dengan nama `forms.py` dan isi lah dengan :
   ```
   from django.forms import ModelForm
   from main.models import Product
   
   class ProductForm(ModelForm):
       class Meta:
           model = Product
           fields = ['name', 'price', 'description', 'quantity', 'mood_intensity']
   ```
7. Buka pada direktori `main` dengan nama `views.py` dan tambahkan import :
   ```
   from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
   from main.forms import MoodEntryForm
   from main.models import MoodEntry
   ```
8. Masih diberkas yang sama, buatlah fungsi baru dengan nama `add_product` dan isi dengan :
   ```
   def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
   ```
9. Lalu ubah fungsi `show_main` jadi :
    ```
    def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Candy Baby Parfum',
        'price': 'Rp 150.000',
        'description': 'Candy Baby adalah body mist yang manis dan menyegarkan, dengan aroma permen kapas yang menggoda dan vanilla yang lembut. Parfum ini memberikan sensasi seperti berada di dunia permen yang ceria, sempurna untuk mereka yang ingin menonjolkan sisi playful dan feminin. Dengan aroma ringan namun tahan lama, Candy Baby adalah pilihan ideal untuk digunakan sehari-hari.',
        'quantity': '10',
        'products': products  
    }

    return render(request, "main.html", context)
    ```
