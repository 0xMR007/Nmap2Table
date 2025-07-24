
### Host : 10.10.6.53

| Port | Protocol | State | Service | Version |
|------|----------|-------|---------|---------|
| 135 | tcp | open | msrpc | Microsoft Windows RPC
| 139 | tcp | open | netbios-ssn | Microsoft Windows netbios-ssn
| 445 | tcp | open | microsoft-ds | Windows 7 Professional 7601 Service Pack 1 microsoft-ds
| 3389 | tcp | open | ms-wbt-server | Microsoft Terminal Service
| 5357 | tcp | open | http | Microsoft HTTPAPI httpd2.0
| 8000 | tcp | open | http | Icecast streaming media server
| 49152 | tcp | open | msrpc | Microsoft Windows RPC
| 49153 | tcp | open | msrpc | Microsoft Windows RPC
| 49154 | tcp | open | msrpc | Microsoft Windows RPC
| 49158 | tcp | open | msrpc | Microsoft Windows RPC
| 49159 | tcp | open | msrpc | Microsoft Windows RPC
| 49161 | tcp | open | msrpc | Microsoft Windows RPC

```bash
Port 3389 :
rdp-ntlm-info:

  Target_Name: DARK-PC
  NetBIOS_Domain_Name: DARK-PC
  NetBIOS_Computer_Name: DARK-PC
  DNS_Domain_Name: Dark-PC
  DNS_Computer_Name: Dark-PC
  Product_Version: 6.1.7601
  System_Time: 2025-07-23T11:52:22+00:00

ssl-date:
2025-07-23T11:52:27+00:00; +1s from scanner time.

ssl-cert:
Subject: commonName=Dark-PC
Not valid before: 2025-07-22T11:47:43
Not valid after:  2026-01-21T11:47:43

Port 5357 :
http-title:
Service Unavailable

http-server-header:
Microsoft-HTTPAPI/2.0

Port 8000 :
http-title:
Site doesn't have a title (text/html).

```