# Toko Anita

### Proyek Django sederhana yang diperuntukkan untuk pemenuhan Tugas 2 mata kuliah Pemrograman Berbasis Platfrom oleh Anita Khoirun Nisa dengan NPM 2306152273.

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
17. 
   
## Emphasis

*This text will be italic*  
_This will also be italic_

**This text will be bold**  
__This will also be bold__

_You **can** combine them_

## Lists

### Unordered

* Item 1
* Item 2
* Item 2a
* Item 2b

### Ordered

1. Item 1
2. Item 2
3. Item 3
    1. Item 3a
    2. Item 3b

## Images

![This is an alt text.](/image/sample.webp "This is a sample image.")

## Links

You may be using [Markdown Live Preview](https://markdownlivepreview.com/).

## Blockquotes

> Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.
>
>> Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.

## Tables

| Left columns  | Right columns |
| ------------- |:-------------:|
| left foo      | right foo     |
| left bar      | right bar     |
| left baz      | right baz     |

## Blocks of code

```
let message = 'Hello world';
alert(message);
```

## Inline code

This web site is using `markedjs/marked`.
