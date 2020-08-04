from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("config.xml")
config = DOMTree.documentElement
if config.hasAttribute("program"):
    print("Root element: %s" % config.getAttribute("program"))

sections = config.getElementsByTagName("Main")


