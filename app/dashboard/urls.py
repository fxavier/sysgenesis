from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('push_data', views.push_data, name='push_data'),
    path('relatorio_posse_machamba', views.relatorio_posse_machamba,
         name='relatorio_posse_machamba'),
    path('relatorio_machamba_pertenca', views.relatorio_machamba_pertenca,
         name='relatorio_machamba_pertenca'),
    path('relatorio_tipo_posse', views.relatorio_tipo_posse,
         name='relatorio_tipo_posse'),
    path('relatorio_forma_aquisicao', views.relatorio_forma_aquisicao,
         name='relatorio_forma_aquisicao'),
    path('relatorio_quando_teve_machamba', views.relatorio_quando_teve_machamba,
         name='relatorio_quando_teve_machamba'),
    path('relatorio_tamanho_machamba', views.relatorio_tamanho_machamba,
         name='relatorio_tamanho_machamba'),
    path('relatorio_local_machamba', views.relatorio_local_machamba,
         name='relatorio_local_machamba'),
    path('relatorio_caracteristica_solos', views.relatorio_caracteristica_solos,
         name='relatorio_caracteristica_solos'),
    path('relatorio_cor_solo', views.relatorio_cor_solo, name='relatorio_cor_solo'),
    path('relatorio_historico_uso_solo', views.relatorio_historico_uso_solo,
         name='relatorio_historico_uso_solo'),
    path('relatorio_quando_recebeu', views.relatorio_quando_recebeu,
         name='relatorio_quando_recebeu'),
    path('relatorio_recebeu_semente', views.relatorio_recebeu_semente,
         name='relatorio_recebeu_semente'),
    path('relatorio_tipo_kit', views.relatorio_tipo_kit, name='relatorio_tipo_kit'),
    path('relatorio_de_quem_recebeu_semente', views.relatorio_de_quem_recebeu_semente,
         name='relatorio_de_quem_recebeu_semente'),
]
