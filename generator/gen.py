import uuid


def gen_uuid():
    return str(uuid.uuid1())


class CustomOS:
    # parameter example: 'rhel', '6', # 'NeoKylin', 64
    def __init__(self, baseOS, name, version, bit):
        self.baseOS = baseOS
        self.bit = bit
        self.version = version
        self.name = name
        self.reference_label = '{reference_name}-{version}-64bit'.format(
            reference_name=name.replace(' ', '-').lower(), version=version)

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
                                  version=self.version, name=self.name)

        if self.baseOS == 'rhel-5':
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
                                  version=self.version, name=self.name)
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


main()
