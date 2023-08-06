# Copyright (C) 2022 Anthony Harrison
# SPDX-License-Identifier: Apache-2.0

class SBOMFile:

    def __init__(self):
        pass

    def initialise(self):
        self.file = {}

    def set_name(self, name):
        self.file["name"] = name

    def set_filetype(self, type):
        if "filetype" in self.file:
            self.file["filetype"].append(type)
        else:
            self.file["filetype"]= [type]

    def set_checksum(self, type, value):
        # Allow multiple entries
        checksum_entry = [type.strip(), value]
        if "checksum" in self.file:
            self.file["checksum"].append(checksum_entry)
        else:
            self.file["checksum"] = [checksum_entry]

    def set_licenseconcluded(self, license):
        self.file["licenseconcluded"] = license

    def set_licenseinfoinfile(self, license_info):
        if "licenseinfoinfile" in self.file:
            self.file["licenseinfoinfile"].append(license_info)
        else:
            self.file["licenseinfoinfile"]= [license_info]

    def set_licensecomment(self, comment):
        self.file["licensecomment"] = comment

    def set_copyrighttext(self, text):
        self.file["copyrighttext"] = text

    def set_comment(self, comment):
        self.file["comment"] = comment

    def set_notice(self, notice):
        self.file["notice"] = notice

    def set_contributor(self, name):
        if "contributor" in self.file:
            self.file["contributor"].append(name)
        else:
            self.file["contributor"]= [name]

    def set_attribution(self, attribution):
        self.file["attribution"] = attribution

    #### TEMPLATE for muliple instances
    def set_externalreference(self, type, value):
        # Allow multiple entries
        reference_entry = [type.strip(), value]
        if "externalreference" in self.file:
            self.file["externalreference"].append(reference_entry)
        else:
            self.file["externalreference"]= [reference_entry]

    def set_value(self, key, value):
        self.file[key] = value

    def get_file(self):
        return self.file

    def debug_file(self):
        print ("OUTPUT:", self.file)

    def show_file(self):
        for key in self.file:
            print (f"{key}    : {self.file[key]}")

    def copy_file(self, file_info):
        for key in file_info:
            self.set_value(key, file_info[key])

    def get_name(self):
        return self.file["name"]