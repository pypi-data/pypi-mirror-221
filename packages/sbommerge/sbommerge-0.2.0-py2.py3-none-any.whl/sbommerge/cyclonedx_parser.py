# Copyright (C) 2022 Anthony Harrison
# SPDX-License-Identifier: Apache-2.0

import json

import defusedxml.ElementTree as ET
from sbommerge.package import SBOMPackage

class CycloneDXParser:
    def __init__(self):
        pass

    def parse(self, sbom_file):
        """parses CycloneDX BOM file extracting package name, version and license"""
        if sbom_file.endswith("json"):
            return self.parse_cyclonedx_json(sbom_file)
        elif sbom_file.endswith(".xml"):
            return self.parse_cyclonedx_xml(sbom_file)
        else:
            return {}

    def parse_cyclonedx_json(self, sbom_file):
        """parses CycloneDX JSON BOM file extracting package name, version and license"""
        data = json.load(open(sbom_file))
        files = {}
        packages = {}
        cyclonedx_package = SBOMPackage()
        for d in data["components"]:
            cyclonedx_package.initialise()
            if d["type"] in ["library", "application", "operating-system"]:
                package = d["name"]
                cyclonedx_package.set_name(package)
                version = d["version"]
                cyclonedx_package.set_version(version)
                # Record type of component
                cyclonedx_package.set_type(d["type"])
                if "supplier" in d:
                    # Assume that this refers to an organisation
                    cyclonedx_package.set_supplier("Organisation", d["supplier"]["name"])
                if "author" in d:
                    # Assume that this refers to an individual
                    cyclonedx_package.set_supplier("Person", d["author"])
                if "description" in d:
                    cyclonedx_package.set_description(d["description"])
                if "hashes" in d:
                    # Potentially multiple entries
                    for checksum in d["hashes"]:
                        cyclonedx_package.set_checksum(checksum["alg"], checksum["content"])
                # Multiple ways of defining license data
                if "licenses" in d and len(d["licenses"]) > 0:
                    license_data = d["licenses"][0]
                    if "license" in license_data:
                        if "id" in license_data["license"]:
                            license = license_data["license"]["id"]
                        elif "name" in license_data["license"]:
                            license = license_data["license"]["name"]
                    elif "expression" in license_data:
                        license = license_data["expression"]
                    # Assume License concluded is same as lincense declared
                    cyclonedx_package.set_licenseconcluded(license)
                    cyclonedx_package.set_licensedeclared(license)
                if "copyright" in d:
                    cyclonedx_package.set_copyrighttext(d["copyright"])
                if "cpe" in d:
                    cyclonedx_package.set_externalreference("SECURITY", "cpe23Type", d["cpe"])
                if "purl" in d:
                    cyclonedx_package.set_externalreference("PACKAGE-MANAGER", "purl", d["purl"])
                if "properties" in d:
                    # Potentially multiple entries
                    for property in d["properties"]:
                        cyclonedx_package.set_property(property["name"], property["value"])
                if package not in packages:
                    # Save package metadata
                    packages[package] = cyclonedx_package.get_package()

        return files, packages

    def parse_cyclonedx_xml(self, sbom_file):
        """parses CycloneDX XML BOM file extracting package name, version and license"""
        files = {}
        packages = {}
        tree = ET.parse(sbom_file)
        # Find root element
        root = tree.getroot()
        # Extract schema
        schema = root.tag[: root.tag.find("}") + 1]
        for components in root.findall(schema + "components"):
            try:
                for component in components.findall(schema + "component"):
                    # Only for application and library components
                    if component.attrib["type"] in ["library", "application"]:
                        component_name = component.find(schema + "name")
                        if component_name is None:
                            raise KeyError(f"Could not find package in {component}")
                        package = component_name.text
                        if package is None:
                            raise KeyError(f"Could not find package in {component}")
                        component_version = component.find(schema + "version")
                        if component_version is None:
                            raise KeyError(f"Could not find version in {component}")
                        version = component_version.text
                        license = "NOT FOUND"
                        component_license = component.find(schema + "licenses")
                        if component_license is not None:
                            license_data = component_license.find(schema + "expression")
                            if license_data is not None:
                                license = license_data.text
                        if version is not None:
                            if package not in packages:
                                packages[package] = [version, license]
            except KeyError as e:
                pass

        return files, packages
