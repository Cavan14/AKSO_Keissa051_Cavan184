DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Gunakan PostgreSQL backend
        'NAME': 'my_database',                     # Nama database
        'USER': 'postgres',                        # User PostgreSQL
        'PASSWORD': 'password',                    # Password PostgreSQL
        'HOST': 'postgres',                        # Host PostgreSQL (nama service di docker-compose.yml)
        'PORT': '5432',                            # Port PostgreSQL (default 5432)
    }
}
