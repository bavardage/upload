from django import template

register = template.Library()

@register.simple_tag
def magic(request):
	return "more magic"
	
@register.simple_tag
def navigation(request):
	return "You are currently at %s" % request.path   