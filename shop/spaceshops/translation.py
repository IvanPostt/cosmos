from modeltranslation.translator import register, TranslationOptions
from .models import CategoryObj, SpaceProduct

@register(SpaceProduct)
class SpaceObjTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(CategoryObj)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
