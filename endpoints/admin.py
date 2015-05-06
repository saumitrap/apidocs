from django.contrib import admin
from endpoints.models import Group, Endpoint, Param, Error

class GroupAdmin(admin.ModelAdmin):
	list_display = ['label', 'descr', 'order_rank']


class ParamInline(admin.TabularInline):
	model = Param
	extra = 1


class ErrorInline(admin.TabularInline):
	model = Error
	extra = 1


class EndpointAdmin(admin.ModelAdmin):
	inlines = [ParamInline, ErrorInline]
	fieldsets = (
        (None, {
            'fields': (
            	'group', 
            	('label', 'order_rank'),
            	('method', 'url'),
            	'descr',
				('request_example', 'response_example'),            
			),
        }),
    )

	class Media:
		css = {
			'all': ('/static/admin_extra/css/style.css',)
		}
		js = ('/static/admin_extra/js/script.js',)


admin.site.register(Group, GroupAdmin)
admin.site.register(Endpoint, EndpointAdmin)
