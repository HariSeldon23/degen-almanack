# .github/scripts/bump_version.py
import sys
import yaml
import semver
from pathlib import Path

def read_version():
    version_file = Path('version.txt')
    if not version_file.exists():
        return '0.1.0'
    return version_file.read_text().strip()

def write_version(version):
    with open('version.txt', 'w') as f:
        f.write(version)
    
    # Update _quarto.yml
    with open('_quarto.yml', 'r') as f:
        config = yaml.safe_load(f)
    
    config['book']['date'] = f"v{version}"
    
    with open('_quarto.yml', 'w') as f:
        yaml.dump(config, f, sort_keys=False)

def main():
    bump_type = sys.argv[1] if len(sys.argv) > 1 else 'minor'
    current_version = read_version()
    
    ver = semver.VersionInfo.parse(current_version)
    if bump_type == 'major':
        new_version = str(ver.bump_major())
    else:
        new_version = str(ver.bump_minor())
    
    write_version(new_version)
    print(f"Bumped version from {current_version} to {new_version}")

if __name__ == '__main__':
    main()