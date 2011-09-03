import sublime
import subprocess
from subprocess import Popen, PIPE

try:
    STARTUP_INFO = subprocess.STARTUPINFO()
    STARTUP_INFO.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    STARTUP_INFO.wShowWindow = subprocess.SW_HIDE
except (AttributeError):
	STARTUP_INFO = None


GLOBAL_SNIPPETS = [
    (u'\u0282  func: Function ...', 'func ${1:name}($2)$3 {\n\t$0\n}'),
    (u'\u0282  func: Function (receiver) ...', 'func (${1:receiver} ${2:type}) ${3:name}($4)$5 {\n\t$0\n}'),
    (u'\u0282  var: Variable (...)', 'var (\n\t$1\n)'),
    (u'\u0282  const: Constant (...)', 'const (\n\t$1\n)'),
    (u'\u0282  import: Import (...)', 'import (\n\t$2"$1"\n)'),
    (u'\u0282  package: Package ...', 'package ${1:NAME}')
]

LOCAL_SNIPPETS = [
    (u'\u0282  func: Function() ...', 'func($1) {\n\t$0\n}($2)'),
    (u'\u0282  var: Variable (...)', 'var ${1:name} ${2:type}'),
]

CLASS_PREFIXES = {
    'const': u'\u0196   ',
    'func': u'\u0192   ',
    'type': u'\u0288   ',
    'var':  u'\u03BD  ',
    'package': u'\u03C1  ',
}

NAME_PREFIXES = {
    'interface': u'\u00A1  ',
}


def runcmd(args, input=None):
    try:
        p = Popen(args, stdout=PIPE, stderr=PIPE, stdin=PIPE, startupinfo=STARTUP_INFO)
        return p.communicate(input=input)
    except (OSError, ValueError) as e:
        err = 'Error while running %s: %s' % (args[0], e)
        return ("", err)

def setting(key, default=None):
    s = sublime.load_settings("GoSublime.sublime-settings")
    return s.get(key, default)
