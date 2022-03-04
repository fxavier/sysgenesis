from django.contrib import admin
from import_export.admin import ImportExportMixin


from dashboard.models import Inquerito, TipoSementeGerminou, TipoAreaGerminacao, VerificacaoSementes, RowControl


class InqueritoAdmin(ImportExportMixin, admin.ModelAdmin):
    ordering = ["nome_agg_familiar", ]
    list_display = ["numero_questionario", "codigo_familia", "nome_agg_familiar",
                    "local_entrevista", "nome_inquiridor", "canais_apresentar_reclamacao"]


class VerificacaoSementesAdmin(ImportExportMixin, admin.ModelAdmin):
    ordering = ["responsavel_local", ]
    list_display = ["responsavel_local", "data", "horas", "provincia", "embalagens_tem_info",
                    "sementes_tratadas_produto_quimico", "etiquetas_classificadas"]


admin.site.site_header = 'Genesis App Administration'
admin.site.register(Inquerito, InqueritoAdmin)
admin.site.register(TipoAreaGerminacao)
admin.site.register(TipoSementeGerminou)
admin.site.register(VerificacaoSementes, VerificacaoSementesAdmin)
admin.site.register(RowControl)
