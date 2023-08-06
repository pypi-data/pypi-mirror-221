
from nwebclient import util
from nwebclient import base as b
import base64

def tag(name, content, **kw):
    a = ''
    for k in kw.keys():
        a += ' ' + k + '="' + str(kw[k]) + '"'
    return '<'+name+a+'>'+content+'</'+name+'>'

def a(content, href):
    if isinstance(href, str):
        return tag('a', content, {'href': href})
    else:
        return tag('a', content, href)
    
def pre(content, **kw):
    return tag('pre', content, **kw)


class NwFlaskRoutes(b.Base):
    def __init__(self):
        super().__init__()
    def requestParams(self):
        from flask import request
        data = {}
        for tupel in request.files.items():
            name = tupel[0]
            f = tupel[1]
            #print(str(f))
            data[name] = base64.b64encode(f.read()).decode('ascii')
        params = {
            **request.cookies.to_dict(),
            **request.args.to_dict(), 
            **request.form.to_dict(),
            **data,
            **{'request_url': request.url}}
        return params
    def addTo(self, app):
        self.web = app
        app.add_url_rule('/nw/<path:p>', 'nw', lambda p: self.nw(p), methods=['GET', 'POST'])
        app.add_url_rule('/nws/', 'nws', self.nws)
    def nws(self):
        p = b.Page().h1("Module")
        for e in b.Plugins('nweb_web'):
            p.div('<a href="{0}">{1}</a>'.format('/nw/'+e.name, e.name))
        return p.simple_page()
    def nw(self, path):
        params = self.requestParams()
        n = path.split('/')[0]
        if self.hasName(n):
            return self.getChildByName(n).page(params)
        plugin = b.Plugins('nweb_web')[n]
        if plugin is not None:
            obj = util.load_class(plugin.value, create=True)  
            w = self.addChild(b.WebObject(obj, {**{'path': path}, **params}))
            w.name = n
            return w.page(params)
        else:
            return "Error: 404 (NwFlaskRoutes)"