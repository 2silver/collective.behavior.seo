# -*- coding: utf-8 -*-
from collective.behavior.seo import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from ..interfaces import ISEOFieldsMarker
from z3c.relationfield.schema import RelationChoice


@provider(IFormFieldProvider)
class ISEOFields(model.Schema):
    """ """

    model.fieldset(
        "seofields",
        label=_(u"SEO"),
        fields=("seo_title", "seo_description", "seo_robots", "seo_outdated", "seo_outdated_alternate"),
    )

    seo_title = schema.TextLine(
        title=_(u"SEO Title"),
        description=_(
            u"seo_title_help",
            default=(
                u"Used in the web page 'head' section title and "
                u"browser tab instead of the default title."
            ),
        ),
        required=False,
    )

    seo_description = schema.Text(
        title=_(u"SEO Description"),
        description=_(
            u"seo_description_help",
            default=(
                u"Used as meta description field in the 'head' section "
                u"of a page instead of the default description."
            ),
        ),
        required=False,
    )

    seo_robots = schema.Choice(
        title=_(u"Metatag Robots"),
        description=_(
            u"seo_robots_help",
            default=(
                u"Select options that hint search engines how "
                u"to treat this content. Typically listings are to "
                u"navigate the site, but add little to no value in its "
                u"own and should be set to 'noindex, follow'. In some "
                u"cases you want a listing to be indexed. E.g. when "
                u"publishing a Top 10 recipes list with extra content "
                u"above and below the list, in which case you would use "
                u"'index,follow'."
            ),
        ),
        vocabulary="seofields.robots",
        required=False,
    )

    seo_outdated = schema.Bool(
        title=_(u"label_seo_outdated", default=u"Outdated Content"),
        description=_(
            u"seo_outdated_help",
            default=(
                u"Check this box if the content is outdated and "
                u"should marked as \"Old content\" for visitors and "
                u"SEO (410 Gone)."
            )
        ),
        default=False,
        required=False,
    )

    seo_outdated_alternate = RelationChoice(
        title=_(u"label_seo_outdated_alternate",
                default=u"Alternate URL"),
        description=_("seo_outdated_alternate_help", default=(
            u"Alternate URL for outdated content. "
            u"Maybe a new version of the content.")
        ),
        vocabulary='plone.app.vocabularies.Catalog',
        required=False,
    )



@implementer(ISEOFields)
@adapter(ISEOFieldsMarker)
class SEOFields(object):
    def __init__(self, context):
        self.context = context

    @property
    def seo_title(self):
        if hasattr(self.context, "seo_title"):
            return self.context.seo_title
        return None

    @seo_title.setter
    def seo_title(self, value):
        self.context.seo_title = value

    @property
    def seo_description(self):
        if hasattr(self.context, "seo_description"):
            return self.context.seo_description
        return None

    @seo_description.setter
    def seo_description(self, value):
        self.context.seo_description = value

    @property
    def seo_robots(self):
        if hasattr(self.context, "seo_robots"):
            return self.context.seo_robots
        return None

    @seo_robots.setter
    def seo_robots(self, value):
        self.context.seo_robots = value

    @property
    def seo_outdated(self):
        if safe_hasattr(self.context, "seo_outdated"):
            return self.context.seo_outdated
        return None

    @seo_outdated.setter
    def seo_outdated(self, value):
        self.context.seo_outdated = value


    @property
    def seo_outdated_alternate(self):
        if safe_hasattr(self.context, "seo_outdated_alternate"):
            return self.context.seo_outdated_alternate
        return None

    @seo_outdated_alternate.setter
    def seo_outdated_alternate(self, value):
        self.context.seo_outdated_alternate = value