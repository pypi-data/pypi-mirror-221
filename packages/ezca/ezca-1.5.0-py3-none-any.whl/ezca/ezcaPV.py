class EzcaPV(object):
    def __init__(self, channel, ezca):
        self.ezca = ezca
        self.channel = channel

    def __repr__(self):
        return '%s(%r, %r)' % (self.__class__.__name__, self.channel, self.ezca)

    def __str__(self):
        return '<%s %r>' % (self.__class__.__name__, self.channel)

    @property
    def pvname(self):
        return self.ezca.prefix + self.channel

    def get(self):
        return self.ezca.read(self.channel)

    def put(self, value, wait=True, monitor=True, **kwargs):
        return self.ezca.write(self.channel, value,
                               wait=wait,
                               monitor=monitor,
                               **kwargs)
