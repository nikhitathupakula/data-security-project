from models import Object
from logger_service import log_event
from datetime import datetime

objects = {}

def upload_object(user, filename, sensitivity):
    obj = Object(filename, user.user_id, sensitivity)
    objects[obj.object_id] = obj

    log_event({
        "action": "upload",
        "user_id": user.user_id,
        "role": user.role,
        "object_id": obj.object_id,
        "sensitivity": sensitivity,
        "status": "success"
    })

    return obj


def download_object(user, object_id):
    obj = objects.get(object_id)

    if not obj:
        user.failed_attempts += 1

        log_event({
            "action": "download",
            "user_id": user.user_id,
            "role": user.role,
            "object_id": object_id,
            "status": "failed",
            "failed_attempts": user.failed_attempts
        })

        return None

    log_event({
        "action": "download",
        "user_id": user.user_id,
        "role": user.role,
        "object_id": object_id,
        "status": "success"
    })

    return obj