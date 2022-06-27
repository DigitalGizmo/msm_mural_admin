import graphene

import panels.schema

class Query(
    panels.schema.Query,
    graphene.ObjectType):
    # This class will inherit from multiple Queries
    pass

schema = graphene.Schema(query=Query)
# print(str(schema))