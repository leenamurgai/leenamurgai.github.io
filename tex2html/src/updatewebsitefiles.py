import os
import yaml
from yaml import load

def update_website_files():

    def replace_oldfile_w_newfile(old_file, new_file):
        print('Replace: ', new_file)
        os.system('rm -f '+old_file)
        os.system('cp '+new_file+' '+old_file)

    # 1. load the list of online book files, folders and fileTypes
    with open('tex2html/config/website.yml') as file:
        vars = load(file, Loader=yaml.FullLoader)

    # 2. Iterate over files and replace old files with new ones 
    for file in vars['files']:
        end_file = os.path.join(vars['onlineBookFolder'],file)
        replace_oldfile_w_newfile(end_file, file)

    # 3. Iterate over figFolders 
    for folder in vars['figFolders']:
        fig_folder = os.path.join(folder, 'figures')
        end_folder = os.path.join(vars['onlineBookFolder'],fig_folder)
        os.system('mkdir -p '+end_folder)
        files = []
        for ext in vars['figFileTypes']:
            fig_files = [f for f in os.listdir(fig_folder) if (os.path.isfile(os.path.join(fig_folder, f)) and f.endswith(ext))]
            files.extend(fig_files)
        for file in files:
            replace_oldfile_w_newfile(os.path.join(end_folder, file),
                os.path.join(fig_folder, file))

    # 4. Iterate over code Folder
    code_files = [f for f in os.listdir('code') if (os.path.isfile(os.path.join('code', f)) and f.endswith(vars['codeFileType']))]
    end_folder = os.path.join(vars['onlineBookFolder'],'code')
    for file in code_files:
        replace_oldfile_w_newfile(os.path.join(end_folder, file),
                os.path.join('code', file))
            
    # 5. Iterate over tex2html 
    for folder, ext in vars['tex2htmlFolderFileType'].items():
        tex2html_folder = os.path.join('tex2html', folder)
        end_folder = os.path.join(vars['onlineBookFolder'], tex2html_folder)
        # Make a list of files in the folder that end with the file ext
        os.system('mkdir -p '+end_folder)
        files = [f for f in os.listdir(tex2html_folder)
        if (os.path.isfile(os.path.join(tex2html_folder, f)) and f.endswith(ext))]
        for file in files:
            replace_oldfile_w_newfile(
                os.path.join(end_folder, file),
                os.path.join(tex2html_folder, file))

if __name__ == '__main__':
    update_website_files()