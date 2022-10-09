# Generated by Django 4.1.2 on 2022-10-09 05:30

from django.db import migrations


class Migration(migrations.Migration):

    initial = True
    
    dependencies = []

    operations = [
        migrations.RunSQL(
            sql=[("CREATE OR REPLACE AGGREGATE range_merge(anyrange)(sfunc=range_merge, stype=anyrange);")],
            reverse_sql=[("DROP AGGREGATE IF EXISTS range_merge(anyrange);")],
        )
    ]