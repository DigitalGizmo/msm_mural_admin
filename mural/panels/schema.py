from statistics import mode
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from pops.models import Visit

from .models import Panel, Article

class PanelNode(DjangoObjectType):
  class Meta:
    model = Panel
    filter_fields = ['id', 'slug']
    interfaces = (relay.Node, )

class ArticleNode(DjangoObjectType):
  class Meta:
    model = Article
    filter_fields = ['panel_id', 'title']
    interfaces = (relay.Node, )

class VisitNode(DjangoObjectType):
  class Meta:
    model = Visit
    filter_fields = ['panel_id', 'title']
    interfaces = (relay.Node, )

class Query(ObjectType):
  # panel = relay.Node.Field(PanelNode)
  all_panels = DjangoFilterConnectionField(PanelNode)
  all_articles = DjangoFilterConnectionField(ArticleNode)