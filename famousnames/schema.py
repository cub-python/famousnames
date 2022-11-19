import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from doers.models import Name, What_is_famous


# level 1
# class Query(ObjectType):
#     hello = graphene.String(default_value="Hi!")
# schema = graphene.Schema(query=Query)

# level 2
# class NameType(DjangoObjectType):
#     class Meta:
#         model = Name
#         fields = '__all__'
#
# class Query(ObjectType):
#     doers = graphene.List(NameType)
#     def resolve_names(root,info):
#         return Name.objects.all()
#
# schema = graphene.Schema(query=Query)

# # level 3
# class What_is_famousType(DjangoObjectType):
#     class Meta:
#         model = What_is_famous
#         fields = '__all__'
#
# class NameType(DjangoObjectType):
#     class Meta:
#         model = Name
#         fields = '__all__'
#
# class Query(ObjectType):
#     doers = graphene.List(NameType)
#     What_is_famous = graphene.List(What_is_famousType)
#
#     def resolve_names(root, info):
#         return Name.objects.all()
#
#     def resolve_What_is_famous(root, info):
#         return What_is_famous.objects.all()
#
# schema = graphene.Schema(query=Query)

# level 4
class What_is_famousType(DjangoObjectType):
    class Meta:
        model = What_is_famous
        fields = '__all__'


class NameType(DjangoObjectType):
    class Meta:
        model = Name
        fields = '__all__'


class Query(ObjectType):
    name_id = graphene.Field(NameType, id=graphene.Int())

    def resolve_name_id(selfroot, info, id=None):
        if id:
            return Name.objects.get(id=id)
        return Name.objects.all()


schema = graphene.Schema(query=Query)
