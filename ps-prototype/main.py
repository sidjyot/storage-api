from PyPowerStore import powerstore_conn

conn = powerstore_conn.PowerStoreConn('user',
                                      'password',
                                      'IP',
                                      False)


volume_create = conn.provisioning.create_volume(name='foo',
                                                size=1073741824)
all_replication_rules = conn.protection.get_replication_rules()
all_networks = conn.config_mgmt.get_networks()