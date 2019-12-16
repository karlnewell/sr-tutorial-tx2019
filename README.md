[Support for Juniper vLab](#juniper-vlab)

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
```
ansible-playbook -e variable_hosts=srtut_vmx lab-config.yml \
  -e sr_enabled=True
  ```

Reboot the routers to update the SRGB (only need to perform this once)  
```ansible-playbook -e variable_hosts=srtut_vmx lab-reboot.yml```

## LDP disabled  
```
ansible-playbook -e variable_hosts=srtut_vmx lab-config.yml \
  -e sr_enabled=True -e ldp_disabled=True
  ```

## TI-LFA enabled
```
ansible-playbook -e variable_hosts=srtut_vmx lab-config.yml \
  -e sr_enabled=True -e ldp_disabled=True -e lfa_enabled=True
```

# Juniper vLab
This tutorial works with this Juniper vLab (you need a free login), https://jlabs.juniper.net/vlabs/portal/ospf-multi-area/

The topology and IPs, https://jlabs.juniper.net/assets/img/campaign/vlabs/ospf-multi-area-diagram.jpg

Edit the `srvlabs_vmx` section of `hosts.ini` to match the public IPs and NETCONF ports provided by the vLab (mouse over the nodes, once the lab is started, to get IP/port info).

You should run the ansible playbooks from your local host and connect via the public IPs/ports.

When running playbooks, change the variable_hosts to `variable_hosts=srvlabs_vmx`, e.g.

```
ansible-playbook -e variable_hosts=srvlabs_vmx lab-config.yml -e sr_enabled=True -e ldp_disabled=True -e lfa_enabled=True
```
