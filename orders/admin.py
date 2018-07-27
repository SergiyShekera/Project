from django.contrib import admin
from .models import Order, OrderItem
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html
import csv
import datetime


def Order_Detail(obj):
    return format_html('<a href="{}">Посмотреть</a>'.format(
        reverse('orders:AdminOrderDetail', args=[obj.id])
    ))

def Export_To_CSV(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
        filename=Orders-{}.csv'.format(datetime.datetime.now().strftime("%d/%m/%Y"))
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Первая строка - оглавления
    writer.writerow([field.verbose_name for field in fields])
    # Заполняем информацией
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
    ExportToCSV.short_description = 'Export CSV'

class Order_Item_In_line(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']

class Order_Admin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated', Order_Detail]
    list_filter = ['paid', 'created', 'updated']
    inlines = [Order_Item_In_line]
    actions = [Export_To_CSV]

admin.site.register(Order, Order_Admin)