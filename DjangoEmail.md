## Django Email Sending

- in settings.py add this at the last

```python
# Mail settings (Gmail)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Use an app password for Gmail
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

# goto this link to generate your password

- https://myaccount.google.com/apppasswords 
- enter any appname and copy 16 digit password  and paste as your app password