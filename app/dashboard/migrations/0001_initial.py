# Generated by Django 4.0.2 on 2022-02-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inquerito',
            fields=[
                ('uuid', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('codigo_familia', models.CharField(max_length=255)),
                ('data_inquerito', models.DateField()),
                ('nome_inquiridor', models.CharField(max_length=255)),
                ('numero_questionario', models.IntegerField(default=0)),
                ('local_entrevista', models.CharField(max_length=255)),
                ('gps_local_lat_long', models.CharField(max_length=255)),
                ('gps_local_accuracy', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_beneficiario', models.CharField(max_length=255)),
                ('tipo_familia', models.CharField(max_length=255)),
                ('nome_agg_familiar', models.CharField(max_length=255)),
                ('tipo_documento', models.CharField(max_length=255)),
                ('documento', models.CharField(max_length=255)),
                ('photo_doc_url', models.CharField(blank=True, max_length=255, null=True)),
                ('data_nascimento', models.DateField()),
                ('genero', models.CharField(max_length=255)),
                ('outro_genero', models.CharField(max_length=255)),
                ('contacto', models.CharField(max_length=255)),
                ('parte_bd', models.CharField(max_length=20)),
                ('criterios_elegib_agg_familiar', models.CharField(max_length=255)),
                ('provincia', models.CharField(blank=True, max_length=255, null=True)),
                ('distrito', models.CharField(blank=True, max_length=255, null=True)),
                ('posto_administrativo', models.CharField(blank=True, max_length=255, null=True)),
                ('localidade', models.CharField(blank=True, max_length=255, null=True)),
                ('comunidade', models.CharField(blank=True, max_length=255, null=True)),
                ('ficha', models.CharField(max_length=255)),
                ('familia_tem_machamba', models.CharField(blank=True, max_length=255, null=True)),
                ('machamba_familia', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_posse', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_tipo_posse', models.CharField(blank=True, max_length=255, null=True)),
                ('forma_aquisicao', models.CharField(blank=True, max_length=255, null=True)),
                ('outra_forma_aquisicao', models.CharField(blank=True, max_length=255, null=True)),
                ('quando_conseguiu_machamba', models.CharField(blank=True, max_length=255, null=True)),
                ('outra_data', models.CharField(blank=True, max_length=255, null=True)),
                ('tamanho_machamba', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_tamanho', models.CharField(blank=True, max_length=255, null=True)),
                ('local_machamba', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_local_machamba', models.CharField(blank=True, max_length=255, null=True)),
                ('caracteristica_solos', models.CharField(blank=True, max_length=255, null=True)),
                ('outra_caracteristica_solos', models.CharField(blank=True, max_length=255, null=True)),
                ('cor_solo', models.CharField(blank=True, max_length=255, null=True)),
                ('outra_cor', models.CharField(blank=True, max_length=255, null=True)),
                ('historico_uso_solo', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_historico_uso_solo', models.CharField(blank=True, max_length=255, null=True)),
                ('tempo_gasto_casa_machamba', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_tempo_gasto', models.CharField(blank=True, max_length=255, null=True)),
                ('recebeu_semente', models.CharField(blank=True, max_length=255, null=True)),
                ('quando_recebeu', models.CharField(blank=True, max_length=255, null=True)),
                ('outra_data_recebeu', models.CharField(blank=True, max_length=255, null=True)),
                ('identificacao_lote', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_kit', models.CharField(blank=True, max_length=255, null=True)),
                ('composicao_kit_a', models.CharField(blank=True, max_length=255, null=True)),
                ('comentario_kit_a', models.CharField(blank=True, max_length=255, null=True)),
                ('composicao_kit_b', models.CharField(blank=True, max_length=255, null=True)),
                ('comentario_kit_b', models.CharField(blank=True, max_length=255, null=True)),
                ('composicao_kit_c', models.CharField(blank=True, max_length=255, null=True)),
                ('comentario_kit_c', models.CharField(blank=True, max_length=255, null=True)),
                ('composicao_kit_d', models.CharField(blank=True, max_length=255, null=True)),
                ('comentario_kit_d', models.CharField(blank=True, max_length=255, null=True)),
                ('conservacao_semente', models.CharField(blank=True, max_length=255, null=True)),
                ('foto_semente_url', models.CharField(blank=True, max_length=255, null=True)),
                ('de_quem_recebeu_semente', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_de_quem_recebeu_semente', models.CharField(blank=True, max_length=255, null=True)),
                ('quem_escolheu_kit', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_quem_escolheu_kit', models.CharField(blank=True, max_length=255, null=True)),
                ('quando_realizou_sementeira', models.CharField(blank=True, max_length=255, null=True)),
                ('familia_necess_nao_recebeu', models.CharField(blank=True, max_length=255, null=True)),
                ('nome_familia', models.CharField(blank=True, max_length=255, null=True)),
                ('sementes_germinou', models.CharField(blank=True, max_length=255, null=True)),
                ('foto_sementes_germinou_url', models.CharField(blank=True, max_length=255, null=True)),
                ('semente_nao_germinou', models.CharField(blank=True, max_length=255, null=True)),
                ('usou_fertilizante', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_fertilizante', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_tipo_fertilizante', models.CharField(blank=True, max_length=255, null=True)),
                ('momento_usou_adubo', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_momento_usou_adubo', models.CharField(blank=True, max_length=255, null=True)),
                ('adubo_usado', models.CharField(blank=True, max_length=255, null=True)),
                ('recebeu_treinamento', models.CharField(blank=True, max_length=255, null=True)),
                ('lugar_treinamento', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_lugar_treinamento', models.CharField(blank=True, max_length=255, null=True)),
                ('de_quem_recebeu_treinamento', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_de_quem_recebeu_treinamento', models.CharField(blank=True, max_length=255, null=True)),
                ('quando_recebeu_treinamento', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_quando_recebeu_treinamento', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_treinamento', models.CharField(blank=True, max_length=255, null=True)),
                ('recebeu_visita_assistencia', models.CharField(blank=True, max_length=255, null=True)),
                ('de_quem_recebeu_visita_assistencia', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_de_quem_recebeu_visita_assistencia', models.CharField(blank=True, max_length=255, null=True)),
                ('momento_recebeu_visita', models.CharField(blank=True, max_length=255, null=True)),
                ('familia_nao_recebeu_treinamento', models.CharField(blank=True, max_length=255, null=True)),
                ('nome_familia_nao_recebeu', models.CharField(blank=True, max_length=255, null=True)),
                ('canais_apresentar_reclamacao', models.CharField(blank=True, max_length=255, null=True)),
                ('apresentou_reclamacao', models.CharField(blank=True, max_length=255, null=True)),
                ('canal_que_usou', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_canal', models.CharField(blank=True, max_length=255, null=True)),
                ('tempo_gasto_resolver', models.CharField(blank=True, max_length=255, null=True)),
                ('ficou_satisfeito', models.CharField(blank=True, max_length=255, null=True)),
                ('ouviu_falar_vbg', models.CharField(blank=True, max_length=255, null=True)),
                ('ja_foi_vitima_vbg', models.CharField(blank=True, max_length=255, null=True)),
                ('canais_denunciar_vbg', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_canal_denuncia', models.CharField(blank=True, max_length=255, null=True)),
                ('teve_toda_assistencia', models.CharField(blank=True, max_length=255, null=True)),
                ('e_comum_vbg_comunidade', models.CharField(blank=True, max_length=255, null=True)),
                ('casos_vbg_ouviu_falar', models.CharField(blank=True, max_length=255, null=True)),
                ('outro_caso_vbg_ouviu_falar', models.CharField(blank=True, max_length=255, null=True)),
                ('foto_caso_vbg_url', models.CharField(blank=True, max_length=255, null=True)),
                ('comentario_geral', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RowControl',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('last_row', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TipoAreaGerminacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=255, null=True)),
                ('nome_semente', models.CharField(blank=True, max_length=100, null=True)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_key', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSementeGerminou',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=255, null=True)),
                ('nome_semente', models.CharField(blank=True, max_length=100, null=True)),
                ('tempo_germinacao', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_key', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VerificacaoSementes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horas', models.TimeField()),
                ('provincia', models.CharField(max_length=255)),
                ('distrito', models.CharField(max_length=255)),
                ('posto_administrativo', models.CharField(max_length=255)),
                ('localidade', models.CharField(max_length=255)),
                ('comunidade', models.CharField(max_length=255)),
                ('aldeia', models.CharField(max_length=255)),
                ('local_especifico', models.CharField(max_length=255)),
                ('responsavel_local', models.CharField(max_length=255)),
                ('contacto', models.CharField(max_length=255)),
                ('sementes_certificadas', models.CharField(blank=True, max_length=10, null=True)),
                ('observacao1', models.CharField(blank=True, max_length=255, null=True)),
                ('foto1_url', models.CharField(blank=True, max_length=255, null=True)),
                ('certificados_dentro_prazo', models.CharField(blank=True, max_length=10, null=True)),
                ('observacao2', models.CharField(blank=True, max_length=255, null=True)),
                ('foto2_url', models.CharField(blank=True, max_length=255, null=True)),
                ('sementes_etiquetas', models.CharField(blank=True, max_length=10, null=True)),
                ('observacao3', models.CharField(blank=True, max_length=255, null=True)),
                ('foto3_url', models.CharField(blank=True, max_length=255, null=True)),
                ('etiquetas_resistentes', models.CharField(blank=True, max_length=10, null=True)),
                ('observacao4', models.CharField(blank=True, max_length=255, null=True)),
                ('foto4_url', models.CharField(blank=True, max_length=255, null=True)),
                ('etiquetas_duplicadas', models.CharField(blank=True, max_length=10, null=True)),
                ('observacao5', models.CharField(blank=True, max_length=255, null=True)),
                ('foto5_url', models.CharField(blank=True, max_length=255, null=True)),
                ('pureza_dentro_padroes', models.CharField(blank=True, max_length=10, null=True)),
                ('observacao6', models.CharField(blank=True, max_length=255, null=True)),
                ('foto6_url', models.CharField(blank=True, max_length=255, null=True)),
                ('semente_transportada_condicoes', models.CharField(blank=True, max_length=10, null=True)),
                ('observacao7', models.CharField(blank=True, max_length=255, null=True)),
                ('foto7_url', models.CharField(blank=True, max_length=255, null=True)),
                ('sementes_armazenadas_condicoes', models.CharField(blank=True, max_length=10, null=True)),
                ('observacao8', models.CharField(blank=True, max_length=255, null=True)),
                ('foto8_url', models.CharField(blank=True, max_length=255, null=True)),
                ('embalagens_tem_info', models.CharField(blank=True, max_length=255, null=True)),
                ('observacao9', models.CharField(blank=True, max_length=255, null=True)),
                ('foto9_url', models.CharField(blank=True, max_length=255, null=True)),
                ('sementes_tratadas_produto_quimico', models.CharField(blank=True, max_length=255, null=True)),
                ('observacao10', models.CharField(blank=True, max_length=255, null=True)),
                ('foto10_url', models.CharField(blank=True, max_length=255, null=True)),
                ('embalagem_selada', models.CharField(blank=True, max_length=10, null=True)),
                ('observacao11', models.CharField(blank=True, max_length=255, null=True)),
                ('foto11_url', models.CharField(blank=True, max_length=255, null=True)),
                ('etiquetas_classificadas', models.CharField(blank=True, max_length=255, null=True)),
                ('observacao12', models.CharField(blank=True, max_length=255, null=True)),
                ('foto12_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]