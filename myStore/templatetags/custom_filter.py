from django import template


register=template.Library()

@register.filter(name='currency')
def currency(num):
    res="₹"+str(num)
    return res

@register.filter(name='multiply')
def multiply(num, num1):
    return num*num1