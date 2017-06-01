import uuid


def gen_uuid():
    return str(uuid.uuid1())


class CustomOS:
    # parameter example: 'rhel', '6', # 'NeoKylin', 64
    def __init__(self, baseOS, name, version, bit, templateName=''):
        self.baseOS = baseOS
        self.bit = bit
        self.version = version
        self.name = name
        self.reference_label = '{reference_name}-{version}-64bit'.format(
            reference_name=name.replace(' ', '-').lower(), version=version)
        if templateName:
            self.templateName = templateName
        else:
            self.templateName = name

    def genPattern(self):
        json = ''
        if self.baseOS == 'rhel-6':
            pattern = '''\
{{
   "uuid": "{uuid}",
   "reference_label": "{reference_label}",
   "name_label": "{name} {version} (64-bit)",
   "derived_from": "base-el-6-64bit.json"
}}\
'''
            json = pattern.format(uuid=gen_uuid(),
                                  reference_label=self.reference_label,
                                  version=self.version, name=self.templateName)

        elif self.baseOS == 'rhel-5':
            pattern = '''\
{{
   "uuid": "{uuid}",
   "reference_label": "{reference_label}",
   "name_label": "{name} {version} (64-bit)",
   "derived_from": "base-el-5-64bit.json"
}}\
'''
            json = pattern.format(uuid=gen_uuid(),
                                  reference_label=self.reference_label,
                                  version=self.version, name=self.templateName)

        elif self.baseOS == 'debian-6':
            pattern = '''\
{{
    "uuid": "{uuid}",
    "reference_label": "{reference_label}",
    "name_label": "{name} {version} (64-bit)",
    "derived_from": "base-debian-pv.json",
    "min_memory": "512M",
    "other_config": {{
        "debian-release": "squeeze",
        "install-arch": "amd64"
    }}
}}\
'''
            json = pattern.format(uuid=gen_uuid(),
                                  reference_label=self.reference_label,
                                  version=self.version, name=self.templateName)

        elif self.baseOS == 'hvm':
            pattern = '''\
{{
    "uuid": "{uuid}",
    "reference_label": "{reference_label}",
    "name_label": "{name} {version} (64-bit)",
    "derived_from": "base-hvmlinux.json",
    "min_memory": "512M",
    "disks": [ {{ "size": "10G" }} ]
}}\
'''
            json = pattern.format(uuid=gen_uuid(),
                                  reference_label=self.reference_label,
                                  version=self.version, name=self.templateName)

        return json

    def genJsonFile(self):
        json = self.genPattern()
        f = open('g:/%s.json' % self.reference_label, 'wb')
        print >>f, json
        f.close()


def main():
    myOS = CustomOS('rhel-6', 'Asianux Server', 4,  64)
    myOS.genJsonFile()
    myOS = CustomOS('rhel-5', 'Asianux Server', 3,  64)
    myOS.genJsonFile()
    myOS = CustomOS('rhel-6', 'Turbo', 12,  64, templateName='GreatTurbo Enterprise Server')
    myOS.genJsonFile()
    myOS = CustomOS('hvm', 'Linx', 8,  64, templateName='Linx Linux')
    myOS.genJsonFile()
    myOS = CustomOS('debian-6', 'Linx', 6,  64, templateName='Linx Linux')
    myOS.genJsonFile()
    myOS = CustomOS('hvm', 'Yinhe', 4,  64, templateName='Yinhe Kylin')
    myOS.genJsonFile()


main()
