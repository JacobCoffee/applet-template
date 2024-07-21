## {{app_name}}

### Usage

You've successfully generated a new applet, {{app_name}}. You still need to register
the applet with the Litestar application via any of the methods listed in 
[the documentation](https://docs.litestar.dev/2/usage/routing/overview.html).

{% if db %}
You will also need to fix a few missing import references for database models
(if applicable).
{% endif %}