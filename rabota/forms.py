#-*- coding:utf-8 -*-
from django import forms
import os
from django.forms import ModelForm
from rabota.models import cam, serega, Seria_name
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.html import mark_safe
from django.utils.translation import ugettext

class ContactForm(forms.Form):
    vari = ((1,(u"По великому учёному ПИФАГОРУ")), (2,(u"Как обычно бывает от 0 до 36")),(3,(u"Для активации 3 варианта")))
    vari1 = ((1,(u"Не стони, если не то ищет хы")), (2,(u"поиск по словам из предложения в хронологическом порядке по Пифу или Обыч. в зависимости от выбранного варианта в первом пункте")), (3,(u"поиск отдельных слов по пифу или обыч. в зависомости от выбранного варианта в 1 пункте")),(4,(u"полное слово П (10) О (20) = полное слово П (10) О (20)")),(5,(u"поиск Пиф (10) Обыч (20) = Пиф(10) Обыч (20)")),(6,(u"поик слов по буквам")),(7,(u"Для активации 3 варианта")))
    vari2 = ((1,(u"Расчитать")), (2,(u"расчитать по предложениям")))
    ishod = forms.FileField(label=u'файл формате txt')
    shablon = forms.CharField(widget=forms.Textarea, label=u'Что ишем')
    variant = forms.ChoiceField(choices=vari, label=u'Вариант 1')
    variant1 = forms.ChoiceField(choices=vari1, label=u'Вариант 2')
    variant2 = forms.ChoiceField(choices=vari2, label=u'Вариант 3')

    def clean_shablon(self):
        shablon = self.cleaned_data['shablon']
        num_word = len(shablon)
        i = 0
        while i<len(shablon):
            for n in range(1040,1103):
                if shablon[i] == unichr(n):
                    raise forms.ValidationError("ты чего ахренел по Русски шпариш")
            i+=1
        if num_word <= 2:
            raise forms.ValidationError("Мало слов")

        return shablon
    def clean_ishod(self):
        ext = os.path.splitext(self.files['ishod'].name)[1]
        if ext != '.txt':
            raise forms.ValidationError("Ахренел не то суёшь")
        return self.cleaned_data['ishod']

class EventSplitDateTime(forms.SplitDateTimeWidget):
    def __init__(self, attrs=None):
        widgets = [forms.TextInput(attrs={'class': 'vDateField'}),
                   forms.TextInput(attrs={'class': 'vTimeField'})]
        # Note that we're calling MultiWidget, not SplitDateTimeWidget, because
        # we want to define widgets.
        forms.MultiWidget.__init__(self, widgets, attrs)

    def format_output(self, rendered_widgets):
        data = u'Дата:'
        time = u'Время:'
        return mark_safe(u'</br>%s%s</br>%s%s' % (data, rendered_widgets[0], time,  rendered_widgets[1]))

class settings_cam(forms.ModelForm):
    class Meta:
        model = cam
def sp():
    return tuple([('','-----')] + [(x.id, x.name) for x in cam.objects.all()])
class view_cam(forms.Form):
    choice = ((1,(u"За весь период")), (2,(u"по дням")),(3,(u"по дням и часам")))
    view_camera = forms.ChoiceField(choices=sp())
    data_time_start = forms.DateTimeField(label=ugettext(u'Начало'), widget=EventSplitDateTime())
    data_time_end = forms.DateTimeField(label=ugettext(u'Конец'), widget=EventSplitDateTime())
    vari_otchet = forms.ChoiceField(choices=choice, label=u'Вариант отчёта')
    data_time_interval = forms.TimeField(label=ugettext(u'Интервал'))

def serg_name():
    return tuple([(0,'-----')] + [(x.id, x.name) for x in Seria_name.objects.all()])
class raschet_form(forms.Form):
    chislo = forms.CharField(label=ugettext(u'Число'),initial='0',required=False)
    chislo1 = forms.CharField(label=ugettext(u'Число1'),initial= '0',required=False)
    chislo2 = forms.CharField(label=ugettext(u'Число2'),initial='0',required=False)
    serga_vari = forms.ChoiceField(choices=serg_name(), required=False, label=u'СЕРИЯ')
    def clean_chislo(self):
        chislo = self.cleaned_data['chislo']
        try:
            s = float(chislo)
        except ValueError:
            raise forms.ValidationError(u'Хули вводишь, ты чё ослеп тебе говорят введи число, а ты придурок чего вводишь то')
        return chislo
    def clean_chislo1(self):
        chislo1 = self.cleaned_data['chislo1']
        try:
            s = float(chislo1)
        except ValueError:
            raise forms.ValidationError(u'Хули вводишь, ты чё ослеп тебе говорят введи число, а ты придурок чего вводишь то')
        return chislo1
    def clean_chislo2(self):
        chislo2 = self.cleaned_data['chislo2']
        try:
            s = float(chislo2)
        except ValueError:
            raise forms.ValidationError(u'Хули вводишь, ты чё ослеп тебе говорят введи число, а ты придурок чего вводишь то')
        return chislo2

class Name_seria(forms.ModelForm):
    class Meta:
        model = Seria_name
class Seria(forms.ModelForm):
    class Meta:
        model = serega


#    class Meta:
#        model = Seria_name


