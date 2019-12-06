# Setup
Use a python virtualenv
```
python3 -m venv venv
source venv/bin/activate
```

Update pip and install requirements
```
pip install --upgrade pip
pip install -r requirements.txt
```
# Checkpoints
## Base config  
```ansible-playbook -e variable_hosts=srtut_vmx lab-config.yml```

## Segment routing enabled  
```ansible-playbook -e variable_hosts=srtut_vmx lab-config.yml -e sr_enabled=True```

Reboot the routers to update the SRGB (only need to perform this once)
```ansible-playbook -e variable_hosts=srtut_vmx lab-reboot.yml```

## LDP disabled  
```ansible-playbook -e variable_hosts=srtut_vmx lab-config.yml -e sr_enabled=True -e ldp_disabled=True```

## TI-LFA enabled
```ansible-playbook -e variable_hosts=srtut_vmx lab-config.yml -e sr_enabled=True -e ldp_disabled=True -e lfa_enabled=True```
