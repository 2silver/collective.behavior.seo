import logging
from zope.component import adapter
from ZPublisher.interfaces import IPubAfterTraversal
from Products.CMFPlone.utils import safe_hasattr

logger = logging.getLogger(__name__)


@adapter(IPubAfterTraversal)
def set_http_status(event):
    """
    Set the HTTP status code to 410 if the context has seo_outdated attribute
    """
    request = event.request

    try:
        context = event.request["PARENTS"][0]
    
        if safe_hasattr(context, 'seo_outdated') and context.seo_outdated:
            request.response.setStatus(410, reason='Gone')
    except KeyError as e:
        logger.error("KeyError: {}".format(e))
        pass
