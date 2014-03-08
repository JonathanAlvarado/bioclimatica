from django.contrib import admin
from nom.models import ciudades, ciudades_fg, ciudades_k, ciudades_temp, soluciones, soluciones_detalles

# Register your models here.
class cds_fg_inline(admin.TabularInline):
	model = ciudades_fg
	extra = 1

class cds_k_inline(admin.TabularInline):
	model = ciudades_k
	extra = 1

class cds_temp_inline(admin.TabularInline):
	model = ciudades_temp
	extra = 1

class ciudad_admin(admin.ModelAdmin):
	'''fieldsets = [
		('Estado', {'fields': ['estado'] } ),#, 'classes': ['collapse'] } ),
		('Ciudad', {'fields': ['ciudad'] } ),#, 'classes': ['collapse'] } ),
	]'''
	list_display = ('estado', 'ciudad')
	inlines = [cds_fg_inline, cds_k_inline, cds_temp_inline]
	search_fields = ['ciudad']

class sol_detalles_inline(admin.TabularInline):
	model = soluciones_detalles
	extra = 1

class solucion_admin(admin.ModelAdmin):
	list_display = ('id','nombre')
	inlines = [sol_detalles_inline]

admin.site.register(ciudades, ciudad_admin)
admin.site.register(soluciones, solucion_admin)