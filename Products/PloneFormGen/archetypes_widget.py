from Products.Archetypes.Registry import registerWidget, registerPropertyType
import Products.Archetypes.Widget as atw



class StringWidget(atw.StringWidget): pass

# TODO: these registerWidget() calls are from the original AT code, but it
#       seems they might not be necessary, perhaps because PFG specifies the
#       widget class directly

# registerWidget(StringWidget,
#                title='String',
#                description=('Renders a HTML text input box which '
#                             'accepts a single line of text'),
#                used_for=('Products.Archetypes.Field.StringField',)
#                )
# registerPropertyType('maxlength', 'integer', HatchdStringWidget)

class SelectionWidget(atw.SelectionWidget): pass

# registerWidget(SelectionWidget,
#                title='Selection',
#                description=('Renders a HTML selection widget, which '
#                             'can be represented as a dropdown, or as '
#                             'a group of radio buttons'),
#                used_for=('Products.Archetypes.Field.StringField',
#                          'Products.Archetypes.Field.LinesField',)
#                )

class PasswordWidget(atw.PasswordWidget): pass

# registerWidget(PasswordWidget,
#                title='Password',
#                description='Renders a HTML password widget',
#                used_for=('Products.Archetypes.Field.StringField',)
#                )

class IntegerWidget(atw.IntegerWidget): pass

# registerWidget(IntegerWidget,
#                title='Integer',
#                description=('Renders a HTML text input box which '
#                             'accepts a integer value'),
#                used_for=('Products.Archetypes.Field.IntegerField',)
#                )

class DecimalWidget(atw.DecimalWidget): pass

# registerWidget(DecimalWidget,
#                title='Decimal',
#                description=('Renders a HTML text input box which '
#                             'accepts a fixed point value'),
#                used_for=('Products.Archetypes.Field.FixedPointField',)
#                )

class BooleanWidget(atw.BooleanWidget): pass

# registerWidget(BooleanWidget,
#                title='Boolean',
#                description='Renders a HTML checkbox',
#                used_for=('Products.Archetypes.Field.BooleanField',)
#                )

class CalendarWidget(atw.CalendarWidget): pass

# registerWidget(CalendarWidget,
#                title='Calendar',
#                description=('Renders a HTML input box with a helper '
#                             'popup box for choosing dates'),
#                used_for=('Products.Archetypes.Field.DateTimeField',)
#                )

class LabelWidget(atw.LabelWidget): pass

# registerWidget(LabelWidget,
#                title='Label',
#                description=('Renders a HTML widget that only '
#                             'displays the label'),
#                used_for=None
#                )

class MultiSelectionWidget(atw.MultiSelectionWidget): pass

# registerWidget(MultiSelectionWidget,
#                title='Multi Selection',
#                description=('Renders a HTML selection widget, where '
#                             'you can be choose more than one value'),
#                used_for=('Products.Archetypes.Field.LinesField',)
#                )

class RichWidget(atw.RichWidget): pass

# registerWidget(RichWidget,
#                title='Rich Widget',
#                description=('Renders a HTML widget that allows you to '
#                             'type some content, choose formatting '
#                             'and/or upload a file'),
#                used_for=('Products.Archetypes.Field.TextField',)
#                )
