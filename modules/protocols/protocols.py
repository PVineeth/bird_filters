# Generate Protocols for Bird 1.6.8
# Author: Vineeth Penugonda
from enum import Enum, unique, auto
from typing import Optional
import re
import json

@unique # Decorator
class Types(Enum):
    BGP = 1
    OSPF = 2

@unique
class Format(Enum):
    OPENBGPD = auto()
    BIRD_1_x = auto()
    BIRD_2_x = auto()
    JUNIPER = auto()
    JUNIPERRFL = auto()
    JSON = auto()
    MIKROTIK = auto()
    SROSMD = auto()
    SROSCL = auto()
    HUAWEI = auto()

class TemplateFilePaths():
    TEMPLATE_BIRD_BGP_1_x = "../../templates/bird_1.x/protocol_bgp_1_x.template"
    TEMPLATE_BIRD_OSPF_1_x = "../../templates/bird_1.x/protocol_ospf_1_x.template"

class ConfigFilePaths():
    CONFIG_BIRD_BGP_1_x = "/etc/bird/filtering/prefixes/protocols_bgp.prt"
    CONFIG_BP_BIRD_BGP_1_x = "../../backups/bird_protocols_bgp.prt"


class Protocols:
    template: Optional[str] = None
    config: Optional[str] = None

    def __init__(self, type = Types.BGP, format = Format.BIRD_1_x):
        self.type = type
        self.format = format
        self.__load_template()
    
    def __load_template(self): # __<func_name>: private function
        if self.format == Format.BIRD_1_x:
            self.__load_template_bird_1_x()

    def __load_template_bird_1_x(self):
        if self.type == Types.BGP:
            f = open(TemplateFilePaths.TEMPLATE_BIRD_BGP_1_x, "rt")
            self.template = f.read()
        elif self.type == Types.OSPF: # Future Implementation
            f = open(TemplateFilePaths.TEMPLATE_BIRD_OSPF_1_x, "rt")
            self.template = f.read()

        f.close()

    def create_protocol(self):
        if self.format == Format.BIRD_1_x and self.type == Types.BGP:
            self.__create_protocol_bird_bgp()

    def __create_protocol_bird_bgp(self):
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

        self.__write_config()

    def list_protocol(self):
        if self.format == Format.BIRD_1_x and self.type == Types.BGP:
            return self.__read_config_file()

    # just_read = We don't require parsing and raise exceptions when __write_config() uses this function
    def __read_config_file(self, just_read = False) -> int: # ->: annotations
        if self.format == Format.BIRD_1_x and self.type == Types.BGP:
            try:
                f = open(ConfigFilePaths.CONFIG_BP_BIRD_BGP_1_x, "r")
                status = 1
                self.config = f.read()
                f.close()
                if not just_read:
                    protocols_list = self.__parse_config_file__bird_bgp_1_x()
                    return protocols_list
            except FileNotFoundError:
                status = -1
                if not just_read: # Some functions just need the status
                    raise FileNotFoundError("Configuration file is not found! Please use create_protocol() function to create BGP protocols.")
        
        return status

    def __parse_config_file__bird_bgp_1_x(self) -> list():
        protocol_bgp_list = re.findall('protocol bgp (.*)', self.config)
        print("\nProtocols Enabled:")
        for proto in protocol_bgp_list:
            print(proto)
        print()

        return protocol_bgp_list


    def __write_config(self):
        status = self.__read_config_file(just_read=True)
        if status == 1:
            self.__write_config_file("r+")
        else:
            self.__write_config_file("w+")
            
            

    def __write_config_file(self, flag):
        if self.format == Format.BIRD_1_x and self.type == Types.BGP:
            file_obj = open(ConfigFilePaths.CONFIG_BP_BIRD_BGP_1_x, flag)
            comment = '''##### Upstreams/Downstreams #####\n\n'''

            if file_obj.read(1):
                    file_obj.write("\n\n" + self.template)
            else:
                    file_obj.write(comment + self.template)
            
            print("\nYour File is written to: " + f'{ConfigFilePaths.CONFIG_BIRD_BGP_1_x}' + "\n")
            file_obj.close()
                                
        

