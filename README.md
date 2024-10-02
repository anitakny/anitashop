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
10. Buat berkas HTML baru dengan nama `add_product.html` pada direktori `main/templates`. Isi `add_product.html` dengan kode berikut :
    ```
      {% extends 'base.html' %}

      {% block content %}
      <h1>Tambah Produk Baru</h1>
      
      <form method="POST">
        {% csrf_token %}
        <table>
          {{ form.as_table }}  <!-- Menampilkan form penambahan produk sebagai tabel -->
          <tr>
            <td></td>
            <td>
              <input type="submit" value="Tambah Produk" />  <!-- Tombol submit form -->
            </td>
          </tr>
        </table>
      </form>
      
      {% endblock %}

    ```
11. Buka `views.py` dan tambahkan import :
    ```
      from django.http import HttpResponse
      from django.core import serializers
    ```
13. Masih di file yang sama buat fungsi-fungsi baru sebagai berikut :
    ```
      def show_xml(request):
          data = Product.objects.all()  
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

      def show_json(request):
          data = Product.objects.all()
          return HttpResponse(serializers.serialize("json", data), content_type="application/json")
      
      def show_xml_by_id(request, id):
          data = Product.objects.filter(pk=id)
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
      
      def show_json_by_id(request, id):
          data = Product.objects.filter(pk=id)
    ```
14. Buka `urls.py` dan tambahkan import :
    ```
      from main.views import show_main, add_product, show_xml
      from main.views import show_main, add_product, show_xml, show_json
      from main.views import show_main, add_product, show_xml, show_json, show_xml_by_id, show_json_by_id
    ```
15. Masih di file yang sama, pada `urlpatterns` tambahkan :
    ```
      ...
       path('xml/', show_xml, name='show_xml'),
       path('json/', show_json, name='show_json'),
       path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
       path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
      ...
    ```
16. Mengetest aplikasi pada localhost dengan command:

     ```
     python manage.py runserver
       ```
    kemudian buka [localhost](http://localhost:8000/) di browser.
17. Lakukan `add, commit, push` .

## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan Data Delivery untuk mengimplementasikan sebuah platfrom untuk memusatkan dan mengelola data. Data delivery sangat penting dalam pengimplementasian platform karena memastikan bahwa informasi yang dibutuhkan untuk menjalankan fungsionalitas aplikasi dapat dipertukarkan antara klien dan server. Sehingga dengan adanya hal tersebut data dapat diproses dan dianalisis secara efisien untuk menghasilkan wawasan yang dapat ditindaklanjuti. Dalam platform modern, API (Application Programming Interface) digunakan untuk data delivery sehingga aplikasi dapat berkomunikasi secara efisien dengan layanan pihak ketiga atau aplikasi lain.
## Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Sebelumnya kita perlu tau pengertian dari XML dan JSON. XML, atau eXtensible Markup Language, adalah sebuah format yang dirancang agar mudah dimengerti hanya dengan membacanya, karena setiap elemen dalam XML mendeskripsikan dirinya sendiri. XML banyak digunakan dalam berbagai aplikasi web dan mobile untuk tujuan penyimpanan dan pertukaran data. Sedangkan JSON, atau JavaScript Object Notation, adalah sebuah format yang dirancang agar mudah dimengerti karena setiap elemennya mendeskripsikan dirinya sendiri atau self describing. JSON banyak digunakan dalam berbagai aplikasi web dan mobile untuk menyimpan dan mentransfer data. Menurut saya, dari kedua versi tersebut lebih baik JSON selain karena populer dan banyak dipakai JSON memiliki format yang lebih mudah dibaca manusia. Selain itu, format JSON yang cenderung memiliki karakter lebih sedikit dari format lain seperti XML memungkinkan JSON untuk diproses lebih cepat daripada format lain.
## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi dari is_valid adalah untuk mencegah input data yang tidak valid atau berpotensi merusak sistem. Validasi yang dilakukan di server mencegah manipulasi data dari sisi klien. Intinya agar program berjalan sesuai dengan apa yang kita inginkan.
## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF token diperlukan saat membuat form di Django untuk melindungi keamanan pengguna dari serangan CSRF (Cross-Site Request Forgery). Jika kita tidak menambahkan csrf_token pada form django aplikasi kita menjadi rentan terhadap serangan CSRF. Ini bisa memungkinkan penyerang untuk mengirimkan permintaan palsu atas nama pengguna yang sah tanpa persetujuan mereka.

## Postman
### Local
![image](https://github.com/user-attachments/assets/46842553-9a5d-4062-8d13-ece92cee89a7)
### show_json
![image](https://github.com/user-attachments/assets/cc8aaec8-3cc7-40d9-abf9-7f587457da3c)
### show_json_by_id
![image](https://github.com/user-attachments/assets/03c84211-6d8b-44b6-911b-972e0335af0c)
### show_xml
![image](https://github.com/user-attachments/assets/229c2029-ddb6-4e09-9415-73982a253044)
### show_xml_by_id
![image](https://github.com/user-attachments/assets/ba15a0dd-00d8-4352-a334-767a68eadf58)

# Tugas 4
## Proses Pembuatan Projek Djang0
1. Membuka file `views.py` tambahkan :
    ```
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages
    ```
    dan buat fungsi register
   ```
   def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
   ```
   Selanjutnya, buat file html nya, seperti :
    ```
   {% extends 'base.html' %}

   {% block meta %}
   <title>Register</title>
   {% endblock meta %}
   
   {% block content %}
   
   <div class="login">
     <h1>Register</h1>
   
     <form method="POST">
       {% csrf_token %}
       <table>
         {{ form.as_table }}
         <tr>
           <td></td>
           <td><input type="submit" name="submit" value="Daftar" /></td>
         </tr>
       </table>
     </form>
   
     {% if messages %}
     <ul>
       {% for message in messages %}
       <li>{{ message }}</li>
       {% endfor %}
     </ul>
     {% endif %}
   </div>
   
   {% endblock content %}
    ```
3. Lakukan hal tersebut dan buat login dan logout (walaupun logout tidak mempunyai tampilan hanya mengarahkan ke laman login lagi)
4. Hubungkan antara Product dan User
5. Migrasi dengan command :
    
     ```
      python manage.py makemigrations
      python manage.py migrate
     ```
6. Mengetest aplikasi pada localhost dengan command:
     ```
     python manage.py runserver
     ```
    kemudian buka [localhost](http://localhost:8000/) di browser.
7. Lakukan `add, commit, push` .
## Apa perbedaan antara HttpResponseRedirect() dan redirect()
Perbedaan antara HttpResponseRedirect() dan redirect() yaitu:
1. Argumen
HttpResponseRedirect() hanya dapat mengambil argumen berupa URL, sedangkan redirect() dapat menerima argumen berupa model, view, atau URL.
2. Fleksibelitas
HttpResponseRedirect() digunakan untuk mengarahkan pengguna ke URL tertentu. Sedangkan Redirect() lebih fleksibel dalam hal apa yang dapat dialihkan karena dapat menerima argumen yang lebih beragam.
## Jelaskan cara kerja penghubungan model Product dengan User
Penghubungan antara product dan user di Django menggunakan ForeignKey memungkinkan setiap produk terkait dengan pengguna tertentu. Penghubungan ini digunakan agar setiap produk dapat diketahui siapa pemilik atau pengguna yang membuatnya. Setiap Product hanya bisa dimiliki oleh satu User, tetapi satu User bisa memiliki banyak Product. 
## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut
Authentication adalah proses memverifikasi identitas pengguna. Django mengelola otentikasi dengan mengelola sesi dan menggunakan model pengguna bawaan. Sedangkan authorization adalah proses menentukan apakah pengguna yang sudah terotentikasi memiliki izin untuk melakukan tindakan tertentu. Django menggunakan permissions, groups, dan decorators untuk mengelola otorisasi.
## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django menggunakan session framework untuk menyimpan data pengguna di server dan menghubungkannya dengan browser pengguna melalui session ID yang disimpan di cookies. Setiap kali pengguna melakukan permintaan baru, session ID ini dikirim ke server dan Django menggunakan session yang sesuai untuk mengenali pengguna. Cookies tidak hanya berguna sebagai itu, kegunaan lain dari cookies meliputi manajemen sesi, personalisasi, analitik, dan pelacakan perilaku pengguna. Cookies juga dapat digunakan untuk menyediakan fitur "Remember Me" atau untuk menyimpan preferensi pengguna. Keamanan cookies harus dijaga dengan menerapkan fitur seperti Secure, HttpOnly, dan SameSite cookies, serta dengan tidak menyimpan informasi sensitif di dalam cookies. Karena tdak semua cookies aman, dan perlindungan tambahan diperlukan untuk mencegah serangan seperti session hijacking atau cross-site scripting (XSS).

# Tugas 5
## Proses Pembuatan Projek Django
1. Membuat folder `static` pada root project
2. Menambahkan `global.css` sebagai basis semua laman pada projek
3. Membuat file sseperti `edit_product`, `register.html`, `navbar.html` dan menyesuaikan nya dengan models, menmabahkan url, path nya dll
4. Menambahkan line berikut di base.html untuk menghubungkan css dengan html:
      ```
     <link rel="stylesheet" href="{% static 'css/main.css' %}">
     ```
6. Migrasi dengan command :
     ```
      python manage.py makemigrations
      python manage.py migrate
     ```
 7. Mengetest aplikasi pada localhost dengan command:
     ```
     python manage.py runserver
     ```
    kemudian buka [localhost](http://localhost:8000/) di browser.
8. Lakukan `add, commit, push` .
## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Dalam CSS, urutan prioritas (specificity) pengambilan selector untuk elemen HTML mengikuti aturan tertentu yang menentukan mana yang akan diterapkan ketika ada beberapa aturan yang berlaku untuk elemen yang sama. Berikut adalah aturan dasar dalam penentuan prioritas 
1. Urutan Spesifitas
Inline styles > ID selector > Class selector > Element selector
2. Urutan Cascade 
Jika dua atau lebih selector memiliki tingkat spesifisitas yang sama, maka urutan di mana mereka muncul dalam stylesheet akan menentukan mana yang diterapkan. Aturan yang muncul terakhir akan diterapkan
3. !important
Aturan dengan !important mengalahkan semua aturan lainnya, kecuali ada aturan !important lain yang lebih spesifik
## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design penting karena : 
a. Penggunaan Multi-Device yang Luas
b. Peningkatan Pengalaman Pengguna (User Experience)
c. SEO dan Rekomendasi Google:
d. Efisien
e. Tren penggunaan internet menunjukkan peningkatan pengguna yang lebih sering mengakses web dari perangkat mobile dibandingkan desktop
Aplikasi yang sudah menerapkannya adalah Twitter atau X, dan yang belum biasanya sistem manajemen bisnis atau ERP (Enterprise Resource Planning) kuno atau situs web pemerintah atau instansi yang lebih tua
## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
a. Margin
Margin memiliki kegunaan untuk memberikan jarak antara elemen satu dengan elemen lain
      ```
      div {
        margin: 20px;
      }
      ```
b. Border
Garis yang mengelilingi elemen. Border memisahkan padding dari margin
    ```
      div {
        border: 1px solid black;
      }
      ```
c. Padding
Ruang di dalam elemen, antara konten elemen dan border
      ```
      div {
        border: 1px solid black;
      }

      ```
## Jelaskan konsep flex box dan grid layout beserta kegunaannya!
a. Flex box
Flexbox adalah layout model satu dimensi yang memudahkan pengaturan tata letak elemen secara fleksibel di sepanjang satu arah (baris atau kolom). Flex box berguna untuk mengatur elemen secara dinamis dalam baris atau kolom, seperti menyusun item dalam menu horizontal atau vertikal yang responsif.
b. Grid layout
Grid layout adalah model tata letak dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom.Grid layout berguna untuk layout kompleks dengan banyak elemen yang perlu ditempatkan di berbagai posisi di sepanjang baris dan kolom.
