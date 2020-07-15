# Generate Protocols for Bird 1.6.8
# Author: Vineeth Penugonda
from enum import Enum, unique

@unique # Decorator
class Types(Enum):
    BGP = 1
    OSPF = 2

class Protocols:
    template = None

    def __init__(self, type):
        self.type = type
        self.__load_template()
    
    def __load_template(self): # __<func_name>: private function
        if self.type == Types.BGP:
            f = open("templates/protocol_bgp.template", "rt")
            self.template = f.read()
        elif self.type == Types.OSPF:
            f = open("templates/protocol_bgp.template", "rt")
            self.template = f.read()

        f.close()

    def create_protocol(self):
        protocol_name = input("Enter Protocol Name? ")
        self.template = self.template.replace("<name>", protocol_name)
        local_as_num = input("Enter Local ASN? ")
        self.template = self.template.replace("<local_as_number>", local_as_num)
        source_IP = input("Enter Source IP? ")
        self.template = self.template.replace("<source_IP>", source_IP)
        import_filter = input("Enter Input Filter? ")
        self.template = self.template.replace("<filter_type>", import_filter)
        export_filter = input("Enter Export Filter? ")
        self.template = self.template.replace("<filter_type>", export_filter)
        pref_number = input("Enter bgp_local_pref value? ")
        self.template = self.template.replace("<pref_number>", pref_number)
        neighbor_IP = input("Enter Neighbor's IP? ")
        self.template = self.template.replace("<neighbor_IP>", neighbor_IP)
        neighbor_AS = input("Enter Neighbor AS? ")
        self.template = self.template.replace("<neighbor_as>", neighbor_AS)

        self.__write_template()

    def __write_template(self):
        try:
            f = open("backups/protocols.prt", "r")
            self.__write_template_file("r+")
        except IOError:
            self.__write_template_file("w+")

    def __write_template_file(self, flag):
        file_obj = open("backups/protocols.prt", flag)

        if file_obj.read(1):
                file_obj.write("\n\n" + self.template)
        else:
                file_obj.write(self.template)
        
        file_obj.close()
                                
        

