from django.contrib import admin
from import_export.admin import ImportExportMixin


from dashboard.models import Inquerito, TipoSementeGerminou, TipoAreaGerminacao, VerificacaoSementes, RowControl, Sementeira


class InqueritoAdmin(ImportExportMixin, admin.ModelAdmin):
    ordering = ["nome_agg_familiar", ]
    list_display = ["numero_questionario", "codigo_familia", "nome_agg_familiar",
                    "local_entrevista", "nome_inquiridor", "canais_apresentar_reclamacao"]
    
class SementeiraAdmin(ImportExportMixin, admin.ModelAdmin):
    ordering = ["codigo_familia",]
    list_display = ["numero_questionario", "codigo_familia", "nome_agg_familiar",
                    "local_entrevista", "nome_inquiridor", "canais_apresentar_reclamacao"]
    
class TipoAreaGerminacaoAdmin(ImportExportMixin, admin.ModelAdmin):
    ordering = ["nome_semente",]
    list_display = ["nome_semente", "area", "sementeira"]
    
class TipoSementeGerminouAdmin(ImportExportMixin, admin.ModelAdmin):
    ordering = ["nome_semente",]
    list_display = ["nome_semente", "tempo_germinacao", "sementeira"]


class VerificacaoSementesAdmin(ImportExportMixin, admin.ModelAdmin):
    ordering = ["responsavel_local", ]
    list_display = ["responsavel_local", "data", "horas", "provincia", "embalagens_tem_info",
                    "sementes_tratadas_produto_quimico", "etiquetas_classificadas"]


admin.site.site_header = 'Genesis App Administration'
admin.site.register(Inquerito, InqueritoAdmin)
admin.site.register(TipoAreaGerminacao, TipoAreaGerminacaoAdmin)
admin.site.register(TipoSementeGerminou, TipoSementeGerminouAdmin)
admin.site.register(VerificacaoSementes, VerificacaoSementesAdmin)
admin.site.register(Sementeira, SementeiraAdmin)
