from troposphere import Template
from troposphere.cloudformation import WaitConditionHandle

def sceptre_handler(scepter_user_data):
    template = Template(Description=f"deploy {scepter_user_data['MyName']} template")
    template.add_resource(WaitConditionHandle("WaitConditionHandle"))
    return template.to_json()
