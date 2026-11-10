:nosearch:

{{ fullname | escape | underline }}

.. automodule:: {{ fullname }}

{% if classes %}
.. rubric:: Classes

.. autosummary::
    :toctree:
    :template: autosummary/class.rst
    :nosignatures:
{% for item in classes %}
    {{ item }}
{%- endfor %}
{% endif %}

{% if functions %}
.. rubric:: Functions

.. autosummary::
    :toctree:
    :nosignatures:
{% for item in functions %}
    {{ item }}
{%- endfor %}
{% endif %}
