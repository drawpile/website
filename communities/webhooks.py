import requests
import logging

logger = logging.getLogger(__name__)

def send_abusereport(webhook_url, community, comment, user):
    if user.is_anonymous:
        logger.info(
            "Sending abuse report about %s by anonymous user: %s",
            community.slug,
            comment
        )
    else:
        logger.info(
            "Sending abuse report about %s by %s (#%d): %s",
            community.slug,
            user.username,
            user.id,
            comment
        )

    # we could support other webhook formats here too
    message = {
        "embeds": [
            {
                "title": ":bangbang: {} reported".format(community.title),
                "description": comment,
                "url": "https://drawpile.net/communities/" + community.slug + "/",
                "color": 16711680,
                "author": {
                    "name": user.username,
                },
            }
        ]
    }

    try:
        r = requests.post(webhook_url, json=message)
    except:
        logger.exception("Discord webhook failed")
        return False

    if not r.ok:
        logger.warning("Discord webhook failed: %s", r.text)
        return False

    return True


def send_review_notification(webhook_url, community, user):
    logger.info(
        "Sending community review notificationa about %s by %s (#%d)",
        community.slug,
        user.username,
        user.id
    )

    message = {
        "embeds": [
            {
                "title": ":new: {} is up for review".format(community.title),
                "url": "https://drawpile.net/communities/" + community.slug + "/",
                "color": 41983,
                "author": {
                    "name": user.username,
                },
            }
        ]
    }

    try:
        r = requests.post(webhook_url, json=message)
    except:
        logger.exception("Discord webhook failed")
        return False

    if not r.ok:
        logger.warning("Discord webhook failed: %s", r.text)
        return False

    return True

