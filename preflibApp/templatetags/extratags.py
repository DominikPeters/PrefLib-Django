from django import template

register = template.Library()

@register.filter
def keyvalue(dict, key):    
	return dict.get(key)

@register.filter
def getPropFromFile(querySet, metadata):
	return querySet.get(metadata = metadata) 