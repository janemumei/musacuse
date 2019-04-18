from app import app

@app.route('/')
@app.route('/<int:cid>')
def index(cid=None):
    return 'Properties in Catchment %d' % cid
