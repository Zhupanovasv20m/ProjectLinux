import subprocess
import string


def found_ls(comand, text) -> bool:
    result = subprocess.run(comand, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    punctuation = string.punctuation
    for i in out:
        if i in punctuation:
            out = out.replace(i, ' ')

    if text in out:
        return True
    else:
        return False


if __name__ == '__main__':
    print(found_ls('ls /etc/network', 'pre'))
