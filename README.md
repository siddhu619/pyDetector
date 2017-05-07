# pyDetector
Pydetector is pure python based IDS/IPS system which captures packets in the network analyzes and prevent various attacks like DOS, DDOS, Ping of Death, SQL injection, Smurf attack , NMAP Probes, TCP Syn Flood, etc.

The approach to design an IDPS(Intrusion Detection and Prevention System) such as PyDetector is to define network behavior patterns that indicate intrusive or improper use of the network and look for the occurrence of those patterns.

The description of the proposed system is divided into three sections

  The IDS module which monitors a local network and captures information about data packet transmission. This module will also perform processing and parsing of captured data and save the data into MySQL database.

  The IPS module which identifies the intrusive or abnormal behavior and applies obstructive rules in iptables to stop any such further occurrences. It also keeps a database of the rules applied.

  The GUI module which works on Django web application framework. A graphical interface is created which shows the alerts and subsequent logs recorded. Also a web service is created using HTML with its base as Django for client use.

