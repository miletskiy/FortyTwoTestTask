
from django.forms import DateInput
from django.utils.safestring import mark_safe

CSS = {
    'all': (
        'https://code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css',
        )
    }

JS = (
    'https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.0/jquery.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js'
)

parameters = '{ showOtherMonths: true,\
                selectOtherMonths: true,\
                changeMonth: true,\
                changeYear: true,\
                yearRange: "1960:2010"\
}'


class CustomCalendarWidget(DateInput):
    """
    Widget for input data with calendar
    """
    class Media:
        css = CSS
        js = JS

    def render(self, name, value, attrs=None):
        return super(CustomCalendarWidget, self).render(
                    name, value, attrs=attrs)+mark_safe(u"""
            <script type="text/javascript">$("#id_birthday").datepicker({});
            </script>""".format(parameters))
