from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile

from pmr2.z3cform.page import SimplePage


class CytoscapeJSDemo(SimplePage):
    """
    Demo Cytoscape.js view.
    """

    index = ViewPageTemplateFile('cytoscape_js_demo.pt')
