import subprocess, argparse, json, pathlib, shutil, os

PATH = os.getcwd()
cmd  = lambda x: subprocess.run(x, check=True, shell=True)

def new_project(name):
    app_name = name.lower().replace('-','_')
    cmd(f'git clone https://github.com/hlop3z/python_skeleton')

    EXAMPLE_FILE = f"""
import { app_name }

# Modules
print( { app_name }.plugins )

# Class
{ app_name }.__demo__.Plugin().hello()

# Def
{ app_name }.__demo__.hello()
    """.strip()

    try:
        shutil.rmtree("python_skeleton/.git")
        shutil.rmtree("python_skeleton/tests")
        shutil.rmtree("python_skeleton/examples")
        shutil.rmtree("python_skeleton/dist")
        shutil.rmtree("python_skeleton/python_skeleton.egg-info")
        os.remove("python_skeleton/project.py")
    except Exception as e:
        raise


    os.mkdir('python_skeleton/examples')
    os.mkdir('python_skeleton/tests')

    with open("python_skeleton/examples/example.py", "w") as f:
        f.write( EXAMPLE_FILE )
        f.close()

    shutil.move("python_skeleton/python_skeleton", f"python_skeleton/{ app_name }")
    shutil.move("python_skeleton", app_name)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('project', nargs=1, help='''Clone Github "hlop3z/python_skeleton" for a new project''')
    args = parser.parse_args()

    if args.project: new_project( args.project[0] )
    else: pass



if __name__ == '__main__':
    main()
