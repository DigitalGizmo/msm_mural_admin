from statistics import mode
from graphene import relay, ObjectType, Field, String
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Panel, Article
from pops.models import Hotspot, Visit, Learnmore #, Slide, Voice

class PanelNode(DjangoObjectType):
  class Meta:
    model = Panel
    filter_fields = ['id', 'slug']
    interfaces = (relay.Node, )

class ArticleNode(DjangoObjectType):
  article_type = String() # Prevents output Uppercase
  class Meta:
    model = Article
    filter_fields = ['panel_id', 'title']
    interfaces = (relay.Node, )

class HotspotNode(DjangoObjectType):
  class Meta:
    model = Hotspot
    filter_fields = ['panel_id']
    interfaces = (relay.Node, )

class VisitNode(DjangoObjectType):
  class Meta:
    model = Visit
    filter_fields = ['panel_id']
    interfaces = (relay.Node, )

class LearnmoreNode(DjangoObjectType):
  learnmore_type = String() # Prevents output Uppercase
  class Meta:
    model = Learnmore
    filter_fields = ['article_id', 'learnmore_type']
    interfaces = (relay.Node, )

# class SlideNode(DjangoObjectType):
#   class Meta:
#     model = Slide
#     filter_fields = ['learnmore_id']
#     interfaces = (relay.Node, )

# class VoiceNode(DjangoObjectType):
#   class Meta:
#     model = Voice
#     filter_fields = ['article_id']
#     interfaces = (relay.Node, )

class PanelType(DjangoObjectType):
    class Meta:
        model = Panel
        fields = ("id", "slug", "panel_title")

class Query(ObjectType):
  # panel = relay.Node.Field(PanelNode)

  all_panels = DjangoFilterConnectionField(PanelNode)

  # all_articles = DjangoFilterConnectionField(ArticleNode)
  panel_by_slug = Field(PanelType, 
    slug=String(required=True))
  # panel_by_slug = Field(PanelType)

  def resolve_panel_by_slug(root, info, slug):
      try:
          # return City.objects.get(title=title)
          return Panel.objects.get(slug=slug)
      except Panel.DoesNotExist:
          return None