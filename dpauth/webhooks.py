import requests
import logging

logger = logging.getLogger(__name__)


def _extract_user(request):
    if request:
        user = request.user
        if user:
            return f"{user.username} ({user.id})"
    return "???"


def _send_notification(webhook_url, emoji, obj_type, description):
    message = {
        "embeds": [
            {
                "title": f"{emoji} {obj_type} Administration",
                "description": description,
            }
        ]
    }

    logger.info("Sending notification %s", message)

    try:
        r = requests.post(webhook_url, json=message)
    except:
        logger.exception("Discord webhook failed")
        return False

    if not r.ok:
        logger.warning("Discord webhook failed: %s", r.text)
        return False

    return True


def _try_send_model_motification(webhook_url, request, action, emoji, obj_type, obj_id):
    try:
        user = _extract_user(request)
        return _send_notification(
            webhook_url, emoji, obj_type, f"{obj_type} ({obj_id}) {action} by {user}"
        )
    except:
        logger.exception("Sending %s %s notification failed", obj_type, action)


def send_save_model_notification(webhook_url, request, change, emoji, obj_type, obj_id):
    action = "updated" if change else "created"
    return _try_send_model_motification(
        webhook_url, request, action, emoji, obj_type, obj_id
    )


def send_delete_model_notification(webhook_url, request, emoji, obj_type, obj_id):
    return _try_send_model_motification(
        webhook_url, request, "deleted", emoji, obj_type, obj_id
    )


def send_delete_queryset_notification(webhook_url, request, emoji, obj_type, obj_ids):
    try:
        user = _extract_user(request)
        return _send_notification(
            webhook_url,
            emoji,
            obj_type,
            f"{len(obj_ids)} {obj_type}(s) {obj_ids} deleted by {user}",
        )
    except:
        logger.exception("Sending delete multiple %s notification failed", obj_type)
