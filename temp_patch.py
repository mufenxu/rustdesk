import re

file_path = r'c:\Users\25912\Desktop\rustdesk\.github\workflows\flutter-build.yml'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'(if \[ -n "\$\{\{ env\.RS_PUB_KEY \}\}" \]; then\n\s*sed -i -e \'s/pub const RS_PUB_KEY: \\&str = ".*";/pub const RS_PUB_KEY: \\&str = "\$\{\{ env\.RS_PUB_KEY \}\}";/g\' libs/hbb_common/src/config\.rs\n\s*fi)')

new_block = r'''\1
          if [ -n "${{ env.API_SERVER }}" ]; then
            sed -i -e "s|https://admin.rustdesk.com|${{ env.API_SERVER }}|g" src/common.rs
          fi'''

new_content = pattern.sub(new_block, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Patched {file_path}")
