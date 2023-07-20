from django import template
register=template.Library()




@register.filter()
def swap(data):
    return data.swapcase()

@register.filter()
def counting(s,sub):
    c=0
    for i in range(len(s)):
        if s[i:i+len(sub):]==sub:
            c+=1
    return c
