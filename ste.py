import sys
import re

charEscape = '$'
charScriptStart = '{'
charScriptEnd = '}'
charComment = '/'
charContext = '@'
charFormat = '%'

tagScriptStart = charEscape + charScriptStart
tagScriptEnd = charScriptEnd + charEscape
tagExpression = charEscape
tagIndent = tagScriptStart + charEscape
tagUnindent = charEscape + tagScriptEnd
tagCommentStart = charEscape + charComment
tagCommentEnd = charComment + charEscape
tagSwitchContext = charEscape + charContext
tagFormatStart = charEscape + charFormat
tagFormatEnd = charFormat

indent = 0
templateScript = []

def read(tf):
	with open(tf,'r') as fd:
		return fd.read()

def append(string):
	re.sub()
	templateScript.append('\t' * indent + string)

def script(string):
	if not string or string == '':
		return
	append(string)

def text(string):
	global indent
	if not string or string == '':
		return
	indent += len(re.findall(re.escape(tagIndent),string)) - len(re.findall(re.escape(tagUnindent),string))
	append(string)

def convert(template):

	scriptPattern = re.compile(re.escape(tagScriptStart)+'.*?'+re.escape(tagScriptEnd))
	whitePattern = re.compile(r'[ \t\n\r]+')
	lastPos = 0
	curPos = 0
	for script in re.finditer(scriptPattern,template):
		curPos = script.start()
		textString = template[lastPos:curPos]

		if re.sub(whitePattern,'',template[lastPos:curPos])
		text(template[lastPos:curPos])
		lastPos = script.start()
		script(script.group()[len(tagScriptStart):-len(tagScriptEnd)])
