import random
from storage_service import download_object

def mass_download(user, object_ids):
    for oid in object_ids:
        download_object(user, oid)

def failed_access_spam(user):
    for _ in range(5):
        download_object(user, "fake-object-id")