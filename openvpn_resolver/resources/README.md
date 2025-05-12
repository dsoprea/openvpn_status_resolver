# Description

Given an OpenVPN status file, provide a tool that can export OpenVPN client
names and IPs as BASH exports or JSON data.


# Install

To install, you must clone recursively:

```
$ git clone --recurse-submodules https://github.com/dsoprea/openvpn_status_resolver.git openvpn_status_resolver
$ pip install openvpn_status_resolver
$ pip install openvpn_resolver/vendor/openvpn-status
```

Because of a newer datetime format in OpenVPN and an unmerged fix in the parsing
library, we must manually install a forked version of it.


# Usage

The OpenVPN server can record client IP assignments in a status file. The status
file is configured via the `status` directive in the OpenVPN.

## Example Status File

Given the following data:

```
OpenVPN CLIENT LIST
Updated,2025-05-12 02:40:21
Common Name,Real Address,Bytes Received,Bytes Sent,Connected Since
client3,1.2.3.4:47016,3728,3786,2025-05-17 00:56:36
client2,1.2.3.4:37424,13216,13388,2025-05-17 00:00:42
client,1.2.3.4:60082,3727,3786,2025-05-17 00:56:36
ROUTING TABLE
Virtual Address,Common Name,Real Address,Last Ref
10.8.0.2,client,1.2.3.4:60082,2025-05-17 00:56:37
10.8.0.4,client2,1.2.3.4:37424,2025-05-17 00:00:43
10.8.0.5,client3,1.2.3.4:47016,2025-05-17 00:56:37
GLOBAL STATS
Max bcast/mcast queue length,0
END
```

The output will be:

```
$ osr_export --status-filepath status.log
export OPENVPN_CLIENT_CLIENT_INTERNAL_IP="10.8.0.2"
export OPENVPN_CLIENT_CLIENT2_INTERNAL_IP="10.8.0.4"
export OPENVPN_CLIENT_CLIENT3_INTERNAL_IP="10.8.0.5"
```

It can also be formatted as JSON:

```
$ osr_export --status-filepath status.log --json
{
    "client2": "10.8.0.4",
    "client3": "10.8.0.5",
    "client": "10.8.0.2"
}
```

The status file's file-path can also be provided via environment:

```
$ OSR_STATUS_FILEPATH=status.log osr_export
export OPENVPN_CLIENT_CLIENT_INTERNAL_IP="10.8.0.2"
export OPENVPN_CLIENT_CLIENT2_INTERNAL_IP="10.8.0.4"
export OPENVPN_CLIENT_CLIENT3_INTERNAL_IP="10.8.0.5"
```
