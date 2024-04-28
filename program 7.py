tpl = ('F', 'l', 'a', 'b', 'b', 'e', 'r', 'g', 'a', 's', 't', 'e', 'd')
# addition of ! is not possible as tuple is an immutable
# so to add ! we need to create a new tuple and then make tpl refer to it
tpl = tpl + ('!',)
print(tpl)