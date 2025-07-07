from modeltranslation.translator import register, TranslationOptions
from .models import SpaceObj, Category

@register(SpaceObj)
class SpaceObjTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
