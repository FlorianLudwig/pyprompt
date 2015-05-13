# -*- coding: utf-8 -*-
"""pyprompt

USAGE
set PS1 environment variable (for example in your .bashrc)
PS1="\$(pyprompt \$?)"
"""
import socket
import os
import pwd
import sys
import fcntl
import termios
import struct
import git


GIT_SYMBOLS = {
    'synced': u"",
    'dirty_synced': u"*",
    'unpushed': u"△",
    'dirty_unpushed': u"▲",
    'unpulled': u"▽",
    'dirty_unpulled': u"▼",
    'unpushed_unpulled': u"⬡",
    'dirty_unpushed_unpulled': u"⬢"
}

# PROMPT_SYNCED_SYMBOL=""
# PROMPT_DIRTY_SYNCED_SYMBOL="*"
# PROMPT_UNPUSHED_SYMBOL="↑"
# PROMPT_DIRTY_UNPUSHED_SYMBOL="*↑"
# PROMPT_UNPULLED_SYMBOL="↓"
# PROMPT_DIRTY_UNPULLED_SYMBOL="*↓"
# PROMPT_UNPUSHED_UNPULLED_SYMBOL="*↑↓"
# PROMPT_DIRTY_UNPUSHED_UNPULLED_SYMBOL="*↑↓"


def color(t, c, bg=0):
    return u'\x1b[' + unicode(c) + u'm' + unicode(t) + u'\x1b[0m'


def black(t):
    return color(t, u'30')


def red(t):
    return color(t, u'31')


def green(t):
    return color(t, u'32')


def yellow(t):
    return color(t, u'1;33')


def cyan(t):
    return color(t, u'36')


def bold(t):
    return color(t, u'1')


def orange(t):
    return color(t, u'33')


def black_bg(t):
    return color(t, u'40')


def red_bg(t):
    return color(t, u'41')


def green_bg(t):
    return color(t, u'42')


def yellow_bg(t):
    return color(t, u'43')


def blue_bg(t):
    return color(t, u'44')


def purple_bg(t):
    return color(t, u'45')


def cyan_bg(t):
    return color(t, u'46')


def white_bg(t):
    return color(t, u'47')


def _ioctl_GWINSZ(fd):
    try:
        cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '0000'))
    except:
        return None
    return cr


def terminal_size():
    env = os.environ

    cr = _ioctl_GWINSZ(sys.stdout.fileno()) or _ioctl_GWINSZ(sys.stderr.fileno())
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = _ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass

    if not cr:
        try:
            cr = (env['LINES'], env['COLUMNS'])
        except:
            cr = (25, 80)
    return int(cr[1]), int(cr[0])


def get_git_status():
    try:
        repo = git.Repo()
    except git.exc.InvalidGitRepositoryError:
        return ''

    branch = unicode(repo.active_branch)
    # symbol = []
    symbol = ''
    if repo.is_dirty():
        # symbol += 'dirty'
        symbol = '*'

    # unpushed = list(repo.iter_commits('{0}..{0}@{{u}}'.format(branch)))

    return symbol + branch


def main():
    # choose background color depending on last return code
    last_return_code = int(sys.argv[1])
    bg = white_bg if last_return_code == 0 else red_bg
    fg = black if last_return_code == 0 else lambda x: x

    width = terminal_size()[0]
    uid = os.getuid()
    user_name = pwd.getpwuid(uid)[0]
    root = uid == 0
    if root:
        user = white_bg(red(user_name)).encode('utf-8')
    else:
        user = bg(fg(user_name)).encode('utf-8')
    path = os.path.abspath('.').decode('utf-8')
    home = os.path.expanduser('~')
    if path.startswith(home):
        path = '~' + path[len(home):]

    text = u'@%s %s' % (socket.gethostname(), path)
    right = get_git_status()


    if len(user_name) + len(text) + len(right) + 1 > width:
        # to much information for one line!
        pass
    else:
        text += ' ' * (width - len(text) - len(user_name) - len(right))
        text += right

    # write title + return to start
    sys.stdout.write('\033]0;' + path.encode('utf-8') + '\007\r')
    print user + bg(fg(text)).encode('utf-8')
    if root:
        sys.stdout.write('# ')
    else:
        sys.stdout.write('$ ')


if __name__ == '__main__':
    main()
