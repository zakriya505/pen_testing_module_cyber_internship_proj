-- CVEs tailored for Metasploitable2 demonstration
CREATE TABLE IF NOT EXISTS cves (
    cve_id TEXT PRIMARY KEY,
    description TEXT
);

INSERT OR IGNORE INTO cves (cve_id, description) VALUES
('CVE-2011-2523', 'VSFTPD v2.3.4 Backdoor'),
('CVE-2007-2447', 'Samba "username map script" Command Execution'),
('CVE-2004-2687', 'UnrealIRCd 3.2.8.1 Backdoor Command Execution'),
('CVE-2006-2369', 'DistCC Daemon Command Execution'),
('CVE-2009-1151', 'Tomcat Manager Application Default Credentials'),
('CVE-2010-0738', 'Jboss JMX Console Deployer Upload'),
('CVE-2012-1823', 'PHP CGI Argument Injection'),
('CVE-2014-6271', 'GNU Bash Shellshock'),
('CVE-2008-1930', 'TWiki Debug Parameter Command Execution'),
('CVE-2010-2075', 'ProFTPD 1.3.2b Backdoor Command Execution');

