# This Program shows error
"""
def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'
eggs = 'global'
spam()"""

# Correction
def spam():
    eggs = 'spam local'
    print(eggs) # CORRECTION!
eggs = 'global'
spam()