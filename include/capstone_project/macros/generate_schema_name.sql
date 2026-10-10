{% macro generate_schema_name(custom_name,node) %}

{% set default_name=target.schema %}

{% if custom_name %}

{{custom_name}}

{% else %}

{{default_name}}

{% endif %}

{% endmacro %}