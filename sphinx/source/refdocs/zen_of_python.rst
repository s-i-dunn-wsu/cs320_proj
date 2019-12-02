The Zen of Python, by Tim Peters
=================================

.. Becca

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Zen Highlights:
----------------
.. how do I create a new line??

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
and 13 more...


Beautiful is better than ugly
-------------------------------
DON'T

.. code-block:: python

    halve_evens_only = lambda nums: map(lambda i: i/2, filter(lambda i: not i%2, nums))

DO

.. code-block:: python

    def halve_evens_only(nums):
    return [i/2 for i in nums if not i % 2]


Simple is better than complex.
---------------------------------
DON’T

.. code-block:: python

    def store(measurements):
        import sqlalchemy
        import sqlalchemy.types as sqltypes
        
        db = sqlalchemy.create_engine('sqlite:///measurements.db')
        db.echo = False
        metadata = sqlalchemy.MetaData(db)
        table = sqlalchemy.Table('measurements', metadata,
            sqlalchemy.Column('id', sqltypes.Integer, primary_key=True),
            sqlalchemy.Column('weight', sqltypes.Float),
            sqlalchemy.Column('temperature', sqltypes.Float),
            sqlalchemy.Column('color', sqltypes.String(32)),
            )
        table.create(checkfirst=True)
        
        for measurement in measurements:
            i = table.insert()
            i.execute(**measurement)

DO

.. code-block:: python

    def store(measurements):
    import json
    with open('measurements.json', 'w') as f:
        f.write(json.dumps(measurements))


Sparse is better than dense
------------------------------
DON’T

.. code-block:: python

    def process(response):
        selector = lxml.cssselect.CSSSelector('#main > div.text')
        lx = lxml.html.fromstring(response.body)
        title = lx.find('./head/title').text
        links = [a.attrib['href'] for a in lx.find('./a') if 'href' in a.attrib]
        for link in links:
        yield Request(url=link)
        divs = selector(lx)
        if divs: yield Item(utils.lx_to_text(divs[0]))

DO

.. code-block:: python

    def process(response):
        lx = lxml.html.fromstring(response.body)

        title = lx.find('./head/title').text

        links = [a.attrib['href'] for a in lx.find('./a') if 'href' in a.attrib]for link in links:
            yield Request(url=link)

        selector = lxml.cssselect.CSSSelector('#main > div.text')
        divs = selector(lx)
        if divs:
            bodytext = utils.lx_to_text(divs[0])
            yield Item(bodytext)




For full Zen
-------------

In a Python shell, type "import this"
