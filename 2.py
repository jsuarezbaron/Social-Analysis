Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from nltk
SyntaxError: invalid syntax
>>> import nltk
>>> from nltk.corpus import cess_esp as cess
>>> from nltk import UnigramTagger as ut
>>> sents = cess.tagged_sents()
>>> 
>>> sents
[[('El', 'da0ms0'), ('grupo', 'ncms000'), ('estatal', 'aq0cs0'), ('Electricité_de_France', 'np00000'), ('-Fpa-', 'Fpa'), ('EDF', 'np00000'), ('-Fpt-', 'Fpt'), ('anunció', 'vmis3s0'), ('hoy', 'rg'), (',', 'Fc'), ('jueves', 'W'), (',', 'Fc'), ('la', 'da0fs0'), ('compra', 'ncfs000'), ('del', 'spcms'), ('51_por_ciento', 'Zp'), ('de', 'sps00'), ('la', 'da0fs0'), ('empresa', 'ncfs000'), ('mexicana', 'aq0fs0'), ('Electricidad_Águila_de_Altamira', 'np00000'), ('-Fpa-', 'Fpa'), ('EAA', 'np00000'), ('-Fpt-', 'Fpt'), (',', 'Fc'), ('creada', 'aq0fsp'), ('por', 'sps00'), ('el', 'da0ms0'), ('japonés', 'aq0ms0'), ('Mitsubishi_Corporation', 'np00000'), ('para', 'sps00'), ('poner_en_marcha', 'vmn0000'), ('una', 'di0fs0'), ('central', 'ncfs000'), ('de', 'sps00'), ('gas', 'ncms000'), ('de', 'sps00'), ('495', 'Z'), ('megavatios', 'ncmp000'), ('.', 'Fp')], [('Una', 'di0fs0'), ('portavoz', 'nccs000'), ('de', 'sps00'), ('EDF', 'np00000'), ('explicó', 'vmis3s0'), ('a', 'sps00'), ('EFE', 'np00000'), ('que', 'cs'), ('el', 'da0ms0'), ('proyecto', 'ncms000'), ('para', 'sps00'), ('la', 'da0fs0'), ('construcción', 'ncfs000'), ('de', 'sps00'), ('Altamira_2', 'np00000'), (',', 'Fc'), ('al', 'spcms'), ('norte', 'ncms000'), ('de', 'sps00'), ('Tampico', 'np00000'), (',', 'Fc'), ('prevé', 'vmm02s0'), ('la', 'da0fs0'), ('utilización', 'ncfs000'), ('de', 'sps00'), ('gas', 'ncms000'), ('natural', 'aq0cs0'), ('como', 'cs'), ('combustible', 'ncms000'), ('principal', 'aq0cs0'), ('en', 'sps00'), ('una', 'di0fs0'), ('central', 'ncfs000'), ('de', 'sps00'), ('ciclo', 'ncms000'), ('combinado', 'aq0msp'), ('que', 'pr0cn000'), ('debe', 'vmip3s0'), ('empezar', 'vmn0000'), ('a', 'sps00'), ('funcionar', 'vmn0000'), ('en', 'sps00'), ('mayo_del_2002', 'W'), ('.', 'Fp')], ...]
>>> tag = ut(sents)

>>> oracion = "Las TICs en la actualidad son fuente de conocimiento y de sabiduría de muchas personas que han generado y compartido sus logros."
>>> tagged = tag.tag(oracion.split(" "))
>>> tagged
[('Las', 'da0fp0'), ('TICs', None), ('en', 'sps00'), ('la', 'da0fs0'), ('actualidad', 'ncfs000'), ('son', 'vsip3p0'), ('fuente', 'ncfs000'), ('de', 'sps00'), ('conocimiento', 'ncms000'), ('y', 'cc'), ('de', 'sps00'), ('sabiduría', 'ncfs000'), ('de', 'sps00'), ('muchas', 'di0fp0'), ('personas', 'ncfp000'), ('que', 'pr0cn000'), ('han', 'vaip3p0'), ('generado', 'vmp00sm'), ('y', 'cc'), ('compartido', 'aq0msp'), ('sus', 'dp3cp0'), ('logros.', None)]
>>> Tree01 = nltk.corpus.cess_esp.tagged.draw()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    Tree01 = nltk.corpus.cess_esp.tagged.draw()
AttributeError: 'BracketParseCorpusReader' object has no attribute 'tagged'
>>> Tree01 = nltk.corpus.cess_esp.parsed_sents(tagged).draw()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    Tree01 = nltk.corpus.cess_esp.parsed_sents(tagged).draw()
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 403, in parsed_sents
    for fileid, enc in self.abspaths(fileids, True)])
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 193, in abspaths
    paths = [self._root.join(f) for f in fileids]
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 193, in <listcomp>
    paths = [self._root.join(f) for f in fileids]
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\data.py", line 337, in join
    _path = os.path.join(self._path, fileid)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\ntpath.py", line 114, in join
    genericpath._check_arg_types('join', path, *paths)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\genericpath.py", line 149, in _check_arg_types
    (funcname, s.__class__.__name__)) from None
TypeError: join() argument must be str or bytes, not 'tuple'
>>> Tree01 = nltk.corpus.cess_esp.parsed_sents()[1].draw()
>>> tagged
[('Las', 'da0fp0'), ('TICs', None), ('en', 'sps00'), ('la', 'da0fs0'), ('actualidad', 'ncfs000'), ('son', 'vsip3p0'), ('fuente', 'ncfs000'), ('de', 'sps00'), ('conocimiento', 'ncms000'), ('y', 'cc'), ('de', 'sps00'), ('sabiduría', 'ncfs000'), ('de', 'sps00'), ('muchas', 'di0fp0'), ('personas', 'ncfp000'), ('que', 'pr0cn000'), ('han', 'vaip3p0'), ('generado', 'vmp00sm'), ('y', 'cc'), ('compartido', 'aq0msp'), ('sus', 'dp3cp0'), ('logros.', None)]
>>> parser = nltk.ChartParser(tagged)
>>> parser
<nltk.parse.chart.ChartParser object at 0x0E6FC9F0>
>>> parser.draw()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    parser.draw()
AttributeError: 'ChartParser' object has no attribute 'draw'
>>> for tree in parser.parse(sent):
...     print(tree)
SyntaxError: expected an indented block
>>> for tree in parser.parse(sent) print(tree)
SyntaxError: invalid syntax
>>> tagged
[('Las', 'da0fp0'), ('TICs', None), ('en', 'sps00'), ('la', 'da0fs0'), ('actualidad', 'ncfs000'), ('son', 'vsip3p0'), ('fuente', 'ncfs000'), ('de', 'sps00'), ('conocimiento', 'ncms000'), ('y', 'cc'), ('de', 'sps00'), ('sabiduría', 'ncfs000'), ('de', 'sps00'), ('muchas', 'di0fp0'), ('personas', 'ncfp000'), ('que', 'pr0cn000'), ('han', 'vaip3p0'), ('generado', 'vmp00sm'), ('y', 'cc'), ('compartido', 'aq0msp'), ('sus', 'dp3cp0'), ('logros.', None)]
>>> Tree01 = nltk.corpus.cess_esp.raw(tagged).draw()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    Tree01 = nltk.corpus.cess_esp.raw(tagged).draw()
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 398, in raw
    return concat([self.open(f).read() for f in fileids])
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 398, in <listcomp>
    return concat([self.open(f).read() for f in fileids])
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 213, in open
    stream = self._root.join(file).open(encoding)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\data.py", line 337, in join
    _path = os.path.join(self._path, fileid)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\ntpath.py", line 114, in join
    genericpath._check_arg_types('join', path, *paths)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\genericpath.py", line 149, in _check_arg_types
    (funcname, s.__class__.__name__)) from None
TypeError: join() argument must be str or bytes, not 'tuple'
>>> t = parser.parse(tagged)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    t = parser.parse(tagged)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\parse\chart.py", line 1351, in parse
    chart = self.chart_parse(tokens)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\parse\chart.py", line 1310, in chart_parse
    self._grammar.check_coverage(tokens)
AttributeError: 'list' object has no attribute 'check_coverage'
>>> S = nltk.Nonterminal('sentence')
>>> grammar = nltk.induce_pcfg(S, prods)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    grammar = nltk.induce_pcfg(S, prods)
NameError: name 'prods' is not defined
>>> prods = sum((t.productions() for t in corpus.parsed_sents()), [])
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    prods = sum((t.productions() for t in corpus.parsed_sents()), [])
NameError: name 'corpus' is not defined
>>> tagged
[('Las', 'da0fp0'), ('TICs', None), ('en', 'sps00'), ('la', 'da0fs0'), ('actualidad', 'ncfs000'), ('son', 'vsip3p0'), ('fuente', 'ncfs000'), ('de', 'sps00'), ('conocimiento', 'ncms000'), ('y', 'cc'), ('de', 'sps00'), ('sabiduría', 'ncfs000'), ('de', 'sps00'), ('muchas', 'di0fp0'), ('personas', 'ncfp000'), ('que', 'pr0cn000'), ('han', 'vaip3p0'), ('generado', 'vmp00sm'), ('y', 'cc'), ('compartido', 'aq0msp'), ('sus', 'dp3cp0'), ('logros.', None)]
>>> t = cess.tagged_sents(tagged)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    t = cess.tagged_sents(tagged)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 409, in tagged_sents
    for fileid, enc in self.abspaths(fileids, True)])
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 193, in abspaths
    paths = [self._root.join(f) for f in fileids]
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 193, in <listcomp>
    paths = [self._root.join(f) for f in fileids]
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\data.py", line 337, in join
    _path = os.path.join(self._path, fileid)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\ntpath.py", line 114, in join
    genericpath._check_arg_types('join', path, *paths)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\genericpath.py", line 149, in _check_arg_types
    (funcname, s.__class__.__name__)) from None
TypeError: join() argument must be str or bytes, not 'tuple'
>>> t = cess.tagged_sents(oracion)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    t = cess.tagged_sents(oracion)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 409, in tagged_sents
    for fileid, enc in self.abspaths(fileids, True)])
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 193, in abspaths
    paths = [self._root.join(f) for f in fileids]
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 193, in <listcomp>
    paths = [self._root.join(f) for f in fileids]
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\data.py", line 338, in join
    return FileSystemPathPointer(_path)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\compat.py", line 221, in _decorator
    return init_func(*args, **kwargs)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\data.py", line 316, in __init__
    raise IOError('No such file or directory: %r' % _path)
OSError: No such file or directory: 'C:\\Users\\UPTC\\AppData\\Roaming\\nltk_data\\corpora\\cess_esp\\Las TICs en la actualidad son fuente de conocimiento y de sabiduría de muchas personas que han generado y compartido sus logros'
>>> t = nltk.chunk.ne_chunk(tagged)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    t = nltk.chunk.ne_chunk(tagged)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\chunk\__init__.py", line 177, in ne_chunk
    return chunker.parse(tagged_tokens)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\chunk\named_entity.py", line 122, in parse
    tagged = self._tagger.tag(tokens)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\tag\sequential.py", line 63, in tag
    tags.append(self.tag_one(tokens, i, tags))
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\tag\sequential.py", line 83, in tag_one
    tag = tagger.choose_tag(tokens, index, history)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\tag\sequential.py", line 632, in choose_tag
    featureset = self.feature_detector(tokens, index, history)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\tag\sequential.py", line 680, in feature_detector
    return self._feature_detector(tokens, index, history)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\chunk\named_entity.py", line 85, in _feature_detector
    nextpos = tokens[index+1][1].lower()
AttributeError: 'NoneType' object has no attribute 'lower'
>>> tagged
[('Las', 'da0fp0'), ('TICs', None), ('en', 'sps00'), ('la', 'da0fs0'), ('actualidad', 'ncfs000'), ('son', 'vsip3p0'), ('fuente', 'ncfs000'), ('de', 'sps00'), ('conocimiento', 'ncms000'), ('y', 'cc'), ('de', 'sps00'), ('sabiduría', 'ncfs000'), ('de', 'sps00'), ('muchas', 'di0fp0'), ('personas', 'ncfp000'), ('que', 'pr0cn000'), ('han', 'vaip3p0'), ('generado', 'vmp00sm'), ('y', 'cc'), ('compartido', 'aq0msp'), ('sus', 'dp3cp0'), ('logros.', None)]
>>> t = cess.parsed_sents(tagged)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    t = cess.parsed_sents(tagged)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 403, in parsed_sents
    for fileid, enc in self.abspaths(fileids, True)])
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 193, in abspaths
    paths = [self._root.join(f) for f in fileids]
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 193, in <listcomp>
    paths = [self._root.join(f) for f in fileids]
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\data.py", line 337, in join
    _path = os.path.join(self._path, fileid)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\ntpath.py", line 114, in join
    genericpath._check_arg_types('join', path, *paths)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\genericpath.py", line 149, in _check_arg_types
    (funcname, s.__class__.__name__)) from None
TypeError: join() argument must be str or bytes, not 'tuple'
>>> tagged
[('Las', 'da0fp0'), ('TICs', None), ('en', 'sps00'), ('la', 'da0fs0'), ('actualidad', 'ncfs000'), ('son', 'vsip3p0'), ('fuente', 'ncfs000'), ('de', 'sps00'), ('conocimiento', 'ncms000'), ('y', 'cc'), ('de', 'sps00'), ('sabiduría', 'ncfs000'), ('de', 'sps00'), ('muchas', 'di0fp0'), ('personas', 'ncfp000'), ('que', 'pr0cn000'), ('han', 'vaip3p0'), ('generado', 'vmp00sm'), ('y', 'cc'), ('compartido', 'aq0msp'), ('sus', 'dp3cp0'), ('logros.', None)]
>>> Unigram tagger -> tagged
SyntaxError: invalid syntax
>>> from nltk.corpus import treebank
>>> t = treebank.parsed_sents(tagged);
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    t = treebank.parsed_sents(tagged);
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 403, in parsed_sents
    for fileid, enc in self.abspaths(fileids, True)])
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 193, in abspaths
    paths = [self._root.join(f) for f in fileids]
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\corpus\reader\api.py", line 193, in <listcomp>
    paths = [self._root.join(f) for f in fileids]
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk\data.py", line 337, in join
    _path = os.path.join(self._path, fileid)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\ntpath.py", line 114, in join
    genericpath._check_arg_types('join', path, *paths)
  File "C:\Users\UPTC\AppData\Local\Programs\Python\Python36-32\lib\genericpath.py", line 149, in _check_arg_types
    (funcname, s.__class__.__name__)) from None
TypeError: join() argument must be str or bytes, not 'tuple'
>>> tagged
[('Las', 'da0fp0'), ('TICs', None), ('en', 'sps00'), ('la', 'da0fs0'), ('actualidad', 'ncfs000'), ('son', 'vsip3p0'), ('fuente', 'ncfs000'), ('de', 'sps00'), ('conocimiento', 'ncms000'), ('y', 'cc'), ('de', 'sps00'), ('sabiduría', 'ncfs000'), ('de', 'sps00'), ('muchas', 'di0fp0'), ('personas', 'ncfp000'), ('que', 'pr0cn000'), ('han', 'vaip3p0'), ('generado', 'vmp00sm'), ('y', 'cc'), ('compartido', 'aq0msp'), ('sus', 'dp3cp0'), ('logros.', None)]
>>> tagged.
