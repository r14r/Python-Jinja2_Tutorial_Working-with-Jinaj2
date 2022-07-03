from jinja2 import Template, StrictUndefined

template = """hostname {{ hostname }}

{# DNS configuration -#}
no ip domain lookup
ip domain name local.lab
ip name-server {{ name_server_pri }}
ip name-server {{ name_server_sec }}

{# Time servers config, we should use pool.ntp.org -#}
ntp server {{ ntp_server_pri }} prefer
ntp server {{ ntp_server_sec }}
ntp server {{ ntp_server_trd }}

interface {{ interface.name }}
    description {{ interface.description }}
    ip address {{ interface.ip_address }}
    speed {{ interface.speed }}
    duplex {{ interface.duplex }}
    mtu {{ interface.mtu }}
 

 # Configuring Prefix List
ip prefix-list PL_AS_65003_IN
{%- for line in demo_loop %}
    {{ line -}}
{% endfor %}

 """

data = {
    "hostname": "core-sw-waw-01",
    "name_server_pri": "1.1.1.1",
    "name_server_sec": "8.8.8.8",
    "ntp_server_pri": "0.pool.ntp.org",
    "ntp_server_sec": "1.pool.ntp.org",
    "ntp_server_trd": "1.pool.ntp.org",
    "interface": {
        "name": "GigabitEthernet1/1",
        "ip_address": "10.0.0.1/31",
        "description": "Uplink to core",
        "speed": "1000",
        "duplex": "full",
        "mtu": "9124"
    },
    "demo_loop": [
        "1",
        "2",
        "3"
    ]

}

j2_template = Template(template, undefined=StrictUndefined)

print(j2_template.render(data))