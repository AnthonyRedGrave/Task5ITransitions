from django import template
from ..forms import LoginForm

register = template.Library()


@register.tag(name='get_login_form')
def get_login_form():
    print("asd")
    login_form = LoginForm()
    return {'login_form' : login_form}