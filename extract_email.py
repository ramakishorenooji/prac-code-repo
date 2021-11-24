# find email address from a document.
# regex findall is used in this scenario to extract email address
# Raw text
text = "Duis info@geeksforgeeks.com convallis. Parturient montes nascetur ridiculus mus \
geeksforgeeks@rocks.xyzee mauris 195.162.10.5 Odio eu feugiat pre@rsos_tium.index nibh ipsum consequat love@gfg.in \
pretium aenean pharetra magna ac placerat. Vitae justo eget magna fermentum iaculis eu non."

import re

email_ids = re.findall(r"[A-Za-z0-9./+%]+\@[A-Za-z0-9]+\.[A-Za-z]{2,}", text)
ip_addr = re.findall(
    r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",
    text,
)
print(email_ids)
print(ip_addr)
