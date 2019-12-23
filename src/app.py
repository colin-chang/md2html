# -*- coding:utf-8 -*-
import shutil
import os
import sys
import subprocess
from platform import system

input_arg = output_arg = None


def main():
    args = sys.argv

    if len(args) < 3:
        print('missing 2 required positional argument:"input","output"')
        return

    global input_arg, output_arg
    input_arg, output_arg = args[1], args[2]
    if not os.path.isdir(output_arg) or not os.path.exists(output_arg):
        print('{} must be a directory,and be sure it exists'.format(output_arg))
        return

    inputs = []
    if not os.path.exists(input_arg):
        print('{} must exist'.format(input_arg))
        return
    elif os.path.isfile(input_arg):
        inputs.append(input_arg)
    elif os.path.isdir(input_arg):
        for root, _, files in os.walk(input_arg):
            for file in files:
                if file.endswith(".md"):
                    inputs.append(os.path.join(root, file))
    else:
        print('{} must be a file or directory'.format(input_arg))
        return

    __run_command(
        'chmod -R 777 static {} {}'.format(input_arg, output_arg))
    __build(inputs, output_arg)


def __build(inputs, output):
    if not os.path.exists('node_modules'):
        __run_command('npm install')

    for md in inputs:
        if os.path.getsize(md) <= 0:
            continue
        __run_command('rm -rf static/*.md')
        # shutil.copy(md, "static")
        __run_command('cp {} static/README.md'.format(md))
        __run_command('npm run build')
        os.rename(os.path.join('dist', 'index.html'), os.path.join(
            'dist', '{}.html'.format(os.path.splitext(os.path.basename(md))[0])))

        des_path = os.path.dirname(md).replace(input_arg, output_arg)
        __run_command('mkdir -p {}'.format(des_path))
       
        # mv dist/* dest
        for root, _, files in os.walk('dist'):
            for file in files:
                cur_file = os.path.join(root, file)
                des_file = cur_file.replace('dist',des_path)
                if not os.path.exists(os.path.dirname(des_file)):
                    os.mkdir(os.path.dirname(des_file))
                __run_command('mv {} {}'.format(cur_file,des_file))
        shutil.rmtree('dist')

        # docker run -it --rm -e input -e output mdbuilder:1.0
        

def __run_command(cmd):
    if not cmd:
        return

    subprocess.run(cmd.split(' '))


if __name__ == "__main__":
    if system()!='Linux':
        print('only linux is supported curretly')
    else:
        main()
