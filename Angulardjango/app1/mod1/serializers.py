from rest_flex_fields import FlexFieldsModelSerializer
from .models import Product, Category, Company, ProductSize, ProductSite, Comments
from django.contrib.auth.models import User


class CompanySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Company
        fields = ['pk', 'name', 'url']


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        expandable_fields = {
          'products': ('mod1.ProductSerializer', {'many': True})
        }


class ProductSizeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['pk', 'name']


class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'content', 'created', 'updated']
        expandable_fields = {
            'category': ('mod1.CategorySerializer', {'many': True}),
            'sites': ('mod1.ProductSiteSerializer', {'many': True}),
            'comments': ('mod1.CommentSerializer', {'many': True}),
        }


class ProductSiteSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSite
        fields = ['pk', 'name', 'price', 'url', 'created', 'updated']
        expandable_fields = {
            'product': 'mod1.CategorySerializer',
            'productsize': 'mod1.ProductSizeSerializer',
            'company': 'mod1.CompanySerializer',
        }


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comments
        fields = ['pk', 'title', 'content', 'created', 'updated']
        expandable_fields = {
            'product': 'mod1.CategorySerializer',
            'user': 'mod1.UserSerializer'
        }