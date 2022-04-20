import libs.ulogging as logging
import libs.picoweb as picoweb


def index(req, resp):
    yield from picoweb.start_response(resp, content_type="application/json; charset=utf-8")

    indexFile = open('modules/server/web/index.html', 'r')

    for line in indexFile:
        yield from resp.awrite(line)
    # yield from app.render_template(resp, "modules/server/web/index.html", (req,))


ROUTES = [
    ("/", index),
    # ("/squares", squares),
    # (re.compile("^/(.+)"), lambda req, resp: (yield from app.sendfile(resp,
    #  "/modules/server/web/" + req.url_match.group(1)))),
    # ("/file", lambda req, resp: (yield from app.sendfile(resp, "example_webapp.py"))),
    # ... or match using a regex, the match result available as req.url_match
    # for match group extraction in your view.
    # (re.compile("^/iam/(.+)"), hello),
]

app = picoweb.WebApp(__name__, ROUTES)


def start_api():
    # debug values:
    # -1 disable all logging
    # 0 (False) normal logging: requests and errors
    # 1 (True) debug logging
    # 2 extra debug logging
    app.run(debug=2, host='192.168.4.1', port=80)
    # app.run(debug=1, log=False)
