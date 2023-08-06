# -*- coding: utf-8 -*-
import os, re

from src import settings
from. webpage import WebPage
from src.utils import split_tool
from src import settings

def creates_web_pages(webpages):
    # pages
    for webpage in webpages:
        new_webpagedef = WebPageDef(webpage)
        new_webpagedef.to_file()

class WebPageDef(object):
    """"

    """

    properties = ""
    webpages = ""

    def __init__(self, page, portal = ""):
        self.id = page["id"]
        self.orig_id = page["origId"]
        self.is_portal = page["isPortal"]
        self.obj_def_id = page["objDefId"]
        self.page_type = page["pageType"]
        self.name = page.PageDefName.cdata
        self.jsp = page.JspName.cdata
        if hasattr(page, "Props"):
            self.properties = page.Props.__dict__
        if hasattr(page, "WebPages"):
            if hasattr(page.WebPages, "WebPage"):
                self.webpages = page.WebPages.WebPage
        dirname = split_tool.split_name(self.name, 50)
        if portal:
            self.page_directory = "{}/pages/{}".format(portal, dirname)
        else:
            self.page_directory = "{}/pages/{}".format(settings.APP_DIR, dirname)


    def to_file(self):
        if not os.path.exists(self.page_directory.encode('utf-8')):
            os.makedirs(self.page_directory.encode('utf-8'))

        # fichier de propriétés
        with open("{}/PROPERTIES.md".format(self.page_directory), 'w+', encoding='utf-8') as file:
            # nom de l'objet
            file.write("# {}\n".format(self.name))

            # Informations
            file.write("\n\n## Informations\n")
            file.write("- id : {}\n".format(self.id))
            file.write("- origId : {}\n".format(self.orig_id))
            file.write("- isPortal : {}\n".format(self.is_portal))
            file.write("- objDefId : {}\n".format(self.obj_def_id))
            file.write("- pageType : {}\n".format(self.page_type))
            file.write("- jsp : {}\n".format(self.jsp))

            # Propriétés
            if self.properties:
                for el in self.properties["children"]:
                    file.write("- {} : {}\n".format(el.__dict__["_name"], el.__dict__["cdata"]))

            if self.webpages:
                for webpage in self.webpages:
                    new_webpage = WebPage(webpage, self.page_directory)
                    new_webpage.to_file()

