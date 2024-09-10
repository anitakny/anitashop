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
10. 
   
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
