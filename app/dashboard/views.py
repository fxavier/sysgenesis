from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from datetime import date
from django.db.models import Q, Count
import gspread

from django.contrib.auth.decorators import login_required

from dashboard.models import Inquerito, TipoSementeGerminou, TipoAreaGerminacao, VerificacaoSementes
from dashboard.helpers import Helpers

from dashboard.constants import Constants

service_account = gspread.service_account(filename="credentials.json")
sh = service_account.open('Inquerito_resultados')
wks = sh.worksheet('Folha1')

genero_count = Inquerito.objects.all().count()


def get_data_from_spreadsheet(worksheet: str, sheet: str):
    sh = service_account.open(worksheet)
    wks = sh.worksheet(sheet)
    return wks.get_all_records()


def refresh_inquerito_data():
    Inquerito.objects.all().delete()
    questionario = 1
    for data in get_data_from_spreadsheet("Inquerito_resultados", "Folha1"):
        inquerito = Inquerito.objects.create(
            uuid=data.get("KEY"),
            codigo_familia=data.get("data-dados_iniciais-codigo_familia"),
            data_inquerito=data.get("data-dados_iniciais-data_inquerito"),
            nome_inquiridor=data.get("data-dados_iniciais-nome_inquiridor"),
            numero_questionario=questionario,
            local_entrevista=data.get("data-dados_iniciais-local_entrevista"),
            gps_local_lat_long=data.get(
                "data-dados_iniciais-gps_local_entrevista"),
            gps_local_accuracy=data.get(
                "data-dados_iniciais-gps_local_entrevista-accuracy"),
            tipo_beneficiario=Constants().get_dicionario().get(
                str(data.get("data-identificacao_receptor-tipo_beneficiario"))),
            tipo_familia=Constants().get_dicionario().get(
                str(data.get("data-identificacao_receptor-tipo_familia"))),
            nome_agg_familiar=data.get(
                "data-identificacao_receptor-nome_agg_familiar"),
            tipo_documento=Constants().get_dicionario().get(
                str(data.get("data-identificacao_receptor-tipo_doc"))),
            documento=data.get("data-identificacao_receptor-documento"),
            photo_doc_url=data.get("data-identificacao_receptor-photo_doc"),
            data_nascimento=Helpers.formatDate(data.get(
                "data-identificacao_receptor-data_nascimento")),
            genero=Constants().get_dicionario().get(
                str(data.get("data-identificacao_receptor-genero"))),
            outro_genero=data.get("data-identificacao_receptor-outro_genero"),
            contacto=data.get("data-identificacao_receptor-contacto"),
            parte_bd=Constants().get_dicionario().get(
                str(data.get("data-identificacao_receptor-part_bd"))),
            criterios_elegib_agg_familiar=Constants().get_dicionario().get(
                str(data.get("data-identificacao_receptor-criterios_eleg_agg_familiar"))),
            provincia=Constants().get_dicionario().get(
                str(data.get("data-localizacao_agregado-provincia"))),
            distrito=Constants().get_dicionario().get(
                str(data.get("data-localizacao_agregado-distrito"))),
            posto_administrativo=Constants().get_dicionario().get(
                str(data.get("data-localizacao_agregado-posto_administrativo"))),
            localidade=Constants().get_dicionario().get(
                str(data.get("data-localizacao_agregado-localidade"))),
            comunidade=Constants().get_dicionario().get(
                str(data.get("data-localizacao_agregado-comunidade"))),
            ficha=Constants().get_dicionario().get(
                str(data.get("data-localizacao_agregado-ficha"))),
            familia_tem_machamba=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-familia_tem_machamba"))),
            machamba_familia=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-machamba_familia"))),
            tipo_posse=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-tipo_posse"))),
            outro_tipo_posse=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-outro_tipo_posse"))),
            forma_aquisicao=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-forma_aquisicao_machamba"))),
            outra_forma_aquisicao=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-outra_forma"))),
            quando_conseguiu_machamba=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-quando_conseguiu_machamba"))),
            outra_data=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-outra_data"))),
            tamanho_machamba=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-tamanho_machamba"))),
            outro_tamanho=data.get("data-alocacao_terra-outro_tamanho"),
            local_machamba=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-local_machamba"))),
            outro_local_machamba=data.get("data-alocacao_terra-outro_local"),
            caracteristica_solos=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-caracteristica_solo"))),
            outra_caracteristica_solos=data.get(
                "data-alocacao_terra-outra_caracteristica_solo"),
            cor_solo=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-cor_solo"))),
            outra_cor=data.get("data-alocacao_terra-outra_cor"),
            historico_uso_solo=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-historico_uso_terra"))),
            outro_historico_uso_solo=data.get(
                "data-alocacao_terra-outro_historico"),
            tempo_gasto_casa_machamba=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-tempo_gasto_casa_machamba"))),
            outro_tempo_gasto=data.get(
                "data-alocacao_terra-outro_tempo_gasto"),
            recebeu_semente=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-recebeu_semente"))),
            quando_recebeu=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-quando_recebeu_semente"))),
            outra_data_recebeu=data.get(
                "data-kits_para_agricultura-outra_data_recebimento"),
            identificacao_lote=data.get(
                "data-kits_para_agricultura-idntificacao_lote"),
            tipo_kit=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-tipo_kit"))),
            composicao_kit_a=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-composicao_kit_a"))),
            comentario_kit_a=data.get(
                "data-kits_para_agricultura-comentario_kit_a"),
            composicao_kit_b=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-composicao_kit_b"))),
            comentario_kit_b=data.get(
                "data-kits_para_agricultura-comentario_kit_b"),
            composicao_kit_c=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-composicao_kit_c"))),
            comentario_kit_c=data.get(
                "data-kits_para_agricultura-comentario_kit_c"),
            composicao_kit_d=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-composicao_kit_d"))),
            comentario_kit_d=data.get(
                "data-kits_para_agricultura-comentario_kit_d"),
            conservacao_semente=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-conservacao_semente"))),
            foto_semente_url=data.get(
                "data-kits_para_agricultura-foto_semente"),
            de_quem_recebeu_semente=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-de_quem_recebeu_semente"))),
            outro_de_quem_recebeu_semente=data.get(
                "data-kits_para_agricultura-outro_de_quem_recebeu"),
            quem_escolheu_kit=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-quem_escolheu_kit"))),
            outro_quem_escolheu_kit=data.get(
                "data-kits_para_agricultura-outro_quem_escolheu_kit"),
            quando_realizou_sementeira=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-quando_realizou_sementeira"))),
            familia_necess_nao_recebeu=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-fam_necess_nao_recebeu"))),
            nome_familia=data.get(
                "data-kits_para_agricultura-nome_familia_nao_recebeu"),
            sementes_germinou=Constants().get_dicionario().get(
                str(data.get("data-germinacao_semente_uso_fertilizante-sementes_germinaram"))),
            foto_sementes_germinou_url=Constants().get_dicionario().get(str(
                data.get("data-germinacao_semente_uso_fertilizante-foto_semente_germinaram"))),
            semente_nao_germinou=Constants().get_dicionario().get(str(
                data.get("data-germinacao_semente_uso_fertilizante-sementes_nao_germinaram"))),
            usou_fertilizante=Constants().get_dicionario().get(
                str(data.get("data-germinacao_semente_uso_fertilizante-usou_fertilizante"))),
            tipo_fertilizante=Constants().get_dicionario().get(
                str(data.get("data-germinacao_semente_uso_fertilizante-tipo_fertilizante"))),
            outro_tipo_fertilizante=data.get(
                "data-germinacao_semente_uso_fertilizante-outro_tipo_fertilizante"),
            momento_usou_adubo=Constants().get_dicionario().get(
                str(data.get("data-germinacao_semente_uso_fertilizante-momento_usou_adubo"))),
            outro_momento_usou_adubo=data.get(
                "data-germinacao_semente_uso_fertilizante-outro_momento_usou_adubo"),
            adubo_usado=Constants().get_dicionario().get(
                str(data.get("data-germinacao_semente_uso_fertilizante-adubo_usado"))),
            recebeu_treinamento=Constants().get_dicionario().get(
                str(data.get("data-treinamento-recebeu_treinamento"))),
            lugar_treinamento=Constants().get_dicionario().get(
                str(data.get("data-treinamento-lugar_treinamento"))),
            outro_lugar_treinamento=data.get(
                "data-treinamento-outro_lugar_treinamento"),
            de_quem_recebeu_treinamento=Constants().get_dicionario().get(
                str(data.get("data-treinamento-de_quem_recebeu_treinamento"))),
            outro_de_quem_recebeu_treinamento=data.get(
                "data-treinamento-outro_de_quem_recebeu_treinamento"),
            quando_recebeu_treinamento=Constants().get_dicionario().get(
                str(data.get("data-treinamento-quando_recebeu_treinamento"))),
            outro_quando_recebeu_treinamento=data.get(
                "data-treinamento-outro_quando_recebeu_treinamento"),
            tipo_treinamento=Constants().get_dicionario().get(
                str(data.get("data-treinamento-recebeu_tipo_treinamento"))),
            recebeu_visita_assistencia=Constants().get_dicionario().get(
                str(data.get("data-treinamento-recebeu_visita_assistencia"))),
            de_quem_recebeu_visita_assistencia=Constants().get_dicionario().get(
                str(data.get("data-treinamento-de_quem_recebeu_visita"))),
            outro_de_quem_recebeu_visita_assistencia=Constants().get_dicionario().get(
                str(data.get("data-treinamento-outro_de_quem_recebeu_visita"))),
            momento_recebeu_visita=Constants().get_dicionario().get(
                str(data.get("data-treinamento-momento_recebeu_visita"))),
            familia_nao_recebeu_treinamento=Constants().get_dicionario().get(
                str(data.get("data-treinamento-familia_nao_recebeu_treinamento"))),
            nome_familia_nao_recebeu=data.get(
                "data-treinamento-nome_familia_nao_recebeu_treinamento"),
            canais_apresentar_reclamacao=Constants().get_dicionario().get(
                str(data.get("data-reclamacoes-canais_apresentar_reclamacoes"))),
            apresentou_reclamacao=Constants().get_dicionario().get(
                str(data.get("data-reclamacoes-apresentou_reclamacao"))),
            canal_que_usou=Constants().get_dicionario().get(
                str(data.get("data-reclamacoes-canal_que_usou"))),
            outro_canal=data.get("data-reclamacoes-outro_canal"),
            tempo_gasto_resolver=Constants().get_dicionario().get(
                str(data.get("data-reclamacoes-tempo_gasto_resolver"))),
            ficou_satisfeito=Constants().get_dicionario().get(
                str(data.get("data-reclamacoes-ficou_satisfeito_solucao"))),
            ouviu_falar_vbg=Constants().get_dicionario().get(
                str(data.get("data-vbg-ouviu_falar_vbg"))),
            ja_foi_vitima_vbg=Constants().get_dicionario().get(
                str(data.get("data-vbg-ja_foi_vitima_vbg"))),
            canais_denunciar_vbg=Constants().get_dicionario().get(
                str(data.get("data-vbg-canais_denunciar_vbg"))),
            outro_canal_denuncia=data.get("data-vbg-outro_canal_denuncia"),
            teve_toda_assistencia=Constants().get_dicionario().get(
                str(data.get("data-vbg-teve_toda_assistencia"))),
            e_comum_vbg_comunidade=Constants().get_dicionario().get(
                str(data.get("data-vbg-e_comum_vbg_comunidade"))),
            casos_vbg_ouviu_falar=Constants().get_dicionario().get(
                str(data.get("data-vbg-casos_vbg_ouviu_falar"))),
            outro_caso_vbg_ouviu_falar=data.get(
                "data-vbg-outro_caso_vbg_ouviu_falar"),
            foto_caso_vbg_url=data.get("data-vbg-foto_caso_vbg")

        )
        questionario += 1
        inquerito.save()

    TipoSementeGerminou.objects.all().delete()
    for data in get_data_from_spreadsheet("Inquerito_resultados", "data-germinacao_semente_uso_fertilizante-germinacao_semente_repeat"):
        tipo_semente_germinou = TipoSementeGerminou.objects.create(
            uuid=data.get("KEY"),
            nome_semente=Constants().get_dicionario().get(str(data.get(
                "data-germinacao_semente_uso_fertilizante-germinacao_semente_repeat-tipo_semente_germinou"))),
            tempo_germinacao=Constants().get_dicionario().get(str(data.get(
                "data-germinacao_semente_uso_fertilizante-germinacao_semente_repeat-tempo_germinacao"))),
            parent_key=data.get("PARENT_KEY")
        )

        tipo_semente_germinou.save()
    TipoAreaGerminacao.objects.all().delete()
    for data in get_data_from_spreadsheet("Inquerito_resultados", "data-germinacao_semente_uso_fertilizante-tipo_area_de_germinacao"):
        tipo_area_de_germinacao = TipoAreaGerminacao.objects.create(
            uuid=data.get("KEY"),
            nome_semente=Constants().get_dicionario().get(str(data.get(
                "data-germinacao_semente_uso_fertilizante-tipo_area_de_germinacao-tipo_semente_germinou_area"))),
            area=Constants().get_dicionario().get(str(data.get(
                "data-germinacao_semente_uso_fertilizante-tipo_area_de_germinacao-tamanho_area_germinou"))),
            parent_key=data.get("PARENT_KEY")
        )

        tipo_area_de_germinacao.save()


def refresh_verificacao_semente_data():
    VerificacaoSementes.objects.all().delete()
    for data in get_data_from_spreadsheet("Ficha_verificacao_sementes", "Sheet1"):
        verificacao_semente = VerificacaoSementes.objects.create(
            data=data.get("data-apresentacao-data"),
            horas=data.get("data-apresentacao-horas"),
            provincia=data.get("data-apresentacao-provincia"),
            distrito=data.get("data-apresentacao-distrito"),
            posto_administrativo=data.get("data-apresentacao-posto_admin"),
            localidade=data.get("data-apresentacao-localidade"),
            comunidade=data.get("data-apresentacao-comunidade"),
            aldeia=data.get("data-apresentacao-aldeia"),
            local_especifico=data.get("data-apresentacao-local_especifico"),
            responsavel_local=data.get("data-apresentacao-responsavel_local"),
            contacto=data.get("data-apresentacao-contacto"),
            sementes_certificadas=Constants().get_numeros().get(
                str(data.get("data-sementes-sementes_certificadas"))),
            observacao1=data.get("data-sementes-observacao1"),
            foto1_url=data.get("data-sementes-foto1"),
            certificados_dentro_prazo=Constants().get_numeros().get(
                str(data.get("data-sementes-certificados_dentro_prazo"))),
            observacao2=data.get("data-sementes-observacao2"),
            foto2_url=data.get("data-sementes-foto2"),
            sementes_etiquetas=Constants().get_numeros().get(
                str(data.get("data-sementes-ementes_etiquetas"))),
            observacao3=data.get("data-sementes-observacao3"),
            foto3_url=data.get("data-sementes-foto3"),
            etiquetas_resistentes=Constants().get_numeros().get(
                str(data.get("data-sementes-etiquetas_resistente"))),
            observacao4=data.get("data-sementes-observacao4"),
            foto4_url=data.get("data-sementes-foto4"),
            etiquetas_duplicadas=Constants().get_numeros().get(
                str(data.get("data-sementes-etiquetas_duplicadas"))),
            observacao5=data.get("data-sementes-observacao5"),
            foto5_url=data.get("data-sementes-foto5"),
            pureza_dentro_padroes=Constants().get_numeros().get(
                str(data.get("data-sementes-pureza_dentro_padroes"))),
            observacao6=data.get("data-sementes-observacao6"),
            foto6_url=data.get("data-sementes-foto6"),
            semente_transportada_condicoes=Constants().get_numeros().get(
                str(data.get("data-sementes-semente_transportada_condicoes"))),
            observacao7=data.get("data-sementes-observacao6"),
            foto7_url=data.get("data-sementes-foto6"),
            sementes_armazenadas_condicoes=Constants().get_numeros().get(
                str(data.get("data-sementes-sementes_armazenadas_condicoes"))),
            observacao8=data.get("data-sementes-observacao8"),
            foto8_url=data.get("data-sementes-foto8"),
            embalagens_tem_info=data.get("data-sementes-embalagens_tem_info"),
            observacao9=data.get("data-sementes-observacao9"),
            foto9_url=data.get("data-sementes-foto9"),
            sementes_tratadas_produto_quimico=data.get(
                "data-sementes-sementes_tratadas_produto_quimico"),
            observacao10=data.get("data-sementes-observacao10"),
            foto10_url=data.get("data-sementes-foto10"),
            embalagem_selada=Constants().get_numeros().get(
                str(data.get("data-sementes-embalagem_selada"))),
            observacao11=data.get("data-sementes-observacao11"),
            foto11_url=data.get("data-sementes-foto11"),
            etiquetas_classificadas=data.get(
                "data-sementes-etiquetas_classificadas"),
            observacao12=data.get("data-sementes-observacao12"),
            foto12_url=data.get("data-sementes-foto12")

        )

        verificacao_semente.save()
        if len(str(verificacao_semente.embalagens_tem_info)) == 37:
            verificacao_semente.embalagens_tem_info = "Embalagem com toda informacao"
            verificacao_semente.save()
        if len(str(verificacao_semente.sementes_tratadas_produto_quimico)) == 10:
            verificacao_semente.sementes_tratadas_produto_quimico = "As sementes foram tratadas com algum produto químico e a embalagem apresenta todas informações"
            verificacao_semente.save()

        if len(str(verificacao_semente.etiquetas_classificadas)) == 14:
            verificacao_semente.etiquetas_classificadas = "As etiquetas estão classificadas de todas as 4 formas"
            verificacao_semente.save()


@login_required(login_url="users:login")
def push_data(request):
    refresh_inquerito_data()
    # return HttpResponse("Data added")
    return render(request, 'dashboard/home.html')


@login_required(login_url="users:login")
def home(request):
    inquerito_count = Inquerito.objects.all().count()
    inquerito_nampula = Inquerito.objects.filter(provincia='Nampula').count()
    inquerito_cabo_delgado = Inquerito.objects.filter(
        provincia='Cabo Delgado').count()
    context = {
        'inquerito_count': inquerito_count,
        'inquerito_cabo_delgado': inquerito_cabo_delgado,
        'inquerito_nampula': inquerito_nampula
    }
    return render(request, 'dashboard/home.html', context)


def relatorio_posse_machamba(request):
    labels = []
    data = []
    tem_machamba = Inquerito.objects.values(
        'familia_tem_machamba').annotate(Count('uuid')).exclude(familia_tem_machamba=None)
    m_labels = [d['familia_tem_machamba'] for d in tem_machamba]
    m_data = [d['uuid__count'] for d in tem_machamba]
    for l in m_labels:
        labels.append(l)
    for d in m_data:
        data.append(d)
    data_json = {'data': data, 'labels': labels}
    return JsonResponse(data_json)


def relatorio_machamba_pertenca(request):
    labels = []
    data = []
    pertence = Inquerito.objects.values(
        'machamba_familia').annotate(Count('uuid')).exclude(machamba_familia=None)
    p_labels = [d['machamba_familia'] for d in pertence]
    p_data = [d['uuid__count'] for d in pertence]
    for x in p_labels:
        labels.append(x)
    for y in p_data:
        data.append(y)
    data_json = {'data': data, 'labels': labels}
    return JsonResponse(data_json)


def relatorio_tipo_posse(request):
    labels = []
    data = []
    tipo_posse = Inquerito.objects.values('tipo_posse').annotate(
        Count('uuid')).exclude(tipo_posse=None)
    t_labels = [d['tipo_posse'] for d in tipo_posse]
    t_data = [d['uuid__count'] for d in tipo_posse]
    for x in t_labels:
        labels.append(x)
    for y in t_data:
        data.append(y)
    data_json = {'data': data, 'labels': labels}
    return JsonResponse(data_json)


def relatorio_forma_aquisicao(request):
    labels = []
    data = []
    forma_aquisicao = Inquerito.objects.values('forma_aquisicao').annotate(
        Count('uuid')).exclude(forma_aquisicao=None)
    f_labels = [d['forma_aquisicao'] for d in forma_aquisicao]
    f_data = [d['uuid__count'] for d in forma_aquisicao]
    for x in f_labels:
        labels.append(x)
    for y in f_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_quando_teve_machamba(request):
    labels = []
    data = []
    quando_conseguiu_machamba = Inquerito.objects.values('quando_conseguiu_machamba').annotate(
        Count('uuid')).exclude(quando_conseguiu_machamba=None)
    q_labels = [d['quando_conseguiu_machamba']
                for d in quando_conseguiu_machamba]
    q_data = [d['uuid__count'] for d in quando_conseguiu_machamba]
    for x in q_labels:
        labels.append(x)
    for y in q_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_tamanho_machamba(request):
    labels = []
    data = []
    tamanho_machamba = Inquerito.objects.values('tamanho_machamba').annotate(
        Count('uuid')).exclude(tamanho_machamba=None)
    ta_labels = [d['tamanho_machamba'] for d in tamanho_machamba]
    ta_data = [float('{:.2f}'.format(d['uuid__count'] / genero_count * 100))
               for d in tamanho_machamba]
    for x in ta_labels:
        labels.append(x)
    for y in ta_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_local_machamba(request):
    labels = []
    data = []
    local_machamba = Inquerito.objects.values('local_machamba').annotate(
        Count('uuid')).exclude(local_machamba=None)
    l_labels = [d['local_machamba'] for d in local_machamba]
    l_data = [float('{:.2f}'.format(d['uuid__count'] / genero_count * 100))
              for d in local_machamba]
    for x in l_labels:
        labels.append(x)
    for y in l_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_caracteristica_solos(request):
    labels = []
    data = []
    caracteristica_solos = Inquerito.objects.values('caracteristica_solos').annotate(
        Count('uuid')).exclude(caracteristica_solos=None)
    c_labels = [d['caracteristica_solos'] for d in caracteristica_solos]
    c_data = [d['uuid__count'] for d in caracteristica_solos]
    for x in c_labels:
        labels.append(x)
    for y in c_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_cor_solo(request):
    labels = []
    data = []
    cor_solo = Inquerito.objects.values('cor_solo').annotate(
        Count('uuid')).exclude(cor_solo=None)
    cs_label = [d['cor_solo'] for d in cor_solo]
    cs_data = [float('{:.2f}'.format(d['uuid__count'] /
                     genero_count * 100)) for d in cor_solo]
    for x in cs_label:
        labels.append(x)
    for y in cs_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_historico_uso_solo(request):
    labels = []
    data = []
    historico_uso_solo = Inquerito.objects.values('historico_uso_solo').annotate(
        Count('uuid')).exclude(historico_uso_solo=None)
    h_label = [d['historico_uso_solo'] for d in historico_uso_solo]
    h_data = [d['uuid__count'] for d in historico_uso_solo]
    for x in h_label:
        labels.append(x)
    for y in h_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_recebeu_semente(request):
    labels = []
    data = []
    recebeu_semente = Inquerito.objects.values('recebeu_semente').annotate(
        Count('uuid')).exclude(recebeu_semente=None)
    s_label = [d['recebeu_semente'] for d in recebeu_semente]
    s_data = [float('{:.2f}'.format(d['uuid__count'] / genero_count * 100))
              for d in recebeu_semente]
    for x in s_label:
        labels.append(x)
    for y in s_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_quando_recebeu(request):
    labels = []
    data = []
    quando_recebeu = Inquerito.objects.values('quando_recebeu').annotate(
        Count('uuid')).exclude(quando_recebeu=None)
    q_label = [d['quando_recebeu'] for d in quando_recebeu]
    q_data = [d['uuid__count'] for d in quando_recebeu]
    for x in q_label:
        labels.append(x)
    for y in q_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_tipo_kit(request):
    labels = []
    data = []
    tipo_kit = Inquerito.objects.values('tipo_kit').annotate(
        Count('uuid')).exclude(tipo_kit=None)
    k_label = [d['tipo_kit'] for d in tipo_kit]
    k_data = [d['uuid__count'] for d in tipo_kit]
    for x in k_label:
        labels.append(x)
    for y in k_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_de_quem_recebeu_semente(request):
    labels = []
    data = []
    recebeu_count = Inquerito.objects.filter(recebeu_semente='Sim').count()
    de_quem_recebeu_semente = Inquerito.objects.values('de_quem_recebeu_semente').annotate(
        Count('uuid')).exclude(de_quem_recebeu_semente=None)
    d_label = [d['de_quem_recebeu_semente'] for d in de_quem_recebeu_semente]
    d_data = [float('{:.2f}'.format(d['uuid__count'] / recebeu_count * 100))
              for d in de_quem_recebeu_semente]
    for x in d_label:
        # if x == None:
        #     x = 'Outro'
        labels.append(x)
    for y in d_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_tipo_familia(request):
    labels = []
    data = []
    tipo_familia = Inquerito.objects.values('tipo_familia').annotate(
        Count('uuid')).exclude(tipo_familia=None)
    k_label = [d['tipo_familia'] for d in tipo_familia]
    k_data = [float('{:.2f}'.format(d['uuid__count'] / genero_count * 100))
              for d in tipo_familia]
    for x in k_label:
        labels.append(x)
    for y in k_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_genero(request):
    labels = []
    data = []

    genero = Inquerito.objects.values('genero').annotate(
        Count('uuid')).exclude(genero=None)
    g_label = [d['genero'] for d in genero]
    g_data = [float('{:.2f}'.format(d['uuid__count'] / genero_count * 100))
              for d in genero]
    for x in g_label:
        labels.append(x)
    for y in g_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_elegibilidade(request):
    labels = []
    data = []
    elegibilidade = Inquerito.objects.values('criterios_elegib_agg_familiar').annotate(
        Count('uuid')).exclude(criterios_elegib_agg_familiar=None)
    e_label = [d['criterios_elegib_agg_familiar']
               for d in elegibilidade]
    e_data = [d['uuid__count'] for d in elegibilidade]
    for x in e_label:
        labels.append(x)
    for y in e_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_comunidade(request):
    labels = []
    data = []
    comunidade = Inquerito.objects.values('comunidade').annotate(
        Count('uuid')).exclude(comunidade=None)
    c_label = [d['comunidade'] for d in comunidade]
    c_data = [d['uuid__count'] for d in comunidade]
    for x in c_label:
        labels.append(x)
    for y in c_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_quando_realizou_sementeira(request):
    labels = []
    data = []
    recebeu_count = Inquerito.objects.filter(recebeu_semente='Sim').count()
    quando_realizou_sementeira = Inquerito.objects.values('quando_realizou_sementeira').annotate(
        Count('uuid')).exclude(quando_realizou_sementeira=None)
    s_label = [d['quando_realizou_sementeira']
               for d in quando_realizou_sementeira]
    s_data = [float('{:.2f}'.format(d['uuid__count'] / recebeu_count * 100))
              for d in quando_realizou_sementeira]
    for x in s_label:
        labels.append(x)
    for y in s_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_sementes_germinou(request):
    labels = []
    data = []
    sementes_germinou = Inquerito.objects.values('sementes_germinou').annotate(
        Count('uuid')).exclude(sementes_germinou=None)
    sg_label = [d['sementes_germinou'] for d in sementes_germinou]
    sg_data = [d['uuid__count'] for d in sementes_germinou]
    for x in sg_label:
        labels.append(x)
    for y in sg_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_canais_reclamacao(request):
    labels = []
    data = []

    canais_reclamacao = Inquerito.objects.values('canais_apresentar_reclamacao').annotate(
        Count('uuid')).exclude(canais_apresentar_reclamacao=None)
    r_labels = [d['canais_apresentar_reclamacao'] for d in canais_reclamacao]
    r_data = [d['uuid__count'] for d in canais_reclamacao]
    for x in r_labels:
        labels.append(x)
    for y in r_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_semente_nao_germinou(request):
    labels = []
    data = []
    semente_nao_germinou = Inquerito.objects.values('semente_nao_germinou').annotate(
        Count('uuid')).exclude(semente_nao_germinou=None)
    n_label = [d['semente_nao_germinou'] for d in semente_nao_germinou]
    n_data = [d['uuid__count'] for d in semente_nao_germinou]
    for x in n_label:
        labels.append(x)
    for y in n_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_apresentou_reclamacao(request):
    labels = []
    data = []
    apresentou_reclamacao = Inquerito.objects.values('apresentou_reclamacao').annotate(
        Count('uuid')).exclude(apresentou_reclamacao=None)
    label = [d['apresentou_reclamacao'] for d in apresentou_reclamacao]
    datas = [float('{:.2f}'.format(d['uuid__count'] / genero_count * 100))
             for d in apresentou_reclamacao]
    for x in label:
        labels.append(x)
    for y in datas:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_canal_usado(request):
    labels = []
    data = []
    apresentou_count = Inquerito.objects.filter(
        apresentou_reclamacao='Sim').count()
    canal_usado = Inquerito.objects.values('canal_que_usou').annotate(
        Count('uuid')).exclude(canal_que_usou=None)
    u_label = [d['canal_que_usou'] for d in canal_usado]
    u_data = [float('{:.2f}'.format(d['uuid__count'] / apresentou_count * 100))
              for d in canal_usado]
    for x in u_label:
        labels.append(x)
    for y in u_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_tempo_gasto_resolver(request):
    labels = []
    data = []
    apresentou_count = Inquerito.objects.filter(
        apresentou_reclamacao='Sim').count()
    tempo_gasto = Inquerito.objects.values('tempo_gasto_resolver').annotate(
        Count('uuid')).exclude(tempo_gasto_resolver=None)
    t_label = [d['tempo_gasto_resolver'] for d in tempo_gasto]
    t_data = [float('{:.2f}'.format(d['uuid__count'] / apresentou_count * 100))
              for d in tempo_gasto]
    for x in t_label:
        labels.append(x)
    for y in t_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_ficou_satisfeito(request):
    labels = []
    data = []
    apresentou_count = Inquerito.objects.filter(
        apresentou_reclamacao='Sim').count()
    satisfeito = Inquerito.objects.values('ficou_satisfeito').annotate(
        Count('uuid')).exclude(ficou_satisfeito=None)
    s_label = [d['ficou_satisfeito'] for d in satisfeito]
    s_data = [float('{:.2f}'.format(d['uuid__count'] / apresentou_count * 100))
              for d in satisfeito]
    for x in s_label:
        labels.append(x)
    for y in s_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_ja_ouviu_vbg(request):
    labels = []
    data = []
    vbg = Inquerito.objects.values('ouviu_falar_vbg').annotate(
        Count('uuid')).exclude(ouviu_falar_vbg=None)
    v_label = [d['ouviu_falar_vbg'] for d in vbg]
    v_data = [float('{:.2f}'.format(d['uuid__count'] /
                    genero_count * 100)) for d in vbg]
    for x in v_label:
        labels.append(x)
    for y in v_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_vitima_vbg(request):
    labels = []
    data = []
    ouviu_count = Inquerito.objects.filter(ouviu_falar_vbg='Sim').count()
    vitima = Inquerito.objects.values('ja_foi_vitima_vbg').annotate(
        Count('uuid')).exclude(ja_foi_vitima_vbg=None)
    v_label = [d['ja_foi_vitima_vbg'] for d in vitima]
    v_data = [float('{:.2f}'.format(d['uuid__count'] /
                    ouviu_count * 100)) for d in vitima]
    for x in v_label:
        labels.append(x)
    for y in v_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_canais_denunciar(request):
    labels = []
    data = []
    denunciar = Inquerito.objects.values('canais_denunciar_vbg').annotate(
        Count('uuid')).exclude(canais_denunciar_vbg=None)
    d_label = [d['canais_denunciar_vbg'] for d in denunciar]
    d_data = [d['uuid__count'] for d in denunciar]
    for x in d_label:
        labels.append(x)
    for y in d_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_teve_toda_assistencia(request):
    labels = []
    data = []
    assistencia = Inquerito.objects.values('teve_toda_assistencia').annotate(
        Count('uuid')).exclude(teve_toda_assistencia=None)
    a_label = [d['teve_toda_assistencia'] for d in assistencia]
    a_data = [float('{:.2f}'.format(d['uuid__count'] / genero_count * 100))
              for d in assistencia]
    for x in a_label:
        labels.append(x)
    for y in a_data:
        data.append(y)

    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


def relatorio_tipo_vbg(request):
    labels = []
    data = []
    tipo_vbg = Inquerito.objects.values('casos_vbg_ouviu_falar').annotate(
        Count('uuid')).exclude(casos_vbg_ouviu_falar=None)
    v_label = [d['casos_vbg_ouviu_falar'] for d in tipo_vbg]
    v_data = [d['uuid__count'] for d in tipo_vbg]
    for x in v_label:
        labels.append(x)
    for y in v_data:
        data.append(y)
    json_data = {'data': data, 'labels': labels}
    return JsonResponse(json_data)


@login_required(login_url="login")
def index(request):
    machamba_label = []
    machamba_data = []
    inqueritos = Inquerito.objects.all()
    inqueritos_count = Inquerito.objects.all().count()
    inquerito_nampula = Inquerito.objects.filter(provincia="Nampula").count()
    inquerito_cabo_delgado = Inquerito.objects.filter(
        provincia="Cabo Delgado").count()
    ficha_verificacao = VerificacaoSementes.objects.all().count()
    tem_machamba = Inquerito.objects.values('familia_tem_machamba').annotate(
        Count('uuid'))  # Inquerito.objects.filter(familia_tem_machamba='Sim').count()
    tem_machamba_labels = [d['familia_tem_machamba'] for d in tem_machamba]
    tem_machamba_values = [d['uuid__count'] for d in tem_machamba]
    machamba_label.append(tem_machamba_labels)
    machamba_data.append(tem_machamba_values)
    nao_tem_machamba = Inquerito.objects.filter(
        familia_tem_machamba='Nao').count()
    machamba_familia_sim = Inquerito.objects.filter(
        machamba_familia="Sim").count()
    machamba_familia_nao = Inquerito.objects.filter(
        machamba_familia="Nao").count()
    emprestada = Inquerito.objects.filter(tipo_posse='Emprestada').count()
    alugada = Inquerito.objects.filter(tipo_posse='Alugada').count()
    outro = Inquerito.objects.filter(tipo_posse='Outro').count()
    comprou = Inquerito.objects.filter(forma_aquisicao='Comprou').count()
    alugada_f = Inquerito.objects.filter(forma_aquisicao='Alugada').count()
    cedido_lider = Inquerito.objects.filter(
        forma_aquisicao='Cedido Pelo Lider').count()
    cedido_governo = Inquerito.objects.filter(
        forma_aquisicao='Cedido Pelo Governo').count()
    outra_forma = Inquerito.objects.filter(forma_aquisicao='Outro').count()
    tamanho_machamba_05 = Inquerito.objects.filter(
        tamanho_machamba='0,5 ha').count()
    tamanho_machamba_15 = Inquerito.objects.filter(
        tamanho_machamba='1,5 ha').count()
    outro_tamanho = Inquerito.objects.filter(tamanho_machamba='Outro').count()
    zona_alta = Inquerito.objects.filter(local_machamba='Zona alta').count()
    zona_baixa = Inquerito.objects.filter(local_machamba='Zona baixa').count()
    pantano = Inquerito.objects.filter(local_machamba='Pantano').count()
    outra_zona = Inquerito.objects.filter(local_machamba='Outro').count()
    arenoso = Inquerito.objects.filter(caracteristica_solos='Arenoso').count()
    argiloso = Inquerito.objects.filter(
        caracteristica_solos='Argiloso').count()
    areno_argiloso = Inquerito.objects.filter(
        caracteristica_solos='Areno Argiloso').count()
    outra_caracteristica = Inquerito.objects.filter(
        caracteristica_solos='Outro').count()
    preto = Inquerito.objects.filter(cor_solo='Preto').count()
    castanho = Inquerito.objects.filter(cor_solo='Castanho').count()
    outra_cor = Inquerito.objects.filter(cor_solo='Outra').count()
    uso = Inquerito.objects.filter(historico_uso_solo='Em Uso').count()
    pousio = Inquerito.objects.filter(historico_uso_solo='Em Pousio').count()
    virgem = Inquerito.objects.filter(historico_uso_solo='Virgem').count()
    outro_historico = Inquerito.objects.filter(
        historico_uso_solo='Outro').count()
    menor_15 = Inquerito.objects.filter(
        tempo_gasto_casa_machamba='Menor ou igual a 15 Minutos').count()
    tempo_15_45 = Inquerito.objects.filter(
        tempo_gasto_casa_machamba='15 a 45 Minutos').count()
    tempo_45_1 = Inquerito.objects.filter(
        tempo_gasto_casa_machamba='45 Minutos a 1 hora"').count()
    mais_1_hora = Inquerito.objects.filter(
        tempo_gasto_casa_machamba='Mais que 1 hora').count()
    outro_tempo = Inquerito.objects.filter(
        tempo_gasto_casa_machamba='Outro').count()

    context = {'inqueritos_count': inqueritos_count, 'inquerito_nampula': inquerito_nampula,
               'inquerito_cabo_delgado': inquerito_cabo_delgado,
               'ficha_verificacao': ficha_verificacao, 'tem_machamba': tem_machamba,
               'nao_tem_machamba': nao_tem_machamba, 'machamba_familia_sim': machamba_familia_sim,
               'machamba_familia_nao': machamba_familia_nao, 'emprestada': emprestada,
               'alugada': alugada, 'outro': outro, 'alugada_f': alugada_f, 'cedido_lider': cedido_lider,
               'cedido_governo': cedido_governo, 'outra_forma': outra_forma, 'comprou': comprou,
               'tamanho_machamba_05': tamanho_machamba_05, 'tamanho_machamba_15': tamanho_machamba_15,
               'outro_tamanho': outro_tamanho, 'zona_baixa': zona_baixa, 'zona_alta': zona_alta,
               'pantano': pantano, 'outra_zona': outra_zona, 'arenoso': arenoso, 'argiloso': argiloso,
               'areno_argiloso': areno_argiloso, 'outra_caracteristica': outra_caracteristica,
               'preto': preto, 'castanho': castanho, 'outra_cor': outra_cor, 'uso': uso, 'pousio': pousio,
               'virgem': virgem, 'outro_historico': outro_historico, 'menor_15': menor_15, 'tempo_15_45': tempo_15_45,
               'tempo_45_1': tempo_45_1, 'mais_1_hora': mais_1_hora, 'outro_tempo': outro_tempo,
               'inqueritos': inqueritos, 'tem_machamba_labels': tem_machamba_labels, 'tem_machamba_values': tem_machamba_values,
               'machamba_label': machamba_label, 'machamba_data': machamba_data
               }

    return render(request, 'dashboard/index.html', context)
