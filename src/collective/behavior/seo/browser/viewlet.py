from ..interfaces import ISEOFieldsMarker
from plone.app.layout.viewlets import common
from Products.CMFPlone.utils import safe_hasattr
from DateTime import DateTime
from plone.dexterity.utils import datify
import pytz
import datetime
from datetime import timedelta
from plone.app.event.base import default_timezone
from plone.app.event.base import localized_now



def outdated(context):
    """
    Check if the content is outdated with priority on the modified date
    1. If the modified date is older than 366 days, the content is outdated
    2. If portal_tye is Event, check if the event has ended and if it has, return True
    3. If the content has a seo_outdated field, return the value of the field
    4. If none of the above, return False
    """
    if context.portal_type in "Event":
        time_delta = datetime.timedelta(hours=3)

        new_datetime = context.end + time_delta
        new_datetime = new_datetime
        now = localized_now()

        if now > new_datetime:
            return True

    modified = context.modified()
    now = DateTime()
    days_past_now = now - 366

    if (bool(modified < days_past_now)) and \
        context.portal_type in ["Event", "News Item"]:
        return True
    elif safe_hasattr(context, "seo_outdated") and context.seo_outdated:
        return True
    return False


class OutdatedViewlet(common.ViewletBase):
    """Override the default Plone viewlet"""

    def update(self):
        super(OutdatedViewlet, self).update()

        try:
            self.behavior = ISEOFieldsMarker(self.context)
        except TypeError:
            self.behavior = None

    def available(self):
        return True if self.behavior else False

    def outdated(self):
        """
        Check if the content is outdated with priority on the modified date
        1. If the modified date is older than 366 days, the content is outdated
        2. If the content has a seo_outdated field, return the value of the field
        3. If none of the above, return False
        """
        return outdated(self.context)
    
    def seo_alternate(self):
        # if safe_hasattr(self.context, "seo_outdated_alternate") and self.context.seo_outdated_alternate:
        #     return self.context.seo_outdated_alternate.to_path
        return None