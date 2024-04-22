from ..interfaces import ISEOFieldsMarker
from plone.app.layout.viewlets import common
from Products.CMFPlone.utils import safe_hasattr


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
        return self.behavior.seo_outdated
    
    def seo_alternate(self):
        # if safe_hasattr(self.context, "seo_outdated_alternate") and self.context.seo_outdated_alternate:
        #     return self.context.seo_outdated_alternate.to_path
        return None