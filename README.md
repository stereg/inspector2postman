# inspector2postman
Script for taking ACI inspector output and converting it into a Google Postman Collection file that can be imported

# Description
The ACI APIC (Application Policy Infrastructure Controller) supports a convenient 'ACI Inspector' tool that records the actual JSON calls to the APIC when a user is interacting with it.  This is also useful for getting started with developing for ACI, as in addition to reading the documentation, a developer can see the calls in real time.

After copying and pasting desired incremental configuration changes through the APIC GUI, recorded by the ACI Inspector, a bit of cleanup can be used to convert these PUT strings into Google Postman requests.  This is extremely easy, but time consuming if the request list becomes more than a few lines.  Additionally, variables will usually be introduced to enable rapid deployment of similar tenants (e.g. creating base e-store templates for multiple separate tenants).  inspector2postman instead takes an input file that is a copy/paste from the ACI inspector, and then produces an output file that can be imported into Google Postman as a collection.

There are plans for an even more user friendly interface if this tool proves useful for anyone besides me.

# Installation
All you need is Python - I have tested with Python 2.7.5

# Usage
Usage: inspector2postman.py <inspector_output_file> <formatted_postmancoll_file>

The script will create a file with the name you have entered as <formatted_postmancoll_file>

There is minimal error checking and testing, but for now the tool is serving its function as a step towards accelerating adoption of Postman utilization when building ACI scripts, without even needing to read the ACI development guide (beyond the authentication call ;)
