# Generated by Django 4.1.4 on 2023-06-27 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundsintel', '0002_rename_information_adm_fee_investmentfund_adm_fee_information_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investmentfund',
            old_name='cnpj_adm',
            new_name='adm_cnpj',
        ),
        migrations.RenameField(
            model_name='investmentfund',
            old_name='cnpj_auditor',
            new_name='auditor_cnpj',
        ),
        migrations.RenameField(
            model_name='investmentfund',
            old_name='cnpj_controler',
            new_name='controler_cnpj',
        ),
        migrations.RenameField(
            model_name='investmentfund',
            old_name='cnpj_custodian',
            new_name='custodian_cnpj',
        ),
        migrations.RenameField(
            model_name='investmentfund',
            old_name='cpf_cnpj_manager',
            new_name='manager_cpf_cnpj',
        ),
    ]