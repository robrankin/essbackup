# essbackup - TP-Link Easy Smart Switch config backup

Cribbed from [essstat](https://github.com/psmode/essstat) by [Peter Smode](https://github.com/psmode)

Quick and dirty script to dump the config of a TP-Link Easy Smart Switch to a local file named `<IP OF SWITCH>_config.cfg`.

## Example

    python backup.py <IP_OR_HOSTNAME> -p <PASSWORD> -u <USERNAME>
